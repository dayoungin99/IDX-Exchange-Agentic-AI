---
name: semantic-property-search
description: Find the top 5 most semantically similar active California real estate listings using Gemini embeddings and cosine similarity.
---

# Semantic Property Search

Use this skill when a user describes the type of California property they want to find in natural language.

## Instructions

1. Identify the user's free-text property description.
2. Retrieve active listings from the `rets_property` table.
3. Filter listings by city and bedroom count when specified.
4. Generate a Gemini embedding for the user's query.
5. Rank matching cached listings using cosine similarity and return up to 5 listing IDs.

## Requirements

- Only include listings where `L_Status = 'Active'`.
- Use embedding cosine similarity, not keyword matching.
- Do not invent listing IDs or property information.
- If the search cannot be completed, explain the limitation.
- Search only active listings with cached embeddings; do not claim full database coverage.

## Execution

The search implementation is located at:
`~/.openclaw/workspace/skills/semantic-property-search/scripts/embedding_search.py`

The script provides:
- `get_active_listings()` to retrieve active properties.
- `build_listing_embedding()` to generate listing embeddings.
- `find_similar_listings()` to rank listings by cosine similarity.

The script currently requires listing embeddings to be prepared before searching.
Do not claim that a search was completed unless the Python functions were actually executed.

### Run the Search

Execute the following command, replacing `<property description>` with the user's request:

```bash
~/Desktop/26Fall/IDXExchange-Internship/ai-agentic-engineer/submission/week-06-embedding-vector-search/.venv/bin/python ~/.openclaw/workspace/skills/semantic-property-search/scripts/embedding_search.py "<property description>"
```