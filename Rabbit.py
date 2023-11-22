# Author: Divyang, Gurbeer, Prabal
# Date: 21st November, 2023
# Description: This program defines a class named Rabbit, which represents a rabbit on the field.

from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        """Constructor for the Rabbit class

        :param x: x coordinate of rabbit
        :type x: int
        :param y: y coordinate of rabbit
        :type y: int
        """
        super().__init__(x, y, "R")
