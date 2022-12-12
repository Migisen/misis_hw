from typing import Union


def convert_any_to_decimal(number: str, base: int) -> int:
    return int(number, base=base)


def convert_decimal_to_any(number: int, base: int) -> str:
    existing_solutions = {2: bin,
                          8: oct,
                          16: hex}
    if base in existing_solutions.keys():
        # Вернет с перфиксом, можно его убрать, если нужно
        return existing_solutions[base](number)
    result_number = ''
    while number > 0:
        digit = int(number % base)
        if digit < 10:
            # Если цифра внутри десяти цифр
            result_number += str(digit)
        else:
            result_number += chr(ord('A')+digit-10)
        number //= base
    return result_number[::-1]


def convert_number_system(initial_base: int, target_base: int, number: Union[int, str]):
    # Првоеряем поддерживаем ли мы эту систему
    for system in (initial_base, target_base):
        if system < 2 or system > 16:
            raise NotImplementedError('Данное основание не поддерживается')
    # Если ничего не надо конвертировать
    if target_base == initial_base:
        return number
    # Проверяем, что все, кроме десятичных передается как строка
    if initial_base != 10 and isinstance(number, int):
        raise Exception('Число в не десятичной системе должно быть строкой')

    # Конвертируем в десятичное число
    if isinstance(number, str):
        decimal_representation = convert_any_to_decimal(number, initial_base)
    else:
        decimal_representation = number

    # Конвертируем в целевую систему
    result_number = convert_decimal_to_any(decimal_representation, target_base)

    print(f'{number}_({initial_base}) = {result_number}_({target_base})')

    return result_number


if __name__ == "__main__":
    convert_number_system(10, 13, 121)
