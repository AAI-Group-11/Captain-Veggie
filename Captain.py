# Author: Divyang, Gurbeer, Prabal
# Date: 21st November, 2023
# Description: This program defines a class named Captain, which represents the Captain on the field.

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        """Constructor for the Captain class

        :param x: x coordinate of captain
        :type x: int
        :param y: y coordinate of captain
        :type y: int
        """
        super().__init__(x, y, "V")
        self._veggies = []

    def addVeggie(self, veggie):
        """Add a veggie to the __veggies list

        :param veggie: A veggie object
        :type veggie: object
        """
        self._veggies.append(veggie)

    def getVeggies(self):
        """Get all veggies collected by captain

        :return: Veggies: List of veggie objects
        :rtype: list
        """
        return self._veggies

    def removeVeggies(self):
        """
        removes the last veggie captured by the captain

        :return: last veggie captured
        :rtype: object
        """
        return self._veggies.pop()
