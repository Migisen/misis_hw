from datetime import date, timedelta
from typing import Iterator, List


def is_date_magical(target_date: date) -> bool:
    if target_date.day * target_date.month == target_date.year % 100:
        return True
    else:
        return False


def generate_dates(start_date, stop_date) -> Iterator[date]:
    days_between = stop_date - start_date
    for shift in range(days_between.days + 1):
        day = start_date + timedelta(days=shift)
        yield day


def find_magical_dates(start_date, stop_date) -> List[date]:
    magical_dates = []
    for date_n in generate_dates(start_date, stop_date):
        if is_date_magical(date_n):
            magical_dates.append(date_n)
    return magical_dates


if __name__ == "__main__":
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    magical_dates = find_magical_dates(start_date, end_date)
    print(magical_dates)
