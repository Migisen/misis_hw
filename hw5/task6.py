def invert_number(number: int, inverted_number: int = 0) -> int:
    if number == 0:
        return inverted_number
    return invert_number(number // 10, 10 * inverted_number + number % 10)


if __name__ == "__main__":
    print(invert_number(123))
