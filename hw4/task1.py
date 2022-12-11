from typing import List
from functools import reduce
import math


def calculate_pair_nod(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def calculate_nod(numbers: List[int]) -> int:
    result = numbers[0]
    for number in numbers[1:]:
        result = calculate_pair_nod(result, number)
    return result


def calculate_nok(numbers: List[int]) -> int:
    nok = 1
    for number in numbers:
        nok = (nok * number) // calculate_pair_nod(nok, number)
    return nok


if __name__ == '__main__':
    test_numbers = [36, 48, 2, 124, 12, 2]
    assert math.gcd(*test_numbers) == calculate_nod(test_numbers)
    assert math.lcm(*test_numbers) == calculate_nok(test_numbers)
