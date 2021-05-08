import math
import copy


class Rectangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("Side A of the rectangle must be greater than 0")
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("Side B of the rectangle must be greater than 0")
        self.__b = value

    def get_perimeter(self):
        return (self.__a + self.__b) * 2

    def get_area(self):
        return self.__a * self.__b

    def is_equal(self, r2):
        return self.__a == r2.__a and self.__b == r2.__b

    def get_rectangle(self):
        return "The resulting rectangle: \nA: {} \t B: {}".format(self.__a, self.__b)


if __name__ == '__main__':
    r1 = Rectangle(2, 4)
    r2 = copy.deepcopy(r1)
    r3 = Rectangle(3, 6)

    print(r1)
    print(r2)
    print(r3)

    print("Perimeter of the first rectangle = ", r1.get_perimeter(), "Area of the first rectangle = ", r1.get_area())
    print("Perimeter of the second rectangle = ", r3.get_perimeter(), "Area of the second rectangle = ", r3.get_area())

    if r1.is_equal(r3):
        print("First rectangle is equal to second rectangle")
    else:
        print("First rectangle is not equal to second rectangle")
