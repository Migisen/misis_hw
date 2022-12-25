import operator


class IncorrectInput(Exception):
    def __init__(self, message):
        super().__init__(message)


def process_user_input(user_input: str):
    operations_mapping = {'+': operator.add,
                          '-': operator.sub,
                          '*': operator.mul,
                          '**': operator.pow,
                          '/': operator.truediv,
                          '//': operator.floordiv,
                          '%': operator.mod}
    try:
        a, operation, b = user_input.split(' ')
    except ValueError as ve:
        raise IncorrectInput(
            'Неправильный ввод, должно быть: "ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2"')
    if operation not in operations_mapping.keys():
        raise NotImplementedError('Неподдерживаемая операция')

    try:
        a = int(a)
        b = int(b)
    except ValueError as ve:
        raise IncorrectInput('Нецелые числа')

    return a, b, operations_mapping[operation]


def calculator(a, b, operation):
    try:
        result = operation(a, b)
        return result
    except Exception as e:
        print(f'Ошибка при вычислении: {str(e)}')
        raise e


if __name__ == "__main__":
    while True:
        user_input = input('Введите выражение: ')
        if user_input == '':
            break
        try:
            a, b, operation = process_user_input(user_input)
        except Exception as e:
            print(f'Ошибка в обработке ввода: {str(e)}')
            continue
        try:
            result = calculator(a, b, operation)
            print(f'Результат = {result}')
        except Exception:
            print('Попробуйте снова')
            continue
