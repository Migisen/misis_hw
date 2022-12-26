from task6 import Point
from typing import Union


class Rectangle:
    def __init__(self, left_bottom: Point, right_top: Point) -> None:
        self.left_bottom = left_bottom
        self.right_top = right_top

        self.left_top = Point(left_bottom.x, right_top.y)
        self.right_bottom = Point(right_top.x, left_bottom.y)

        self.top_side_len = self.right_top.x - self.left_top.x
        self.left_side_len = self.right_top.y - self.right_bottom.y

    def calculate_perimeter(self) -> Union[int, float]:
        return 2*(self.top_side_len + self.left_side_len)

    def calculate_area(self) -> Union[int, float]:
        return self.top_side_len * self.left_side_len


if __name__ == "__main__":
    left_bottom = Point(1, 1)
    right_top = Point(4, 4)
    rectangle = Rectangle(left_bottom, right_top)
    print(f'Периметр: {rectangle.calculate_perimeter()}')
    print(f'Площадь: {rectangle.calculate_area()}')
