import pathlib
import re


def read_data(file: str):
    with open(file, 'r') as f:
        return f.read()


def write_data(file: str, data):
    with open(file, 'w') as f:
        f.write(data)


if __name__ == "__main__":
    resource_path = pathlib.Path(
        __file__).parent.resolve() / 'resources'
    numbers_path = resource_path / 'numbers.txt'
    answer_path = resource_path / 'answer.txt'
    data = read_data(numbers_path)

    regex = re.compile(r'\d+')
    numbers = [int(number) for number in regex.findall(data)]
    result = sum(numbers)
    print(f'Сумма = {result}')

    write_data(answer_path, str(result))
