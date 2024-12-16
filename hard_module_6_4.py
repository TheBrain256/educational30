from math import pi, sqrt

class Figure:

    sides_count = 0
    __sides = []
    __color = []
    filled = True

    def __init__(self, rgb, *sides):
        self.color = list(rgb)
        self.__sides = sides

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g ,b):
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if i > 0:
                if len(new_sides) == self.sides_count:
                    return True
                else:
                    return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        for j in new_sides:
            if j != self.__is_valid_sides(j):
                self.__sides = list(new_sides)
                return self.__sides


class Circle(Figure):

    sides_count = 1
    __radius = None

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self):
        s = (self.__radius ** 2) * pi
        return s


class Triangle(Figure):

    sides_count = 3
    __height = None

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) *
                                  (p - self.sides[2]))) / self.sides[0]

    def get_square(self):
        a = (self.__height * self.sides[0]) / 2
        return a


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.sides_count
        print(self.__sides)

    def get_volume(self):
        b = self.__sides[0] ** 3
        return b


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
