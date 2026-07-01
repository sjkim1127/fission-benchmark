// GhidraScript: Export function diagnostics in JSON format for parity benchmarking.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.pcode.PcodeOp;
import ghidra.program.model.pcode.Varnode;
import ghidra.program.model.block.SimpleBlockModel;
import ghidra.program.model.block.CodeBlock;
import ghidra.program.model.block.CodeBlockIterator;
import ghidra.program.model.block.CodeBlockReferenceIterator;
import ghidra.program.model.block.CodeBlockReference;

import java.util.ArrayList;

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
            exportFunctions();
        } else {
            if (args.length < 2) {
                println("===RESULT==={\"error\": \"missing address argument\"}");
                return;
            }
            String addrStr = args[1];
            Address addr = currentProgram.getAddressFactory().getAddress(addrStr);
            Function func = currentProgram.getFunctionManager().getFunctionAt(addr);
            if (func == null) {
                println("===RESULT==={\"error\": \"no function at " + addrStr + "\"}");
                return;
            }

            if (mode.equals("disasm")) {
                exportDisasm(func);
            } else if (mode.equals("pcode")) {
                exportPcode(func);
            } else if (mode.equals("cfg")) {
                exportCfg(func);
            } else {
                println("===RESULT==={\"error\": \"unknown mode " + mode + "\"}");
            }
        }
    }

    private void exportFunctions() throws Exception {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        boolean first = true;
        for (Function func : currentProgram.getFunctionManager().getFunctions(true)) {
            if (!first) sb.append(",");
            first = false;
            sb.append(String.format(
                "{\"address\": \"0x%s\", \"name\": \"%s\", \"size\": %d, \"kind\": \"function\"}",
                func.getEntryPoint().toString(),
                func.getName(),
                func.getBody().getNumAddresses()
            ));
        }
        sb.append("]");
        println("===RESULT===" + sb.toString());
    }

    private void exportDisasm(Function func) throws Exception {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        boolean first = true;
        InstructionIterator insts = currentProgram.getListing().getInstructions(func.getBody(), true);
        while (insts.hasNext()) {
            Instruction inst = insts.next();
            if (!first) sb.append(",");
            first = false;

            // Convert bytes to hex
            byte[] bytes = inst.getBytes();
            StringBuilder byteStr = new StringBuilder();
            for (byte b : bytes) {
                byteStr.append(String.format("%02x", b));
            }

            Address fall = inst.getFallThrough();
            Address[] flows = inst.getFlows();
            String branchTarget = (flows.length > 0) ? "0x" + flows[0].toString() : "null";

            sb.append(String.format(
                "{\"address\": \"0x%s\", \"bytes\": \"%s\", \"mnemonic\": \"%s\", \"operands\": \"%s\", \"length\": %d, \"fallthrough\": %s, \"branch_target\": %s}",
                inst.getMinAddress().toString(),
                byteStr.toString(),
                inst.getMnemonicString().toLowerCase(),
                inst.getDefaultOperandRepresentationList(0) != null ? inst.toString().replace("\"", "\\\"") : "",
                inst.getLength(),
                fall != null ? "\"0x" + fall.toString() + "\"" : "null",
                branchTarget.equals("null") ? "null" : "\"" + branchTarget + "\""
            ));
        }
        sb.append("]");
        println("===RESULT===" + sb.toString());
    }

    private void exportPcode(Function func) throws Exception {
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
        println("===RESULT===" + sb.toString());
    }

    private void exportCfg(Function func) throws Exception {
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

        println("===RESULT==={\"blocks\": " + blocksJson.toString() + ", \"edges\": " + edgesJson.toString() + "}");
    }
}
