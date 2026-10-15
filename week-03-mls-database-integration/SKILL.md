---
name: property-search
description: Search real estate listings using natural language queries and return formatted property cards.
---

# Property Search

Use this skill when the user provides a natural language real estate search query.

1. Parse the user's query using `{baseDir}/scripts/parse_property_query.ts`.
2. Search active listings using `{baseDir}/scripts/search_properties.ts`.
3. Format the results using `{baseDir}/scripts/format_property_cards.ts`.
4. Return the formatted property cards to the user.
