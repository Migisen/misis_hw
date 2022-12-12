from task2 import AdvancedMan


class GreetMan(AdvancedMan):
    def greet(self) -> None:
        print(
            f'Привет! Меня зовут {self.last_name} {self.first_name}, мне {self.age} лет')


if __name__ == "__main__":
    test_greet_man = GreetMan('Ivan', 'Ivanov', 12)
    test_greet_man.greet()
