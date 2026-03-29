# Taxonomy And Tables

Use plain-text target names when preparing merge decisions. The helper script matches these names against the actual emoji-prefixed headings in `README.md`.

## Top-Level Targets

- `Visual Text Parsing`
  Use for OCR, document parsing, OCR-free parsing, layout analysis, PDF parsing, document VLMs centered on parsing.

- `Visual Text Understanding`
  Use only when semantic document understanding is central and document-specific. Do not use for generic VLM papers.

- `Benchmarks and Evaluation`
  Use for datasets, benchmarks, evaluation suites, judge-based evaluation, and document/OCR test sets.

- `Visual Text Generation`
  Use for scene text generation, editing, glyph rendering, poster text rendering, and related text-centric generation.

## Specialized Model Subtargets

- `Document Dewarping`
- `Physical Structure Analysis`
- `Reading Order Prediction`
- `Mathematical Expression Recognition`
- `Geometry Problem-solving`
- `Table Understanding`
- `Chart Understanding`
- `Scene Text Spotting`

Use a specialized subtarget when the contribution clearly belongs there. Otherwise use `Visual Text Parsing`.

## Table Shapes

Most tables use six columns:

```text
| Venue | Name | Primary affiliation | Title | GitHub | Date |
```

`Benchmarks and Evaluation` uses five columns:

```text
| Venue | Benchmark Name | Description | Link | Date |
```

The merge script does not rewrite columns. The row string in the decisions JSON must already match the target table shape.

## Formatting Rules

- Prefer the generic arXiv paper badge when venue styling is unclear.
- Keep names in backticks, matching the existing README style.
- Keep names canonical. Do not add explanatory suffixes just to make a row name unique.
- Use `-` for unknown affiliation or missing GitHub.
- Use dates like `Mar. 2026`.
- Insert only one row per paper.
