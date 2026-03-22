# AMC 10 Mock Tests & Practice Resources

High-quality AMC 10 mock tests and practice resources, collected from AoPS community, DMC contests, and other sources.

## Quick Start

```bash
# Download all mock tests
python3 download_amc10.py --all

# Download only MockAMC collection (50+ sets)
python3 download_amc10.py --mockamc
```

## Downloaded Resources

After running the script, you'll have:

| Directory | Contents | Count |
|-----------|----------|-------|
| `amc10_mocks/MockAMC/` | AoPS community mock tests (Problems + Solutions) | ~65 files |
| `amc10_mocks/DMC_MockContests/` | DMC/KMMC contest series PDFs | ~46 files |
| `amc10_mocks/ProblemBank/` | Problems organized by topic | ~61 files |
| `amc10_mocks/HomemadeProblems/` | David Altizio's original problem collection | 1 PDF |
| `amc10_mocks/github_tools/` | Source code tools for generating more tests | 11 repos |

## Sources

- [MockAMC](https://mockamc.github.io) — Curated collection of AoPS mock tests
- [AoPS Wiki](https://artofproblemsolving.com/wiki/index.php/Mock_Amc_10) — Full mock contest list
- [DeToasty3](https://detoasty3.github.io) — DMC mock contest series
- [David Altizio](https://davidaltizio.web.illinois.edu) — Homemade Problem Collection
- [ZIML](https://ziml.areteem.org) — Practice contests
- [AMC Trainer](https://andrewboldi.github.io/AMC-Trainer/) — Online practice
- [AMC Tesseract](https://amctesseract.github.io) — Web app for practice
- [MathPrepPro](https://www.mathpreppro.com) — Online mock exams
- [Po-Shen Loh LIVE](https://live.poshenloh.com/past-contests) — Past contests PDF
- [Dr. Xue's Math School](https://www.xuemath.org/amc10-resources) — Google Drive archives

## Tools

| Tool | Description |
|------|-------------|
| `amc_prep/` | Python scraper → generates random practice PDFs from AoPS |
| `AMC_ProblemSetCreator/` | HuggingFace app → random problem set generator |
| `PrepAMC/` | Shell script → download from AoPS |
| `amc_pdf_tool/` | Bash+LaTeX → generate beautiful PDFs |

## Large Files Note

PDF files (408 total, ~217MB) are not committed to this repo due to size.
Run `download_amc10.py --all` to download them, or store them separately.
