def skate_rent():
    n_skates = int(input('Кол-во коньков: '))
    skates = sorted([int(input(f'Размер {idx}-й пары: '))
                     for idx in range(1, n_skates + 1)], reverse=True)
    n_people = int(input('Кол-во людей: '))
    feet = sorted([int(input(f'Размер ноги {idx}-го человека: '))
                   for idx in range(1, n_people + 1)], reverse=True)
    # Нас не просят найти оптимальные наборы
    # Поэтому пойдем с конца
    fullfilled_people = 0
    for foot in feet:
        if foot <= skates[0]:
            fullfilled_people += 1
            skates.remove(skates[0])

    print(
        f'Наибольшее кол-во людей, которые могут взять ролики: {fullfilled_people}')


if __name__ == '__main__':
    skate_rent()
