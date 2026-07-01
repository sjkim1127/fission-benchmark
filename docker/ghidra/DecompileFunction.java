// GhidraScript: Decompile multiple functions and print JSON.
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import java.util.ArrayList;

public class DecompileFunction extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length == 0) {
            println("{\"error\": \"no addresses specified\"}");
            return;
        }

        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);

        ArrayList<String> jsonResults = new ArrayList<>();

        for (String addrStr : args) {
            try {
                Address addr = currentProgram.getAddressFactory().getAddress(addrStr);
                Function func = currentProgram.getFunctionManager().getFunctionAt(addr);
                if (func == null) {
                    jsonResults.add("{\"addr\": \"" + addrStr + "\", \"error\": \"no function at " + addrStr + "\"}");
                    continue;
                }
                DecompileResults res = decomp.decompileFunction(func, 60, monitor);
                if (!res.decompileCompleted()) {
                    jsonResults.add("{\"addr\": \"" + addrStr + "\", \"error\": \"decompile failed\"}");
                    continue;
                }
                String code = res.getDecompiledFunction().getC();
                code = code.replace("\\", "\\\\").replace("\"", "\\\"").replace("\r\n", "\\n").replace("\n", "\\n").replace("\r", "\\n");
                jsonResults.add("{\"addr\": \"" + addrStr + "\", \"name\": \"" + func.getName() + "\", \"code\": \"" + code + "\"}");
            } catch (Exception e) {
                jsonResults.add("{\"addr\": \"" + addrStr + "\", \"error\": \"" + e.getMessage() + "\"}");
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < jsonResults.size(); i++) {
            sb.append(jsonResults.get(i));
            if (i < jsonResults.size() - 1) {
                sb.append(",");
            }
        }
        sb.append("]");
        println("===BATCH_RESULT===" + sb.toString());
    }
}
