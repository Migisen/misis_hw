def counting_rhyme(n_people: int, terminate_number: int):
    people = list(range(1, n_people + 1))
    start_idx = 0
    while len(people) > 1:
        print('-'*5)
        print(f'Текущий круг людей: {people}')
        print(f'Начало счёта с номера {people[start_idx]}')
        start_idx += terminate_number
        start_idx %= len(people)
        start_idx -= 1
        print(f'Выбывает человек под номером {people[start_idx]}')
        del people[start_idx]
        if start_idx < 0:
            start_idx = 0
    print(f'Остался человек под номером {people[0]}')


if __name__ == '__main__':
    n_people = int(input('Кол-во человек: '))
    lucky_number = int(input('Какое число в считалке?: '))
    print(f'Значит выбывает каждый {lucky_number}-й человек')
    counting_rhyme(n_people, lucky_number)
