# Author: Divyang, Gurbeer, Prabal
# Date: 19th November, 2023
# Description: This program defines a class named FieldInhabitant, which represents an inhabitant of a field.


class FieldInhabitant:

    def __init__(self, symbol):
        """
        Constructor for the FieldInhabitant class.

        :param symbol: The text symbol representing the field inhabitant.
        :type symbol: str
        """
        self._symbol = symbol

    def getSymbol(self):
        """
        Getter method for retrieving the symbol of the field inhabitant.

        :return: The text symbol representing the field inhabitant.
        :rtype: str
        """
        return self._symbol

    def setSymbol(self, new_symbol):
        """
        Setter method for updating the symbol of the field inhabitant.

        :param new_symbol: The new text symbol to assign to the field inhabitant.
        :type new_symbol: str
        """
        self._symbol = new_symbol
