def move(n: int, x: str, y: str, z: str) -> None:
    """Перекладывание дисков пирамиды со стержня под номером x
    на стержень под номером y

    Args:
        n (int): высота пирамиды
        x (str): изначальный стержень
        y (str): стержень на который перекладывают диск
        z (str): "дополнительный стержень"
    """
    rod_mapping = {'A': 1,
                   'B': 2,
                   'C': 3}
    if n == 1:
        print(f'1 {rod_mapping[x]} {rod_mapping[y]}')
        return
    move(n-1, x, z, y)
    print(f'{n} {rod_mapping[x]} {rod_mapping[y]}')
    move(n-1, z, y, x)


if __name__ == "__main__":
    N = 3
    move(N, 'A', 'C', 'B')
