---
name: market-statistics
description: Answer California real estate market questions using historical sales data and active property listings.
---

# Market Statistics Agent

Use this skill when a user asks about California real estate market statistics or trends.

## Data Sources

- `california_sold`: Historical property sales data
- `rets_property`: Active property listings

## Core Metrics

- Average and median close price by city, ZIP code, and property type
- Average price per square foot
- Price per square foot trends over time
- List-to-close price ratio
- Average days on market (DOM)
- Active inventory versus sold volume
- Month-over-month and year-over-year trends

## Example Questions

- Is now a good time to buy in San Diego?
- What is the average price per square foot in Pasadena?
- What is the median home price in Irvine?

## Instructions

1. Identify the city or location in the user's question.
2. Retrieve relevant statistics from the database.
3. Calculate the requested market metrics and trends.
4. Summarize the results using actual data.
5. Explain market trends clearly without inventing statistics.

## Expected Output

Provide a data-backed market summary including:

- Median home price
- Average days on market
- List-to-close price ratio
- 12-month market trend

Only report metrics supported by the available data.

## Execution

When a user asks about California real estate market statistics:

1. Identify the California city mentioned in the question.
2. Run the market statistics script:

   ~/Desktop/26Fall/IDXExchange-Internship/ai-agentic-engineer/submission/week-05-market-statistics-agent/.venv/bin/python ~/.openclaw/workspace/skills/market-statistics/scripts/run_market_stats.py "CITY"

   Replace CITY with the requested city.

3. Read the JSON output from the script.
4. Summarize the results using the available metrics:
   - Median close price
   - Average close price
   - Average price per square foot
   - Average days on market (DOM)
   - List-to-close price ratio
   - Active inventory versus sold volume
   - Month-over-month and year-over-year price trends
5. Explain what the data suggests about the local market.
6. If data is missing, clearly state that it is unavailable.

Do not invent statistics or make unsupported market predictions.
