from task7 import Rectangle
from task6 import Point


class RectangleContains(Rectangle):
    def contains(self, point: Point) -> bool:
        inside_x_boundaries = point.x > self.left_top.x and point.x < self.right_top.x
        inside_y_boundaries = point.y > self.left_bottom.y and point.y < self.left_top.y

        if inside_x_boundaries and inside_y_boundaries:
            return True
        else:
            return False


if __name__ == "__main__":
    left_bottom = Point(1, 1)
    right_top = Point(4, 4)
    rectangle = RectangleContains(left_bottom, right_top)
    print(rectangle.contains(Point(2, 3)))
    print(rectangle.contains(Point(10, 10)))
