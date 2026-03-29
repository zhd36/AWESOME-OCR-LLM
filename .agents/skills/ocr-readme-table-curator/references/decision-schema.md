# Decision Schema

Create a JSON file with one top-level key: `insertions`.

```json
{
  "insertions": [
    {
      "target": "Visual Text Parsing",
      "date_iso": "2026-03-26",
      "dedupe_keys": {
        "paper_id": "2603.22709",
        "name": "PP-OCRv5",
        "title": "PP-OCRv5: A Specialized 5M-Parameter Model Rivaling Billion-Parameter Vision-Language Models on OCR Tasks"
      },
      "row": "| [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.22709) | `PP-OCRv5` | PaddlePaddle | PP-OCRv5: A Specialized 5M-Parameter Model Rivaling Billion-Parameter Vision-Language Models on OCR Tasks | - | Mar. 2026 |"
    },
    {
      "target": "Benchmarks and Evaluation",
      "date_iso": "2026-03-26",
      "dedupe_keys": {
        "paper_id": "2603.22578",
        "name": "DISCO",
        "title": "DISCO: Document Intelligence Suite for COmparative Evaluation"
      },
      "row": "| [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.22578) | `DISCO` | A comparative evaluation suite for document intelligence systems covering OCR, parsing, and downstream extraction behavior. | - | Mar. 2026 |"
    }
  ]
}
```

## Field Rules

- `target`
  Plain-text section or subsection name from `references/taxonomy-and-tables.md`.

- `date_iso`
  ISO date used only for ordering within the new batch. Use the paper's announcement or submission date.

- `dedupe_keys`
  Include whatever is available, but prefer `paper_id`, `name`, and `title`.
  When `paper_id` is present, treat it as the authoritative duplicate key.
  Same displayed `name` is acceptable when the `paper_id` is different.

- `row`
  Complete Markdown table row ready to insert.

The merge script inserts rows deterministically but does not decide whether a paper belongs in the README.
