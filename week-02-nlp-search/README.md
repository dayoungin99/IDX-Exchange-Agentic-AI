# Week 2: Natural Language Property Search

## Deliverable

**An OpenClaw skill that accepts a free-text query and returns a structured filter object, validated against at least 10 test queries.**

## 1. Overview

This week focuses on converting natural-language real estate queries into structured property filters that can be used with MLS property data.

For example:

```text
Show me 3-bedroom condos in Irvine under $1.5M with a pool.
```

is converted into:

```json
{
  "city": "Irvine",
  "maxPrice": 1500000,
  "beds": 3,
  "type": "Condominium",
  "pool": "True"
}
```

## 2. Supported Filters

- City
- Maximum price
- Minimum bedrooms
- Minimum bathrooms
- Minimum square feet
- Property type
- Pool
- View
- Maximum HOA

## 3. Implementation

The `property-search` OpenClaw skill uses a TypeScript parser to extract property search filters from a free-text query.

## 4. Testing

The parser was validated using 10 different natural-language property search queries.

```text
Test 1: PASS
Test 2: PASS
Test 3: PASS
Test 4: PASS
Test 5: PASS
Test 6: PASS
Test 7: PASS
Test 8: PASS
Test 9: PASS
Test 10: PASS
```

**Result: 10/10 tests passed.**
