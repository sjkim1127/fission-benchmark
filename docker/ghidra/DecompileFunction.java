// GhidraScript: Decompile a single function at a given address and print JSON to stdout.
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;

public class DecompileFunction extends GhidraScript {
    @Override
    public void run() throws Exception {
        String addrStr = System.getProperty("decomp.addr", "");
        if (addrStr.isEmpty()) {
            println("{\"error\": \"decomp.addr not set\"}");
            return;
        }
        Address addr = currentProgram.getAddressFactory().getAddress(addrStr);
        Function func = currentProgram.getFunctionManager().getFunctionAt(addr);
        if (func == null) {
            println("{\"error\": \"no function at " + addrStr + "\"}");
            return;
        }
        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        DecompileResults res = decomp.decompileFunction(func, 60, monitor);
        if (!res.decompileCompleted()) {
            println("{\"error\": \"decompile failed\"}");
            return;
        }
        String code = res.getDecompiledFunction().getC();
        // JSON-escape the code
        code = code.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\r", "");
        println("{\"name\": \"" + func.getName() + "\", \"code\": \"" + code + "\"}");
    }
}
