def task_2(country: str, capital: str) -> None:
    print(f'Государство - {country}, столица - {capital}')


if __name__ == '__main__':
    country, capital = input(
        "Запраишваю государство\n"), input("Запраишваю столицу\n")
    task_2(country, capital)
