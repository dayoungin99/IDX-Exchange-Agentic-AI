# Week 6 — Embeddings & Vector Search

## Overview

Implemented a semantic property search system using Gemini embeddings and cosine similarity, integrated with OpenClaw.

The system retrieves active property listings from MySQL, filters listings based on user-specified criteria, and ranks cached listings by semantic similarity.

## Features

- Retrieve active property listings from MySQL (`rets_property`)
- Generate embeddings using `gemini-embedding-001`
- Cache listing embeddings to reduce repeated API calls
- Filter active listings by city and number of bedrooms
- Rank matching properties using cosine similarity
- Return up to 5 most similar listing IDs
- Integrate with OpenClaw as `semantic-property-search`

## Usage

### Build Embedding Cache

Generate embeddings for 5 active listings:

```bash
python3 embedding_search.py --build-cache 5
```

Generate embeddings for 10 active listings in San Diego:

```bash
python3 embedding_search.py --build-cache 10 "San Diego"
```

Generate embeddings for 10 active listings in San Diego with 3 bedrooms:

```bash
python3 embedding_search.py --build-cache 10 "San Diego" 3
```

### Semantic Property Search

Search using a natural-language description:

```bash
python3 embedding_search.py "3 bedroom house in San Diego"
```

The system filters cached active listings by city and bedroom count before ranking them using cosine similarity.

## Testing

Successfully generated and cached embeddings for 80 property listings.

Test query:

```text
3 bedroom house in San Diego
```

Output:

```text
Top 5 listing IDs: ['1151780870', '1151427980', '1151427981', '1152508096', '1151573979']
```

The search successfully returned 5 listing IDs after applying city and bedroom filters.

## Limitations

- Searches only active listings with cached embeddings, not the entire active listing database.
- The current cache contains 80 listings.
- Gemini API quotas limit large-scale embedding generation.
- Requires MySQL credentials and a Gemini API key configured in the local environment.
- The embedding cache currently uses a local file path and must be configured for other environments.
- Additional query constraints, such as price range and property type, are not yet implemented.

## Future Improvements

- Expand embedding coverage across active listings.
- Add additional filters, including price range and property type.
- Improve embedding cache management and scalability.
- Extend semantic search into a property recommendation engine.
