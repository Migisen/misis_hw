import pathlib
import operator


class IncorrectInputError(Exception):
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
        raise IncorrectInputError(
            'Неправильный ввод, должно быть: "ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2"')
    if operation not in operations_mapping.keys():
        raise NotImplementedError('Неподдерживаемая операция')

    try:
        a = int(a)
        b = int(b)
    except ValueError as ve:
        raise IncorrectInputError('Нецелые числа')

    return a, b, operations_mapping[operation]


def calculator(a, b, operation):
    try:
        result = operation(a, b)
        return result
    except Exception as e:
        print(f'Ошибка при вычислении: {str(e)}')
        raise e


def read_data(file: str):
    with open(file, 'r') as f:
        return f.readlines()


def calculate_from_file(file_path):
    requiered_calculations = read_data(file_path)
    result_sum = 0
    for line_num, expression in enumerate(requiered_calculations):
        try:
            a, b, operation = process_user_input(expression)
        except IncorrectInputError as iie:
            print(
                f'Ошибка ({str(iie)}) на строчке {line_num + 1}: {expression}')
            continue
        try:
            answer = calculator(a, b, operation)
            expression_print = expression.strip("\n")
            result_sum += answer
            print(f'{expression_print} = {answer}')
        except Exception as e:
            print(
                f'Не смогли вычислить выражение ({str(e)}) на строчке {line_num + 1}: {expression}')
    print(f'Сумма результатов = {result_sum}')


if __name__ == "__main__":
    path_to_file = pathlib.Path(
        __file__).parent.resolve() / 'resources' / 'calc_nums.txt'
    calculate_from_file(path_to_file)
