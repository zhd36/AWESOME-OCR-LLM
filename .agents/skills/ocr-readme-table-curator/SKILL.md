---
name: ocr-readme-table-curator
description: Curate papers from a structured weekly JSON list into the hand-maintained tables in AWESOME-OCR-LLM `README.md`. Use when Codex needs to read `paper-daily` weekly outputs or similar JSON paper lists, decide which OCR/document papers are strong enough for the awesome list, map accepted papers into the repository taxonomy, and update the correct Markdown tables without duplicating existing entries.
---

# OCR README Table Curator

Use this skill when the task is not "summarize recent papers", but "decide which papers deserve permanent inclusion in the awesome list and patch the right README table."

The input is usually a weekly JSON bundle produced by `paper-daily`, for example `data/topics/document_ocr/weekly/...json`. The output is a reviewed change to `README.md`, not a report.

## Read First

1. Read `README.md`.
2. Read [references/inclusion-rubric.md](references/inclusion-rubric.md).
3. Read [references/taxonomy-and-tables.md](references/taxonomy-and-tables.md).
4. Read [references/metadata-enrichment.md](references/metadata-enrichment.md) when filling `Primary affiliation` or `GitHub`.
5. Read [references/decision-schema.md](references/decision-schema.md) only when preparing the merge input for the helper script.

## Workflow

### 1. Narrow the weekly JSON to awesome-list candidates

- Start from the papers already present in the JSON input.
- Treat the awesome list as stricter than the weekly recall output.
- Reject papers that are only adjacent to OCR/document intelligence.
- Prefer a short, high-quality diff over a noisy batch insertion.

### 2. Apply the quality bar

- Include a paper only if both are true:
  - repository fit is strong
  - paper quality or expected impact is high enough to justify a permanent README entry
- Use accepted venue, strong technical report, released code/model/dataset, or clear benchmark value as positive evidence.
- If the fit is borderline, skip it. Do not add "maybe" papers into the permanent tables.

### 3. Map each accepted paper to exactly one target table

- Use the plain-text target names from [references/taxonomy-and-tables.md](references/taxonomy-and-tables.md).
- Prefer the most specific subsection when working under `Specialized Model`.
- Do not force a paper into `Visual Text Understanding` just because it mentions documents; that section should stay document-centric.

### 4. Actively search metadata for accepted papers

- For every accepted paper, actively search for `Primary affiliation` and `GitHub` before defaulting to `-`.
- Search in this order:
  - the arXiv abstract page
  - official links named on the arXiv page or in the abstract
  - the paper PDF first page for author affiliations when needed
  - the official GitHub / Hugging Face / project page when the ownership is clear
- Keep this search targeted and short. The goal is to fill high-confidence metadata, not to spend most of the run on enrichment.
- If the signal stays ambiguous after a short search, use `-`.
- Never guess affiliations or attach a community-maintained repo as if it were official.

### 5. Enrich only the metadata you can justify

- `Venue`:
  - Prefer the generic arXiv paper badge unless an accepted venue is explicit and unambiguous.
  - Do not invent conference logo rows.
- `Name`:
  - Use the canonical model or benchmark name from the paper or official project.
  - Do not append editorial disambiguators such as `(Coarse-to-Fine)` just to avoid a collision.
  - If two rows share the same displayed name, keep the direct name and rely on the arXiv paper identity to distinguish them.
- `Primary affiliation`:
  - Use the primary lab/company/team that clearly owns the work.
  - Prefer the affiliation visible on the paper itself or the official project page.
  - If multiple affiliations appear and no single owner is clear, use `-`.
- `GitHub` or benchmark link:
  - Use the official repo/model/dataset page when high confidence.
  - For benchmark rows, a dataset or project homepage is acceptable when GitHub is not the canonical entry point.
  - If multiple unofficial reproductions exist, use `-`.
- `Date`:
  - Keep the README style such as `Mar. 2026`.

### 6. Build a decisions JSON and merge it with the helper script

- Prepare a JSON file that matches [references/decision-schema.md](references/decision-schema.md).
- Run:
  ```powershell
  python .agents/skills/ocr-readme-table-curator/scripts/merge_table_rows.py `
    --readme README.md `
    --decisions <path-to-decisions-json>
  ```
- The script performs only deterministic work:
  - locate the target table
  - detect duplicates
  - insert new rows near the top of that table
- The script does not decide what to include. That judgment stays with the agent.

### 7. Review the diff before finishing

- Check that every inserted row lands in the intended section.
- Check that no duplicate row was created under a different nearby section.
- Check that the table still renders as Markdown and the row has the right number of columns.
- Check that searched `Primary affiliation` and `GitHub` values are still high-confidence after the final row is assembled.
- If the change set is large, explain why each inserted paper passed the bar.

## Judgment Rules

- The weekly JSON is a recall surface, not a final curation surface.
- `included=true` in the weekly JSON does not imply README inclusion.
- Generic multimodal papers, application papers, and document-adjacent reasoning papers should usually stay out.
- When the paper is strong but the section is unclear, stop and classify first. Do not patch the README until the target section is clear.
- Same-name entries are allowed when they point to different arXiv papers.

## Typical Use

```text
Use $ocr-readme-table-curator to read a weekly JSON paper list, keep only strong OCR/document papers, and update README.md tables.
```

## Output Discipline

- Modify `README.md` only when you have at least one accepted paper.
- Do not create extra audit files unless the user asks for them.
- If no paper passes the bar, say so explicitly and leave `README.md` unchanged.
