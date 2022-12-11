def print_borders(s: str, k: str) -> None:
    line_length = len(s) + 2
    print(k*line_length)
    print(k, s, k, sep='')
    print(k*line_length)


if __name__ == "__main__":
    print_borders('Текст в рамке', '@')
