---
name: property-search
description: Search real estate listings through natural language conversations, ask follow-up questions, refine filters, and return formatted property cards.
---

# Property Search

Use this skill when a user wants to search for real estate properties.

## Conversational Property Search

1. Identify the user using a consistent user ID.
2. Process the user's message using `{baseDir}/scripts/conversational_search.ts`.
3. Maintain the user's search filters across messages using `{baseDir}/scripts/session.ts`.
4. If the search requires additional information, return the follow-up question.
5. When enough information is available, search active MLS listings.
6. Return the formatted property cards to the user.

## Supporting Scripts

- `{baseDir}/scripts/parse_property_query.ts` — Extract search filters from natural language.
- `{baseDir}/scripts/refine_query.ts` — Update existing search filters.
- `{baseDir}/scripts/follow_up.ts` — Generate follow-up questions.
- `{baseDir}/scripts/session.ts` — Manage user sessions.
- `{baseDir}/scripts/active_listings.ts` — Query active MLS listings.
- `{baseDir}/scripts/format_property_cards.ts` — Format search results.

## Execution

Run the conversational property search using the CLI entry point:

```bash
node --env-file="$HOME/.openclaw/.env" \
--import "$HOME/Desktop/26Fall/IDXExchange-Internship/ai-agentic-engineer/openclaw/node_modules/tsx/dist/loader.mjs" \
{baseDir}/scripts/run_conversation.ts "<userId>" '<userMessage>'
```

- Replace `<userId>` with a consistent identifier for the user.
- Replace `<userMessage>` with the user's latest message.
- Use the same user ID across messages to preserve search filters.
- Return the CLI output directly to the user.
- Do not call the Gemini API from the property-search scripts.
