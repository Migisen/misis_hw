from typing import List


def task_2(class_1: List[int], class_2: List[int]) -> List[int]:
    result_queue = class_1 + class_2
    sorted_queue = sorted(result_queue)
    return sorted_queue


if __name__ == '__main__':
    # Не очень понял, что значит списки роста :(
    class_1 = list(range(160, 177, 2))
    class_2 = list(range(162, 181, 3))
    result_queue = task_2(class_1, class_2)
    print(f'Отсортированный список учеников: {result_queue}')
