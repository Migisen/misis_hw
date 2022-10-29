from typing import List


class PartyHouse:
    def __init__(self, max_guesets: int, initial_guests: List[str]) -> None:
        self.max_guests = max_guesets
        if len(initial_guests) > max_guesets:
            raise Exception('Гостей слишком много, вечеринки не будет')
        else:
            self._current_guests = initial_guests

    @property
    def current_guests(self):
        print(
            f'Сейчас на вечеринке {len(self._current_guests)} человек: {self._current_guests}')
        return self._current_guests

    @current_guests.setter
    def current_guests(self, new_guest: str):
        if len(self._current_guests) < 6:
            print(f'Привет, {new_guest}!')
            self._current_guests.append(new_guest)
        else:
            print(f'Прости, {new_guest}, но мест нет.')

    def remove_guest(self, guest_name: str) -> None:
        if guest_name not in self._current_guests:
            print('У нас нет такого гостя :(')
        else:
            self._current_guests.remove(guest_name)
            print(f'Пока, {guest_name}!')

    def run_party(self, stop_word: str):
        while True:
            print('-'*5)
            self.current_guests
            action = input('Гость пришёл или ушёл?: ')
            while action not in ['пришёл', 'ушёл', stop_word]:
                action = input('Не расслышал, повтори: ')
            if action == stop_word:
                print('Вечеринка закончилась, все легли спать.')
                break
            guest_name = input('Имя гостя: ')
            if action == 'пришёл':
                self.current_guests = guest_name
            else:
                self.remove_guest(guest_name)


if __name__ == '__main__':
    MAX_GUESTS = 6
    STOP_WORD = 'Пора спать'
    INITIAL_GUESTS = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

    party_house = PartyHouse(max_guesets=MAX_GUESTS,
                             initial_guests=INITIAL_GUESTS)
    party_house.run_party(stop_word=STOP_WORD)
