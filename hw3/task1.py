def count_and_remove(target_list: list, number: int, delete_value: bool = True) -> None:
    counter = 0
    for element in target_list:
        if element == number:
            counter += 1
            if delete_value:
                target_list.remove(element)
    print(f'Кол-во цифр {number} при первом объединении: {counter}')


def task_1(list_main, list_a, list_b) -> None:
    # Делаем inplace, так как нельзя создавать новые списки | Это не список
    for additional_list, number, delete_flag in ((list_a, 5, True), (list_b, 3, False)):
        list_main += additional_list
        count_and_remove(list_main, number, delete_flag)


if __name__ == '__main__':
    main = [1, 5, 3]
    a, b = [1, 5, 1, 5], [1, 3, 1, 5, 3, 3]
    task_1(main, a, b)
    print(f'Сам список в конце: {main}')
