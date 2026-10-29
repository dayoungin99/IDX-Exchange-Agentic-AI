import os
import re
import json
import time
from pathlib import Path
from google import genai
import numpy as np
import mysql.connector
from sklearn.metrics.pairwise import cosine_similarity

env_path = Path.home() / ".openclaw" / ".env"

for line in env_path.read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        key, value = line.split("=", 1)
        if key in {"GEMINI_API_KEY", "MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"}:
            os.environ[key] = value.strip().strip('"').strip("'")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
CACHE_PATH = Path.home() / (
    "Desktop/26Fall/IDXExchange-Internship/"
    "ai-agentic-engineer/submission/"
    "week-06-embedding-vector-search/embedding_cache.json"
)

def load_embedding_cache() -> dict:
    if CACHE_PATH.exists():
        with open(CACHE_PATH, "r") as f:
            return json.load(f)

    return {}

def save_embedding_cache(cache: dict) -> None:
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f)

def get_embedding(text: str) -> list[float]:
    text = text.replace("\n", " ").strip()[:8000]

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )

    return response.embeddings[0].values


# Build embedding for a listing (combine key fields)
def build_listing_embedding(row: dict, cache: dict) -> list[float]:
    listing_id = str(row["L_ListingID"])

    # Reuse an existing embedding
    if listing_id in cache:
        return cache[listing_id]

    text = f"""
{row["L_Type_"]} in {row["L_City"]}, CA.
{row["L_Keyword2"]} beds, {row["LM_Dec_3"]} baths.
{row["LM_Int2_3"]} sq ft. Built {row["YearBuilt"]}.
Price: ${row["L_SystemPrice"]:,}.
{row.get("L_Remarks", "")}
""".strip()

    embedding = get_embedding(text)

    cache[listing_id] = embedding
    save_embedding_cache(cache)

    return embedding

def filter_listings_by_query(query: str, listings: list[dict]) -> list[dict]:
    """Filter listings by explicitly requested city and bedroom count."""

    query_lower = query.lower()

    # Extract bedroom count (e.g., "3 bedroom", "3 bed")
    bedroom_match = re.search(r"\b(\d+)\s*(?:bedrooms?|beds?|br)\b", query_lower)

    # Match city names from the actual listing data
    cities = {
        str(row["L_City"]).strip()
        for row in listings
        if row.get("L_City")
    }

    matched_cities = [
        city for city in cities
        if re.search(rf"\b{re.escape(city.lower())}\b", query_lower)
    ]

    # Prefer the longest match to avoid overlapping city names
    city = max(matched_cities, key=len) if matched_cities else None

    filtered = listings

    if city:
        filtered = [
            row for row in filtered
            if str(row["L_City"]).strip().lower() == city.lower()
        ]

    if bedroom_match:
        bedrooms = int(bedroom_match.group(1))

        filtered = [
            row for row in filtered
            if row.get("L_Keyword2") is not None
            and float(row["L_Keyword2"]) == bedrooms
        ]

    return filtered

def find_similar_listings(
    query: str,
    listing_embeddings: list[tuple[str, list[float]]],
    top_k: int = 5
) -> list[str]:
    """Return the top_k most similar listing IDs."""

    if not listing_embeddings:
        return []

    query_vec = np.array(get_embedding(query)).reshape(1, -1)

    listing_ids = [listing_id for listing_id, _ in listing_embeddings]
    embedding_matrix = np.array(
        [embedding for _, embedding in listing_embeddings]
    )

    similarities = cosine_similarity(
        query_vec, embedding_matrix
    )[0]

    top_indices = np.argsort(similarities)[::-1][:top_k]

    return [listing_ids[i] for i in top_indices]

def build_embedding_cache(
    limit: int = 5,
    city: str | None = None,
    bedrooms: int | None = None
) -> None:
    """Cache embeddings for active listings, optionally filtered by city."""
    cache = load_embedding_cache()
    listings = get_active_listings()

    if city:
        listings = [
            row for row in listings
            if str(row.get("L_City") or "").strip().lower() == city.lower()
        ]

    if bedrooms is not None:
        listings = [
            row for row in listings
            if row.get("L_Keyword2") is not None
            and float(row["L_Keyword2"]) == bedrooms
        ]
        
    new_count = 0

    for row in listings:
        listing_id = str(row["L_ListingID"])

        if listing_id in cache:
            continue

        try:
            build_listing_embedding(row, cache)
            new_count += 1
        except Exception as e:
            print(f"Stopped after {new_count} new embeddings: {e}")
            break

        if new_count >= limit:
            break

    print(f"Added {new_count} embeddings to cache.")
    print(f"Total cached listings: {len(cache)}")
    
def get_active_listings():
    conn = mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"],
    )

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            L_ListingID,
            L_Type_,
            L_City,
            L_Keyword2,
            LM_Dec_3,
            LM_Int2_3,
            YearBuilt,
            L_SystemPrice,
            L_Remarks
        FROM rets_property
        WHERE L_Status = 'Active'
    """)

    listings = cursor.fetchall()

    cursor.close()
    conn.close()

    return listings

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python embedding_search.py '<description>'")
        print("   or: python embedding_search.py --build-cache 5")
        sys.exit(1)

    if sys.argv[1] == "--build-cache":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5

        if limit <= 0:
            print("Limit must be a positive integer.")
            sys.exit(1)

        city = sys.argv[3] if len(sys.argv) > 3 else None
        bedrooms = int(sys.argv[4]) if len(sys.argv) > 4 else None

        build_embedding_cache(limit=limit, city=city, bedrooms=bedrooms)
        sys.exit(0)

    query = sys.argv[1]
    cache = load_embedding_cache()

    # Only search listings that are currently Active.
    active_listings = get_active_listings()

    filtered_listings = filter_listings_by_query(query, active_listings)

    active_ids = {str(row["L_ListingID"]) for row in filtered_listings}

    listing_embeddings = [
        (listing_id, embedding)
        for listing_id, embedding in cache.items()
        if listing_id in active_ids
    ]

    if not listing_embeddings:
        print("No cached active listings. Build the cache first.")
        sys.exit(0)

    results = find_similar_listings(query, listing_embeddings)
    print("Top 5 listing IDs:", results)
