# Inclusion Rubric

The README tables are narrower than the weekly `paper-daily` output.

## Keep

Keep a paper only when it is both strongly relevant and strong enough for a permanent awesome-list entry.

Positive signals:

- end-to-end OCR or document parsing
- OCR-free document parsing with clear structure extraction value
- document-specific VLM or MLLM with a central OCR/document contribution
- OCR, document parsing, layout, reading order, formula, chart, table, scene text benchmark or dataset
- technical report with obvious community impact and released code/model
- strong scene text generation or editing work that fits the existing `Visual Text Generation` section

## Reject

Reject when the paper is mainly about something adjacent rather than core to this repository.

Common reject patterns:

- citation parsing, bibliography parsing, scholarly metadata extraction
- generic document grounding or scientific paper reasoning without OCR/parsing as the main contribution
- domain application pipelines for finance, clinical, legal, or enterprise documents
- generic multimodal models that merely support documents among many other modalities
- general image reasoning, pruning, or agent orchestration papers
- document HTML/CSS generation unless the core contribution is visual text rendering or editing and it clearly fits the existing generation section

## Borderline Rules

- If the paper is strong but would look out of place beside nearby entries, skip it.
- If the paper lacks obvious released artifacts and is only weakly better than existing entries, skip it.
- If the paper is more suitable for a short weekly update than a long-lived table, skip it.

## Examples From Recent Weekly Output

Likely keep:

- `PP-OCRv5`
- `Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing`
- `Towards Real-World Document Parsing via Realistic Scene Synthesis and Document-Aware Training`
- `TDATR`
- `DISCO`
- `MinerU-Diffusion`
- `Towards Training-Free Scene Text Editing`

Likely reject:

- `RenoBench`
- `DAGverse`
- `AnyDoc`
- `PaperVoyager`
- `Benchmarking Multi-Agent LLM Architectures for Financial Document Processing`
- `TimeTox`

These examples are guidance, not a substitute for reading the paper title and abstract.
