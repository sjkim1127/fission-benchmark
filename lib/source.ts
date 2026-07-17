import { readFile, readdir } from "fs/promises";
import path from "path";

export type FunctionSourceEntry = {
  functionName: string;
  sourcePath: string;
  /** Extracted function body, or whole file if extraction fails. */
  code: string;
  /** True when a single-function extract succeeded. */
  extracted: boolean;
};

/**
 * Extract one C function definition by name (brace-matched).
 * Mirrors runner/scoring.py::extract_function_source best-effort.
 */
function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

export function extractFunctionSource(
  source: string,
  functionName: string,
): string {
  const stripped = source
    .replace(/\/\*[\s\S]*?\*\//g, "")
    .replace(/\/\/[^\n]*/g, "");

  const re = new RegExp(
    `(?:^|\\n)(?:[\\w\\s*,<>\\[\\]]+?)?\\b${escapeRegExp(functionName)}\\s*\\(`,
    "gm",
  );

  let match: RegExpExecArray | null;
  while ((match = re.exec(stripped)) !== null) {
    const start = match.index;
    const rest = stripped.slice(start);
    let parenDepth = 0;
    let braceStart = -1;
    for (let idx = 0; idx < rest.length; idx++) {
      const ch = rest[idx];
      if (ch === "(") parenDepth += 1;
      else if (ch === ")") parenDepth -= 1;
      else if (ch === "{" && parenDepth === 0) {
        braceStart = start + idx;
        break;
      } else if (ch === ";" && parenDepth === 0) {
        break;
      }
    }
    if (braceStart === -1) continue;

    let depth = 0;
    for (let idx = braceStart; idx < stripped.length; idx++) {
      const c = stripped[idx];
      if (c === "{") depth += 1;
      else if (c === "}") {
        depth -= 1;
        if (depth === 0) {
          return stripped.slice(start, idx + 1).trim();
        }
      }
    }
    break;
  }
  return "";
}

async function loadManifestMap(
  corpusRoot: string,
): Promise<Map<string, string>> {
  const out = new Map<string, string>();
  const manDir = path.join(corpusRoot, "manifests");
  let files: string[] = [];
  try {
    files = (await readdir(manDir)).filter((f) => f.endsWith(".json"));
  } catch {
    return out;
  }
  for (const file of files) {
    try {
      const raw = JSON.parse(await readFile(path.join(manDir, file), "utf8")) as {
        functions?: Array<{ name?: string; source?: string }>;
      };
      for (const fn of raw.functions || []) {
        if (fn.name && fn.source) out.set(fn.name, fn.source);
      }
    } catch {
      // skip bad manifest
    }
  }
  return out;
}

/**
 * Load original C function sources for a corpus split (dev / holdout).
 * Used by the NIR vs HIR dashboard page only — never for ranking.
 */
export async function loadFunctionSources(
  corpus = "dev",
): Promise<Record<string, FunctionSourceEntry>> {
  const root = path.join(process.cwd(), "corpus", corpus);
  const mapping = await loadManifestMap(root);
  const result: Record<string, FunctionSourceEntry> = {};
  const fileCache = new Map<string, string>();

  for (const [functionName, relSource] of mapping) {
    const candidates = [
      path.join(root, relSource),
      path.join(root, "source", "c", path.basename(relSource)),
      path.join(root, "source", "cpp", path.basename(relSource)),
      path.join(root, "source", "rust", path.basename(relSource)),
      path.join(root, "source", "go", path.basename(relSource)),
    ];
    let abs = candidates[0];
    let fileText = fileCache.get(abs);
    if (fileText === undefined) {
      fileText = "";
      for (const cand of candidates) {
        try {
          fileText = await readFile(cand, "utf8");
          abs = cand;
          break;
        } catch {
          // try next
        }
      }
      fileCache.set(abs, fileText);
    }
    const displayPath = path.relative(root, abs) || relSource;
    if (!fileText) {
      result[functionName] = {
        functionName,
        sourcePath: relSource,
        code: "",
        extracted: false,
      };
      continue;
    }
    const extracted = extractFunctionSource(fileText, functionName);
    result[functionName] = {
      functionName,
      sourcePath: displayPath,
      code: extracted || fileText,
      extracted: Boolean(extracted),
    };
  }
  return result;
}
