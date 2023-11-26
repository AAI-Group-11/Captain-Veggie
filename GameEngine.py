# Author: Divyang, Gurbeer, Prabal
# Date: 25th November, 2023
# Description: This program initializes the Game.

import os
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
import random


class GameEngine():

    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        """
        Constructor for GameEngine class
        """
        self.field = []
        self.rabits = []
        self.cap = None
        self.vegetables = []
        self.score = 0

    def initVeggies(self):
        """
        Create vegatable file with vegetable data.
        """
        veg = input("Enter the name of the veggie file: ")
        while not os.path.exists(veg):
            print(f"{veg} does not exist!")
            veg = input("Enter the name of the veggie file: ")

        with open(veg, "r") as File:
            dimesions = File.readline().strip().split(',')
            rows, cols = int(dimesions[1]), int(dimesions[2])
            self.field = [[None for j in range(cols)] for i in range(rows)]
            for i in File:
                info = i.strip().split(',')
                v = Veggie(info[0], info[1], int(info[2]))
                self.vegetables.append(v)

            for _ in range(self.__NUMBEROFVEGGIES):
                while True:
                    rows = random.randint(0, rows - 1)
                    cols = random.randint(0, cols - 1)
                    if self.field[rows][cols] is None:
                        randomVeggie = random.choice(self.vegetables)
                        self.field[rows][cols] = randomVeggie
                        break

    def initCaptain(self):
        """
        Initialize Captain position
        """
        goon = True
        while goon:
            rows = random.randint(0, len(self.field)-1)
            cols = random.randint(0, len(self.field[1])-1)

            if self.field[rows][cols] is None:
                self.cap = Captain(rows, cols)
                self.field[rows][cols] = self.cap
                goon = False

    def initRabbits(self):
        """
        Initialize number of Rabbits on the field.
        """

        for i in range(len(self.__NUMBEROFRABBITS)):
            rows = random.randint(0, len(self.field)-1)
            cols = random.randint(0, len(self.field[1])-1)
            goon = True
            while goon:
                if self.field[rows][cols] is None:
                    rabbit = Rabbit(rows, cols)
                    self.rabits.append(rabbit)
                    goon = False

    def initializeGame(self):
        """
        Initialize the game.
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        """
        This function shows amount of vegetables remaining in the field
        :return: count of vegetables
        :rtype: int
        """

        count = 0
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if isinstance(self.field[i], Veggie):
                    count += 1

        return count

    def intro(self):
        """
        This function introduce us to the game and its rules
        """
        # TODO: add snake info in the intro

        print("""Welcome to Captain Veggie!
The rabbits have invaded your garden and you must harvest
as many vegetables as possible before the rabbits eat them
all! Each vegetable is worth a different number of points
so go for the high score!\n""")

        print("The vegetables are: ")
        for v in self.vegetables:
            print(v)

        print("""\nCaptain Veggie is V, and the rabbits are R's.

Good luck!\n""")

    def printField(self):
        """
        This function prints out the whole field
        """
        out = "###" * (len(self.field[0])) + "#" * 2 + "\n"

        for i in range(len(self.field)):
            out += "# "
            for j in range(len(self.field[i])):
                out += self.field[i][j].getSymbol() + " "

            out += " #\n"

        out = "###" * (len(self.field[0])) + "#" * 2

        print(out)

    def getScore(self):
        """
        This function returns our score
        :return: returns the current score
        :rtype: int
        """
        return self.score

    def moveRabbits(self):
        """
        This function defines the movement of rabbit in the field
        """
        for rabbit in self.rabits:
            new_x = random.randint(rabbit.getX()-1, rabbit.getX+1)
            new_y = random.randint(rabbit.getY()-1, rabbit.getY()+1)

            if new_x < 0 or new_x >= len(self.field[0]) or new_y < 0 or new_y >= len(self.field):
                continue

            # TODO: add snake condition
            elif isinstance(self.field[new_x][new_y], Rabbit) or isinstance(self.field[new_x][new_y], Captain):
                continue

            else:
                old_x = rabbit.getX()
                old_y = rabbit.getY()

                self.field[new_x][new_y] = rabbit
                rabbit.setX(new_x)
                rabbit.setY(new_y)

                self.field[old_x][old_y] = None

