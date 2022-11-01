list_one = [
    int(input(f'Введите {idx}-е число для первого списка: ')) for idx in range(1, 4)]

list_two = [
    int(input(f'Введите {idx}-е число для второго списка: ')) for idx in range(1, 8)]

print(f'Первый список: {list_one}')
print(f'Второй список: {list_two}')

list_one += list_two
list_one = list(set(list_one))
print(f'Новый первый список с уникальными элементами: {list_one}')
