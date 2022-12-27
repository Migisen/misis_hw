from typing import Union


def group_by_sign(*args: Union[int, float]):
    negative_numbers, positive_numbers = [], []
    for number in args:
        if number < 0:
            negative_numbers.append(number)
        else:
            positive_numbers.append(number)
    return sorted(negative_numbers, reverse=True), sorted(positive_numbers)


if __name__ == "__main__":
    result = group_by_sign(1, 3, 5, 6, 7, 8, -1, -4, -100, 0)
    print(result)
