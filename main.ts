// News-image entry for Sunday 22 November 2026 (Node 22, stdlib only).
// The entry is the PNG sitting next to this file: this program copies
// entry.png into the harness output directory, unchanged, byte for byte.
// The gate only ever sees the copied bytes, so nothing here transforms
// the image in any way.
//
// Outside the grader container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const here = new URL('./entry.png', import.meta.url);
copyFileSync(here, join(outDir, 'entry.png'));
