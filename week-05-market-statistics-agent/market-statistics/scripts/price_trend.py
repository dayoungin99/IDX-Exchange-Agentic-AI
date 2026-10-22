import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

import os
from pathlib import Path
from urllib.parse import quote_plus

env_path = Path.home() / ".openclaw" / ".env"

if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)

        if key in {"MYSQL_HOST", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"}:
            os.environ.setdefault(key, value.strip().strip('"').strip("'"))

engine = create_engine(
    "mysql+mysqlconnector://"
    f"{quote_plus(os.environ['MYSQL_USER'])}:"
    f"{quote_plus(os.environ['MYSQL_PASSWORD'])}@"
    f"{os.environ['MYSQL_HOST']}/"
    f"{os.environ['MYSQL_DATABASE']}"
)

def get_price_trend(city: str, months: int = 24):
    query = """
      SELECT
        DATE_FORMAT(CloseDate, "%Y-%m") AS month,
        COUNT(*) AS sales,
        ROUND(AVG(ClosePrice), 0) AS avg_price,
        ROUND(AVG(DaysOnMarket), 1) AS avg_dom
      FROM california_sold
      WHERE City = %s
        AND PropertyType = "Residential"
        AND CloseDate >= DATE_SUB(CURDATE(), INTERVAL %s MONTH)
      GROUP BY DATE_FORMAT(CloseDate, "%Y-%m")
      ORDER BY month
    """
    df = pd.read_sql(query, engine, params=(city, months))
    df["price_change_pct"] = df["avg_price"].pct_change() * 100
    return df
