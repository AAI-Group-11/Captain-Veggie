# Author: Divyang, Gurbeer, Prabal
# Date: 21st November, 2023
# Description: This program defines a class named Veggie, which represents vegetables on the field.

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):

    def __init__(self, name, symbol, points):
        """
        Constructor for the Veggie class.

        :param name: Name of the vegetable
        :type name: string
        :param points: points of the vegetable
        :type points: int
        :param symbol: The text symbol representing the field inhabitant.
        :type symbol: str
        """
        super().__init__(symbol)

        self.__name = name
        self.__points = points

    def __str__(self):

        return f"{self._symbol}: {self.__name} {self.__points} points"

    def getName(self):
        """
        Get Name
        """
        return self.__name

    def setName(self, name):
        """
        set Name

        :param name: Name of the vegtable
        :type name: string
        """

        self.__name = name

    def getPoints(self):
        """
        Get Points
        """
        return self.__points

    def setPoints(self, points):
        """
        set Points

        :param points: points of the vegtable
        :type name: int
        """

        self.__points = points


v = Veggie("Garlic", "G", 20)

print(v)
