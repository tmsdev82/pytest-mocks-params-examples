from datetime import datetime, timedelta


def get_future_date(days_in_future: int) -> datetime:
    future_date = datetime.utcnow() + timedelta(days=days_in_future)

    return future_date