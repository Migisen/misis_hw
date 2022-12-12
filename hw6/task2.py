from task1 import Man


class AdvancedMan(Man):
    def __str__(self) -> str:
        return f'Имя: {self.first_name}, Фамилия: {self.last_name}, Возраст: {self.age}'


if __name__ == "__main__":
    test_advanced_man = AdvancedMan('Ivan', 'Ivanov', 10)
    print(test_advanced_man)
