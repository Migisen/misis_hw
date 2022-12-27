# так как дз на рекурссии
# то бинарное решение не будем использовать
def is_power_two(number: int) -> bool:
    number = number / 2
    if number == 2:
        return True
    elif number > 2:
        return is_power_two(number)
    else:
        return False


if __name__ == "__main__":
    if is_power_two(2048):
        print('YES')
    else:
        print('NO')
