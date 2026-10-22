from sqlalchemy import text
from price_trend import engine


def get_inventory_comparison(city: str):
    active_sql = """
        SELECT COUNT(*) AS active_count
        FROM rets_property
        WHERE L_City = :city
          AND StandardStatus = 'Active'
    """

    sold_sql = """
        SELECT COUNT(*) AS sold_count
        FROM california_sold
        WHERE City = :city
          AND PropertyType = 'Residential'
          AND CloseDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
    """

    with engine.connect() as connection:
        active_count = connection.execute(
            text(active_sql), {"city": city}
        ).scalar()

        sold_count = connection.execute(
            text(sold_sql), {"city": city}
        ).scalar()

    return {
        "active_inventory": int(active_count or 0),
        "sold_volume_12_months": int(sold_count or 0),
    }
