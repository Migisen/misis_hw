class Man:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


if __name__ == "__main__":
    test_man = Man('Ivan', 'Ivanov', 10)
    print(test_man.first_name, test_man.last_name, test_man.age)
