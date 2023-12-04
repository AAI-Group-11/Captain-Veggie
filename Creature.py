# Author: Divyang, Gurbeer, Prabal
# Date: 21st November, 2023
# Description: This program defines a class named Creature, which represents a Creature on the field.

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):

    def __init__(self, x, y, symbol):
        """
        Constructor for the Creature class.

        :param x: x coordinate of the creature
        :type x: int
        :param y: y coordinate of the creature
        :type y: int
        :param symbol: The text symbol representing the field inhabitant.
        :type symbol: str
        """
        super().__init__(symbol)
        self._x = x
        self._y = y

    def getX(self):
        """
        Get X coordinate
        """
        return self._x

    def setX(self, x):
        """
        Set X coordinate
        :param x: x coordinate of the creature
        :type x: int
        """
        self._x = x

    def getY(self):
        """
        Get Y coordinate
        """
        return self._y

    def setY(self, y):
        """
        Set Y coordinate
        :param y: y coordinate of the creature
        :type y: int
        """
        self._y = y
