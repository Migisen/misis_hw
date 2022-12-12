from typing import Optional, Tuple


class ImpossibleTimeError(Exception):
    ...


class Clock:
    """Класс для часов
    """

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        if hours < 0 or hours >= 24:
            raise ImpossibleTimeError
        self._hours = hours
        if minutes < 0 or minutes >= 60:
            raise ImpossibleTimeError
        self._minutes = minutes
        if seconds < 0 or seconds >= 60:
            raise ImpossibleTimeError
        self._seconds = seconds

    def __str__(self) -> str:
        return 'Текущее время: {:02d}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.seconds)

    @property
    def hours(self) -> int:
        return self._hours

    @hours.setter
    def hours(self, hours: int) -> None:
        """Добавление часов

        Args:
            hours (int): добавление произвольного количества часов, можно < 0
        """
        new_hours, _ = Clock.get_generic_time_delta(hours, 0, 24)
        self._hours = new_hours

    # По тз
    def add_hour(self):
        self.hours += 1

    @property
    def minutes(self) -> int:
        return self._minutes

    @minutes.setter
    def minutes(self, minutes: int) -> None:
        """Добавление минут

        Args:
            minutes (int): добавление произвольного количества минут, можно < 0
        """
        new_minutes, addtitional_hours = Clock.get_generic_time_delta(
            minutes, 0, 60)
        self.hours += addtitional_hours
        self._minutes = new_minutes

    # По тз
    def add_minute(self):
        self.minutes += 1

    @property
    def seconds(self) -> int:
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: int) -> None:
        """Добавление cекунд

        Args:
            seconds (int): добаление произвольного количеств секунд, можно < 0
        """
        new_seconds, addtitional_minutes = Clock.get_generic_time_delta(
            seconds, 0, 60)
        self.minutes += addtitional_minutes
        self._seconds = new_seconds

    # по тз
    def add_second(self):
        self.seconds += 1

    @staticmethod
    def get_generic_time_delta(new_time: int, lower_time_bound: int, upper_time_bound: int) -> Tuple[int, int]:
        assert isinstance(new_time, int) == True
        additional_parent_time = new_time // upper_time_bound
        if new_time < lower_time_bound:
            if new_time <= -upper_time_bound:
                new_time = upper_time_bound - (-new_time % upper_time_bound)
            else:
                new_time += upper_time_bound
        if new_time >= upper_time_bound:
            new_time %= upper_time_bound
        return new_time, additional_parent_time


if __name__ == "__main__":
    my_clock = Clock(17, 0, 0)
    print(my_clock)
    my_clock.minutes -= 120
    print(my_clock)
    my_clock.minutes += 210
    print(my_clock)
    my_clock.minutes -= 1111
    print(my_clock)
    my_clock.seconds += 61
    print(my_clock)
    my_clock.seconds -= 3600
    print(my_clock)

    my_clock.add_second()
    print(my_clock)

    my_clock.add_minute()
    print(my_clock)

    my_clock.add_hour()
    print(my_clock)
