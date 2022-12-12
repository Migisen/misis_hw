from task10 import Clock


class AdvancedClock(Clock):
    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds


if __name__ == "__main__":
    clock_1 = AdvancedClock(13, 37, 42)
    clock_2 = AdvancedClock(12, 12, 12)
    clock_1 + clock_2
    print(clock_1)
