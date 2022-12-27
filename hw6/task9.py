class CounterBelowZeroError(Exception):
    ...


class DecimalCounter:
    def __init__(self) -> None:
        self._count = 0

    def get_counter(self) -> int:
        return self._count

    def increment(self) -> None:
        self._count += 1

    def decrement(self) -> None:
        if self._count == 0:
            raise CounterBelowZeroError()
        self._count -= 1


if __name__ == "__main__":
    decimal_counter = DecimalCounter()
    decimal_counter.increment()
    decimal_counter.increment()
    print(decimal_counter.get_counter())
    decimal_counter.decrement()
    decimal_counter.decrement()
    print(decimal_counter.get_counter())
    try:
        decimal_counter.decrement()
    except CounterBelowZeroError as cbze:
        print(':(')
