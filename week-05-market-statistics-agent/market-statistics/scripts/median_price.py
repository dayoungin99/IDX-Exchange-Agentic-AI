from sqlalchemy import text
from price_trend import engine


def get_median_price(city: str):
    sql = """
        SELECT AVG(ClosePrice) AS median_price
        FROM (
            SELECT
                ClosePrice,
                ROW_NUMBER() OVER (ORDER BY ClosePrice) AS row_num,
                COUNT(*) OVER () AS total_count
            FROM california_sold
            WHERE City = :city
              AND PropertyType = 'Residential'
              AND CloseDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
              AND ClosePrice > 0
        ) AS ranked
        WHERE row_num IN (
            FLOOR((total_count + 1) / 2),
            FLOOR((total_count + 2) / 2)
        )
    """

    with engine.connect() as connection:
        result = connection.execute(text(sql), {"city": city})
        median_price = result.scalar()

    return float(median_price) if median_price is not None else None
