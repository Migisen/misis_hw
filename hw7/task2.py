def sum_everything():
    temp_sum = 0
    while True:
        print('-'*5)
        user_input = input('Введите число: ')
        if user_input == '':
            return temp_sum

        try:
            int_input = float(user_input)
        except ValueError as ve:
            print('Вы ввели не число :(')
            continue

        temp_sum += int_input
        print(f'Текущая сумма: {temp_sum}')


if __name__ == "__main__":
    result = sum_everything()
    print(f'Итоговая сумма = {result}')
