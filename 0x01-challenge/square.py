#!/usr/bin/python3
"""Defining a square object."""


class Square():
    """Representation of a square."""

    width = 0
    height = 0

    def __init__(self, **kwargs):
        """Initialising a square object."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.height

    def perimeter_o_my_square(self):
        """Returns the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
