# Metadata Enrichment

Use this reference only after a paper has already passed the README inclusion bar.

The goal is to improve `Primary affiliation` and `GitHub` coverage without lowering precision.

## Search Order

For each accepted paper, search in this order and stop as soon as the answer is high-confidence:

1. arXiv abstract page
2. official links explicitly named in the abstract or comments
3. paper PDF first page for author affiliations
4. official project page / GitHub / Hugging Face page

Keep the search short and targeted. Do not turn metadata filling into a long research pass.

## Primary Affiliation

Fill `Primary affiliation` only when one owner is clearly dominant.

Good signals:

- a single lab or company appears across most authors
- the repo or project page clearly belongs to one organization
- the paper branding is obviously tied to one team or company

Use `-` when:

- authors come from several institutions and no clear primary owner exists
- the paper looks like a broad collaboration without a dominant lab
- the affiliation cannot be confirmed quickly from an official source

Prefer short canonical names such as:

- `Baidu Inc.`
- `Shanghai Artificial Intelligence Laboratory`
- `Allen Institute for AI`

Do not concatenate many institutions into one cell.

## GitHub Or Benchmark Link

Use the official project link only when ownership is clear.

Allowed targets:

- official GitHub repository
- official Hugging Face model/dataset page
- official project or dataset homepage when GitHub is not the canonical destination

Use `-` when:

- only third-party reproductions exist
- the code link is mentioned informally but ownership is unclear
- there are multiple candidate repos and none is clearly official

## Conflict Rules

- Prefer the paper itself over secondary websites.
- Prefer explicit ownership over popularity.
- If the metadata is still ambiguous after a short search, keep `-`.

## Optional Decision Notes

You may keep extra keys such as `metadata_sources` or `metadata_notes` in the temporary decisions JSON for your own audit trail.

The merge script ignores unknown keys.
