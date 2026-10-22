import json
import sys
from pathlib import Path
from median_price import get_median_price
from inventory_comparison import get_inventory_comparison
from yearly_trends import get_year_over_year_trend

import pandas as pd
from sqlalchemy import create_engine, text

from price_trend import get_price_trend, engine


def get_market_summary(city: str):
    sql_file = Path(__file__).with_name("city_market_summary.sql")
    sql = sql_file.read_text()

    with engine.connect() as connection:
        df = pd.read_sql(text(sql), connection)

    city_data = df[df["City"].str.lower() == city.lower()]

    if city_data.empty:
        return None

    return city_data.iloc[0].to_dict()


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Please provide a city."}))
        return

    city = sys.argv[1]

    summary = get_market_summary(city)
    median_price = get_median_price(city)
    inventory = get_inventory_comparison(city)
    yearly_trend = get_year_over_year_trend(city)
    trends = get_price_trend(city, months=12)

    result = {
        "city": city,
        "market_summary": summary,
        "median_price": median_price,
        "inventory_comparison": inventory,
        "year_over_year_trend": yearly_trend,
        "monthly_trends": trends.to_dict(orient="records"),
    }

    print(json.dumps(result, default=str))


if __name__ == "__main__":
    main()
