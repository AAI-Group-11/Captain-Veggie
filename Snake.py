# Author: Divyang, Gurbeer, Prabal
# Date: 21st November, 2023
# Description: This program defines a class named Snake, which represents the snake on the field.

from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y):
        """Constructor for the Snake class

        :param x: x coordinate of snake
        :type x: int
        :param y: y coordinate of snake
        :type y: int
        """
        super().__init__(x, y, "S")
