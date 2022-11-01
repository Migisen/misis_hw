from typing import List


def visualise_sequence(sequence: List[int], selected_idx: int) -> str:
    result_str = ''
    for idx, number in enumerate(sequence):
        if idx != selected_idx:
            result_str += f'{number} '
        else:
            result_str += f'[ {number} ] '
    return result_str.replace('  ', ' ')


def find_min_to_symmetric(numbers_sequence: List[int], visualise: bool = True) -> None:
    print(f'Последовательность: {numbers_sequence}')

    target_shift_idx, result_shift = -1, 0
    for idx, value in enumerate(numbers_sequence):
        if visualise:
            print(5*'-')
            print(visualise_sequence(numbers_sequence, idx))
        if value != numbers_sequence[target_shift_idx]:
            if visualise:
                if idx != 0:
                    indent = '  ' * result_shift
                else:
                    indent = ' ' * result_shift
                print(indent + visualise_sequence(numbers_sequence[::-1], -target_shift_idx-1))
                print('Сдвигаем нижний ряд вправо')
            result_shift = idx + 1
            target_shift_idx = 0
        elif visualise:
            print('  '*result_shift + visualise_sequence(numbers_sequence[::-1], -target_shift_idx-1))
        target_shift_idx -= 1

    print(5*'-')
    if result_shift == 0:
        print('Число уже симметричное')
        return None

    new_numbers = numbers_sequence[:result_shift][::-1]
    print(f'Нужно приписать чисел: {len(new_numbers)}')
    print(f'Сами числа: {new_numbers}')


if __name__ == '__main__':
    n_numbers = int(input('Кол-во чисел: '))
    n_sequence = [int(input('Число: ')) for _ in range(n_numbers)]
    find_min_to_symmetric(n_sequence)
