import random


class OutOfFoodError(Exception):
    ...


class Grass:
    def __init__(self, max_nutrition: int) -> None:
        self.nutrition = random.sample(range(1, max_nutrition+1), 1)[0]


class Herbivore:
    def __init__(self, max_fullness: int, hunger_threshold: float, max_hunger_per_tick: int) -> None:
        self._fullness = random.sample(range(max_fullness+1), 1)[0]
        self._max_fullness = max_fullness + 1
        self._hunger_threshold = hunger_threshold * (max_fullness + 1)
        self._max_hunger_per_tick = max_hunger_per_tick

    def __str__(self) -> str:
        return f' ? Состояние животного: \n ? Сытость: {self.fullness}'

    @property
    def fullness(self) -> int:
        return self._fullness

    def change_fullness(self, nutrition: int):
        self._fullness += nutrition
        if self._fullness > self._max_fullness:
            self._fullness = self._max_fullness

    def eat(self, grass: Grass) -> True:
        # Проверка на голод
        if self.fullness > self._hunger_threshold:
            print(' ~ Животное не голодное')
            return False
        print(f' + Животное поело и получило {grass.nutrition} ед. насыщения')
        self.change_fullness(grass.nutrition)
        return True

    def add_hunger(self):
        hunger = -random.sample(range(self._max_hunger_per_tick), 1)[0]
        print(f' - Проголодалось на {hunger} ед')
        self.change_fullness(hunger)
        if self.fullness < 0:
            raise OutOfFoodError


if __name__ == "__main__":
    # Небольшая сисуляция
    MAX_FULLNESS = 20
    HUNGER_THRESHOLD = 0.3
    MAX_HUNGER_PER_TICK = 5
    animal = Herbivore(MAX_FULLNESS, HUNGER_THRESHOLD, MAX_HUNGER_PER_TICK)

    MAX_GRASS = 3
    grass = [Grass(3) for _ in range(MAX_GRASS)]
    while True:
        print('---')
        print(animal)
        if len(grass) != 0:
            if animal.eat(grass[0]):
                del grass[0]
        else:
            print(' ? Травы больше нет (')
        try:
            animal.add_hunger()
            print(animal)
        except OutOfFoodError:
            print(' x(')
            break
