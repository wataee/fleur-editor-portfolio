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
// 2. Patch Astro core build CSS resolution on Windows symlink/OneDrive paths
const internalFile = 'node_modules/astro/dist/core/build/internal.js';
if (fs.existsSync(internalFile)) {
  let internalCode = fs.readFileSync(internalFile, 'utf8');
  const oldGetPage = 'function getPageDataByViteID(internals, viteid) {\n  if (internals.pagesByViteID.has(viteid)) {\n    return internals.pagesByViteID.get(viteid);\n  }\n  return void 0;\n}';
  const newGetPage = 'function getPageDataByViteID(internals, viteid) {\n  if (internals.pagesByViteID.has(viteid)) {\n    return internals.pagesByViteID.get(viteid);\n  }\n  for (const [key, value] of internals.pagesByViteID.entries()) {\n    if (value.component && viteid.endsWith(value.component)) {\n      return value;\n    }\n  }\n  return void 0;\n}';
  if (internalCode.includes(oldGetPage)) {
    internalCode = internalCode.replace(oldGetPage, newGetPage);
    fs.writeFileSync(internalFile, internalCode);
    console.log('Successfully patched Astro getPageDataByViteID for Windows paths');
  } else if (internalCode.includes('value.component && viteid.endsWith')) {
    console.log('Astro getPageDataByViteID already patched');
  }
}

// 3. Patch Astro vite-plugin-astro-server/vite.js for Windows OneDrive / symlink paths
const viteServerFile = 'node_modules/astro/dist/vite-plugin-astro-server/vite.js';
if (fs.existsSync(viteServerFile)) {
  let vCode = fs.readFileSync(viteServerFile, 'utf8');
  if (!vCode.includes('id = fs.realpathSync(id)')) {
    const target = 'async function* crawlGraph(loader, _id, isRootFile, scanned = /* @__PURE__ */ new Set()) {\n  const id = unwrapId(_id);';
    const replacement = 'async function* crawlGraph(loader, _id, isRootFile, scanned = /* @__PURE__ */ new Set()) {\n  let id = unwrapId(_id);\n  try {\n    if (fs.existsSync(id)) {\n      id = fs.realpathSync(id).replace(/\\\\/g, "/");\n    }\n  } catch {}\n  let moduleEntriesForId = isRootFile ? (\n    loader.getModulesByFile(id) ?? /* @__PURE__ */ new Set()\n  ) : (\n    /* @__PURE__ */ new Set([loader.getModuleById(id)])\n  );\n  if ((!moduleEntriesForId || moduleEntriesForId.size === 0) && isRootFile) {\n    const byId = loader.getModuleById(id);\n    if (byId) moduleEntriesForId = new Set([byId]);\n  }';
    if (vCode.includes(target)) {
      vCode = 'import fs from "node:fs";\n' + vCode.replace(target, replacement);
      vCode = vCode.replace('if (id === entry.id) {', 'const matchesId = id === entry.id || (entry.file && id === entry.file.replace(/\\\\/g, "/"));\n    if (matchesId) {');
      fs.writeFileSync(viteServerFile, vCode);
      console.log('Successfully patched Astro vite-plugin-astro-server/vite.js');
    }
  } else {
    console.log('Astro vite.js already patched');
  }
}

