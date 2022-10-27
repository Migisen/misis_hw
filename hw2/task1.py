def task_1(team_name: str) -> None:
    print(f'{team_name} - чемпион!')
    team_name = team_name.lower()
    print(len(team_name)*'-')
    print(f'Длинна наименования команды = {len(team_name)}')
    if 'п' in team_name: # Можно еще через str.find(), но это медленнее
        print(f'Буква "п" есть, {True}')
    else:
        print(f'Буквы "п" нет :(, {False}')
    
    print(f'Буква "а" повторяется {team_name.count("а")} раз[а]')


if __name__ == '__main__':
    task_1(input('Введите название команды\n'))
