from sqlalchemy import text
from price_trend import engine


def get_year_over_year_trend(city: str):
    sql = """
        SELECT
            CASE
                WHEN CloseDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
                    THEN 'current_12_months'
                ELSE 'previous_12_months'
            END AS period,
            COUNT(*) AS sales,
            ROUND(AVG(ClosePrice), 0) AS avg_price,
            ROUND(AVG(DaysOnMarket), 1) AS avg_dom
        FROM california_sold
        WHERE City = :city
          AND PropertyType = 'Residential'
          AND CloseDate >= DATE_SUB(CURDATE(), INTERVAL 24 MONTH)
          AND CloseDate <= CURDATE()
        GROUP BY period
    """

    with engine.connect() as connection:
        rows = connection.execute(text(sql), {"city": city}).mappings().all()

    periods = {row["period"]: dict(row) for row in rows}

    current = periods.get("current_12_months")
    previous = periods.get("previous_12_months")

    price_change_pct = None

    if current and previous and previous["avg_price"]:
        price_change_pct = (
            (float(current["avg_price"]) - float(previous["avg_price"]))
            / float(previous["avg_price"])
            * 100
        )

    return {
        "current_12_months": current,
        "previous_12_months": previous,
        "year_over_year_price_change_pct": price_change_pct,
    }

