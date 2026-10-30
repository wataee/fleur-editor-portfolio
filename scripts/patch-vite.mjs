import fs from 'node:fs';

const file = 'node_modules/astro/node_modules/vite/dist/node/chunks/dep-CkSfqg8D.js';
let code = fs.readFileSync(file, 'utf8');

const target = 'for (const id in depsInfo) {\n        const output = esbuildOutputFromId(';
const replacement = `for (const id in depsInfo) {
        let output = esbuildOutputFromId(meta.outputs, id, processingCacheDir);
        if (!output) {
          const flatName = flattenId(id);
          for (const k in meta.outputs) {
            if (k.includes(flatName) || k.endsWith(flatName + '.js')) {
              output = meta.outputs[k];
              break;
            }
          }
        }
        if (!output) {
          console.warn("[Vite Patch] Skipping unmapped output for dep:", id);
          continue;
        }`;

if (code.includes('const output = esbuildOutputFromId(')) {
  code = code.replace(/for \(const id in depsInfo\) \{\s*const output = esbuildOutputFromId\([^)]+\);/, replacement);
  fs.writeFileSync(file, code);
  console.log('Successfully patched Vite 6 esbuildOutputFromId fallback');
} else {
  console.log('Target not found in', file);
}
