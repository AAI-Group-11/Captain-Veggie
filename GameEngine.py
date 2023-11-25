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
