// GhidraScript: Export function diagnostics in JSON for parity benchmarking.
// Modes:
//   functions
//   disasm | pcode | cfg | bundle   (+ address)
//   multi_bundle                     (+ comma-separated addresses)
// multi_bundle: ONE JVM run for many functions in the already-opened program.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.lang.Register;
import ghidra.program.model.listing.Parameter;
import ghidra.program.model.listing.VariableStorage;
import ghidra.program.model.pcode.PcodeOp;
import ghidra.program.model.pcode.Varnode;
import ghidra.program.model.block.SimpleBlockModel;
import ghidra.program.model.block.CodeBlock;
import ghidra.program.model.block.CodeBlockIterator;
import ghidra.program.model.block.CodeBlockReferenceIterator;
import ghidra.program.model.block.CodeBlockReference;

public class ExportParity extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 1) {
            println("===RESULT==={\"error\": \"missing mode argument\"}");
            return;
        }

        String mode = args[0];
        if (mode.equals("functions")) {
            emit(exportFunctionsJson());
            return;
        }

        if (args.length < 2) {
            println("===RESULT==={\"error\": \"missing address argument\"}");
            return;
        }

        if (mode.equals("multi_bundle")) {
            // args[1] = "0xA,0xB,0xC"  (requested entry addresses)
            String[] addrs = args[1].split(",");
            StringBuilder sb = new StringBuilder();
            sb.append("{\"schema\": \"ghidra-parity-multi-bundle-v1\", \"by_addr\": {");
            boolean first = true;
            for (String raw : addrs) {
                String addrStr = raw.trim();
                if (addrStr.isEmpty()) {
                    continue;
                }
                Function func = resolveFunction(addrStr);
                if (func == null) {
                    if (!first) sb.append(",");
                    first = false;
                    sb.append("\"").append(normalizeAddrKey(addrStr)).append("\": ");
                    sb.append("{\"error\": \"no function at ").append(jsonEscape(addrStr)).append("\"}");
                    continue;
                }
                if (!first) sb.append(",");
                first = false;
                // Key by the *requested* address so the client can look up by manifest addr.
                sb.append("\"").append(normalizeAddrKey(addrStr)).append("\": ");
                sb.append(exportBundleObject(func));
            }
            sb.append("}}");
            emit(sb.toString());
            return;
        }

        Function func = resolveFunction(args[1]);
        if (func == null) {
            println("===RESULT==={\"error\": \"no function at " + args[1] + "\"}");
            return;
        }

        if (mode.equals("disasm")) {
            emit(exportDisasmJson(func));
        } else if (mode.equals("pcode")) {
            emit(exportPcodeJson(func));
        } else if (mode.equals("cfg")) {
            emit(exportCfgJson(func));
        } else if (mode.equals("abi")) {
            emit(exportAbiJson(func));
        } else if (mode.equals("bundle")) {
            emit(exportBundleObject(func));
        } else {
            println("===RESULT==={\"error\": \"unknown mode " + mode + "\"}");
        }
    }

    private Function resolveFunction(String addrStr) throws Exception {
        Address addr = currentProgram.getAddressFactory().getAddress(addrStr);
        if (addr == null) {
            // try without 0x / with 0x
            if (addrStr.startsWith("0x") || addrStr.startsWith("0X")) {
                addr = currentProgram.getAddressFactory().getAddress(addrStr.substring(2));
            } else {
                addr = currentProgram.getAddressFactory().getAddress("0x" + addrStr);
            }
        }
        if (addr == null) {
            return null;
        }
        Function func = currentProgram.getFunctionManager().getFunctionAt(addr);
        if (func == null) {
            func = currentProgram.getFunctionManager().getFunctionContaining(addr);
        }
        return func;
    }

    private String normalizeAddrKey(String addrStr) {
        try {
            String hex = addrStr.trim().toLowerCase();
            if (hex.startsWith("0x")) {
                hex = hex.substring(2);
            }
            // canonical 0x + lowercase hex without leading zeros stripped carefully
            long v = Long.parseUnsignedLong(hex, 16);
            return String.format("0x%x", v);
        } catch (Exception e) {
            return addrStr.trim().toLowerCase();
        }
    }

    private String exportBundleObject(Function func) throws Exception {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        sb.append("\"schema\": \"ghidra-parity-bundle-v1\",");
        sb.append("\"address\": \"0x").append(func.getEntryPoint().toString()).append("\",");
        sb.append("\"name\": \"").append(jsonEscape(func.getName())).append("\",");
        sb.append("\"disasm\": ").append(exportDisasmJson(func)).append(",");
        sb.append("\"pcode\": ").append(exportPcodeJson(func)).append(",");
        sb.append("\"cfg\": ").append(exportCfgJson(func));
        sb.append("}");
        return sb.toString();
    }

    private void emit(String json) {
        println("===RESULT===" + json);
    }

    private String jsonEscape(String s) {
        if (s == null) {
            return "";
        }
        return s.replace("\\", "\\\\").replace("\"", "\\\"");
    }

    private String exportFunctionsJson() throws Exception {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        boolean first = true;
        for (Function func : currentProgram.getFunctionManager().getFunctions(true)) {
            if (!first) sb.append(",");
            first = false;
            sb.append(String.format(
                "{\"address\": \"0x%s\", \"name\": \"%s\", \"size\": %d, \"kind\": \"function\"}",
                func.getEntryPoint().toString(),
                jsonEscape(func.getName()),
                func.getBody().getNumAddresses()
            ));
        }
        sb.append("]");
        return sb.toString();
    }

    private String exportDisasmJson(Function func) throws Exception {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        boolean first = true;
        InstructionIterator insts = currentProgram.getListing().getInstructions(func.getBody(), true);
        while (insts.hasNext()) {
            Instruction inst = insts.next();
            if (!first) sb.append(",");
            first = false;

            byte[] bytes = inst.getBytes();
            StringBuilder byteStr = new StringBuilder();
            for (byte b : bytes) {
                byteStr.append(String.format("%02x", b & 0xff));
            }

            Address fall = inst.getFallThrough();
            Address[] flows = inst.getFlows();
            String branchTarget = (flows.length > 0) ? "\"0x" + flows[0].toString() + "\"" : "null";
            String operands = jsonEscape(inst.toString());

            sb.append(String.format(
                "{\"address\": \"0x%s\", \"bytes\": \"%s\", \"mnemonic\": \"%s\", \"operands\": \"%s\", \"length\": %d, \"fallthrough\": %s, \"branch_target\": %s}",
                inst.getMinAddress().toString(),
                byteStr.toString(),
                inst.getMnemonicString().toLowerCase(),
                operands,
                inst.getLength(),
                fall != null ? "\"0x" + fall.toString() + "\"" : "null",
                branchTarget
            ));
        }
        sb.append("]");
        return sb.toString();
    }

    private String exportPcodeJson(Function func) throws Exception {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        boolean first = true;
        int seq = 0;
        InstructionIterator insts = currentProgram.getListing().getInstructions(func.getBody(), true);
        while (insts.hasNext()) {
            Instruction inst = insts.next();
            PcodeOp[] ops = inst.getPcode();
            for (PcodeOp op : ops) {
                if (!first) sb.append(",");
                first = false;

                String outputStr = "null";
                Varnode out = op.getOutput();
                if (out != null) {
                    outputStr = String.format(
                        "{\"space\": \"%s\", \"offset\": \"0x%x\", \"size\": %d}",
                        out.getAddress().getAddressSpace().getName(),
                        out.getAddress().getOffset(),
                        out.getSize()
                    );
                }

                StringBuilder inputsStr = new StringBuilder();
                inputsStr.append("[");
                Varnode[] inputs = op.getInputs();
                for (int i = 0; i < inputs.length; i++) {
                    Varnode in = inputs[i];
                    if (i > 0) inputsStr.append(",");
                    inputsStr.append(String.format(
                        "{\"space\": \"%s\", \"offset\": \"0x%x\", \"size\": %d}",
                        in.getAddress().getAddressSpace().getName(),
                        in.getAddress().getOffset(),
                        in.getSize()
                    ));
                }
                inputsStr.append("]");

                sb.append(String.format(
                    "{\"seq\": %d, \"op\": \"%s\", \"output\": %s, \"inputs\": %s}",
                    seq++,
                    op.getMnemonic(),
                    outputStr,
                    inputsStr.toString()
                ));
            }
        }
        sb.append("]");
        return sb.toString();
    }

    private String exportCfgJson(Function func) throws Exception {
        SimpleBlockModel blockModel = new SimpleBlockModel(currentProgram);
        CodeBlockIterator blocks = blockModel.getCodeBlocksContaining(func.getBody(), monitor);

        StringBuilder blocksJson = new StringBuilder();
        blocksJson.append("[");
        boolean firstBlock = true;

        StringBuilder edgesJson = new StringBuilder();
        edgesJson.append("[");
        boolean firstEdge = true;

        while (blocks.hasNext()) {
            CodeBlock block = blocks.next();
            if (!firstBlock) blocksJson.append(",");
            firstBlock = false;

            // Inclusive last byte of last instruction (Fission adapter promotes
            // terminal_address + insn length to the same encoding).
            blocksJson.append(String.format(
                "{\"start\": \"0x%s\", \"end\": \"0x%s\"}",
                block.getMinAddress().toString(),
                block.getMaxAddress().toString()
            ));

            CodeBlockReferenceIterator dests = block.getDestinations(monitor);
            while (dests.hasNext()) {
                CodeBlockReference ref = dests.next();
                if (!firstEdge) edgesJson.append(",");
                firstEdge = false;
                edgesJson.append(String.format(
                    "{\"source\": \"0x%s\", \"target\": \"0x%s\", \"kind\": \"branch\"}",
                    block.getMinAddress().toString(),
                    ref.getDestinationAddress().toString()
                ));
            }
        }
        blocksJson.append("]");
        edgesJson.append("]");

        return "{\"blocks\": " + blocksJson.toString() + ", \"edges\": " + edgesJson.toString() + "}";
    }

    private String exportAbiJson(Function func) throws Exception {
        String conv = func.getCallingConventionName();
        if (conv == null || conv.isEmpty()) {
            conv = "unknown";
        }
        StringBuilder params = new StringBuilder();
        params.append("[");
        Parameter[] arr = func.getParameters();
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) params.append(",");
            params.append(parameterToJson(arr[i], i));
        }
        params.append("]");

        String retJson = "null";
        Parameter ret = func.getReturn();
        if (ret != null) {
            retJson = parameterToJson(ret, -1);
        }

        return String.format(
            "{\"status\": \"ok\", \"address\": \"0x%s\", \"name\": \"%s\", \"convention\": \"%s\", \"parameters\": %s, \"return\": %s}",
            func.getEntryPoint().toString(),
            jsonEscape(func.getName()),
            jsonEscape(conv),
            params.toString(),
            retJson
        );
    }

    private String parameterToJson(Parameter p, int index) {
        String loc = "unknown";
        int size = 0;
        try {
            size = p.getLength();
            // Prefer Register name (RCX/RAX) over raw register-space offsets ("00000008").
            Register reg = p.getRegister();
            VariableStorage storage = p.getVariableStorage();
            if (reg == null && storage != null && storage.isValid()) {
                reg = storage.getRegister();
            }
            if (reg != null) {
                loc = reg.getName().toLowerCase();
            } else if (storage != null && storage.isValid() && storage.isStackStorage()) {
                loc = String.format("stack+0x%x", storage.getStackOffset());
            } else if (storage != null && storage.isValid() && storage.getFirstVarnode() != null) {
                Varnode vn = storage.getFirstVarnode();
                Register r2 = currentProgram.getRegister(vn.getAddress(), vn.getSize());
                if (r2 == null) {
                    r2 = currentProgram.getRegister(vn.getAddress());
                }
                if (r2 != null) {
                    loc = r2.getName().toLowerCase();
                } else {
                    String space = vn.getAddress().getAddressSpace().getName();
                    if ("register".equalsIgnoreCase(space)) {
                        loc = String.format("reg+0x%x", vn.getOffset());
                    } else if ("stack".equalsIgnoreCase(space)) {
                        loc = String.format("stack+0x%x", vn.getAddress().getOffset());
                    } else {
                        loc = space.toLowerCase() + "+0x" + Long.toHexString(vn.getAddress().getOffset());
                    }
                }
            }
        } catch (Exception e) {
            loc = "unknown";
        }
        String name = p.getName() != null ? p.getName() : ("param_" + index);
        return String.format(
            "{\"index\": %d, \"name\": \"%s\", \"location\": \"%s\", \"size\": %d}",
            index,
            jsonEscape(name),
            jsonEscape(loc.toLowerCase()),
            size
        );
    }
}
