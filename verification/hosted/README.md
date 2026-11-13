# Hosted mathematical rendering

The [pull-request workflow](../../.github/workflows/hosted-math.yml) checks the exact proposed head commit for pull requests from this repository. It reads every tracked Markdown page at that commit from its public GitHub URL. The unchanged collector records the actual hosted article at widths 1440 and 760 pixels, compares its accessible mathematics against the pinned source, and saves full-page PNGs, HTML, source inventories and JSON reports. It does not replace the scientific proofs or the separate visual review of equation bodies and layout.

The workflow uses Ubuntu 24.04, Node 22, Playwright 1.56.1, MathJax 3.2.1 and Chromium. It requests read-only repository contents, checks out the exact head with credential persistence disabled, and uses no repository secrets. Failed captures fail the job; the artifact upload runs even after failure. Download `hosted-math-HEAD_SHA` from the Actions run to inspect `hosted-math/hosted-report.json` and the captured pages. A representative README probe runs first and is retained in `hosted-probe/`. Artifacts are retained for 14 days.

To reproduce from a complete local Git checkout with Python 3, Node 22 and public browser access to GitHub:

```bash
capture_runtime=$(mktemp -d)
capture_output=$(mktemp -d)
capture_revision=$(git rev-parse HEAD)
npm install --prefix "$capture_runtime" playwright@1.56.1 mathjax-full@3.2.1
node "$capture_runtime/node_modules/playwright/cli.js" install --with-deps chromium
NODE_PATH="$capture_runtime/node_modules" \
  node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Diffusive-Quantum-Storage \
  --revision "$capture_revision" \
  --output "$capture_output"
```

No `--page` option is supplied: the default captures the complete Markdown tree at both widths. The output directory must initially be empty. The two helper files are distributed unchanged; the Python checker is invoked by the collector. A passing comparison establishes only its recorded source-to-host checks. It is not a device simulation, an independent proof or a complete visual-layout certification.
