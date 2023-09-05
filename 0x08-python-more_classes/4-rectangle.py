#!/usr/bin/python3

"""
Create a class with private instance attributes
and methods to calculate the area and parameter
of a rectangle

                                            """


class Rectangle:
    """
    class has the instance attributes `width` and `height` that
    defines the dimentions of a rectangle
    """

    def __init__(self, width=0, height=0):
        # initailize the width and height variable for all instances

        self.width = width
        self.height = height

    @property
    def width(self):
        # making width attribute private

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        # making hight attribute private

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        """
        Print `#` when `print()` or `str()` is used to print an instance of
        this class.

        Horizontally print `width` times the character `#`
        Also print vertically, `height` times to acheive a square like
        shape based on the current `width` and `height` atrribute
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            print("#" * self.__width, end=""
                  if i == (self.__height - 1) else "\n")
        return ""  # return an empty string

    def __repr__(self):
        """
        return a string that can be used to recreate an existing instance of
        the class using `eval()` and `repr()` string methods

        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def area(self):
        # return the area of a rectangtle

        return self.__width * self.__height

    def perimeter(self):
        # return the perimeter of a rectangle

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
