# Author: Divyang, Gurbeer, Prabal
# Date: 25th November, 2023
# Description: This program initializes the Game.

import os
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake
import random


class GameEngine:
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
            dimesions = File.readline().strip().split(",")
            rows, cols = int(dimesions[1]), int(dimesions[2])
            self.field = [[None for j in range(cols)] for i in range(rows)]
            for i in File:
                info = i.strip().split(",")
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
            rows = random.randint(0, len(self.field) - 1)
            cols = random.randint(0, len(self.field[1]) - 1)

            if self.field[rows][cols] is None:
                self.cap = Captain(rows, cols)
                self.field[rows][cols] = self.cap
                goon = False

    def initRabbits(self):
        """
        Initialize number of Rabbits on the field.
        """

        for i in range(len(self.__NUMBEROFRABBITS)):
            rows = random.randint(0, len(self.field) - 1)
            cols = random.randint(0, len(self.field[1]) - 1)
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

        print(
            """Welcome to Captain Veggie!
The rabbits have invaded your garden and you must harvest
as many vegetables as possible before the rabbits eat them
all! Each vegetable is worth a different number of points
so go for the high score!\n"""
        )

        print("The vegetables are: ")
        for v in self.vegetables:
            print(v)

        print(
            """\nCaptain Veggie is V, and the rabbits are R's.

Good luck!\n"""
        )

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
            new_x = random.randint(rabbit.getX() - 1, rabbit.getX + 1)
            new_y = random.randint(rabbit.getY() - 1, rabbit.getY() + 1)

            if (
                new_x < 0
                or new_x >= len(self.field[0])
                or new_y < 0
                or new_y >= len(self.field)
            ):
                continue

            # TODO: add snake condition
            elif isinstance(self.field[new_x][new_y], Rabbit) or isinstance(
                self.field[new_x][new_y], Captain
            ):
                continue

            else:
                old_x = rabbit.getX()
                old_y = rabbit.getY()

                self.field[new_x][new_y] = rabbit
                rabbit.setX(new_x)
                rabbit.setY(new_y)

                self.field[old_x][old_y] = None

    def moveCptVertical(self, movement):
        """
        Sets vertical movement of the Captain
        :param movement: "w"/"W" or "s"/"S" representing up or down movement
        :type movement: str
        """
        captX = self.cap.getX()
        captY = self.cap.getY()
        movement = movement.lower()

        if movement == "w" and captY > 0:
            if self.field[captX][captY - 1] == None:
                self.cap.setY(captY - 1)
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX][captY - 1], Veggie):
                self.cap.setY(captY - 1)
                print(f"Yummy! A delicious {self.field[captX][captY - 1].getName()}")
                self.cap.addVeggie(self.field[captX][captY - 1])
                self.score += self.field[captX][captY - 1].getPoints()
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX][captY - 1], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.field[captX][captY - 1], Snake):
                print("Don't step on the snake!")

        elif movement == "s" and captY < len(self.field) - 1:
            if self.field[captX][captY + 1] == None:
                self.cap.setY(captY + 1)
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX][captY + 1], Veggie):
                self.cap.setY(captY + 1)
                print(f"Yummy! A delicious {self.field[captX][captY + 1].getName()}")
                self.cap.addVeggie(self.field[captX][captY + 1])
                self.score += self.field[captX][captY + 1].getPoints()
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX][captY + 1], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.field[captX][captY + 1], Snake):
                print("Don't step on the snake!")

    def moveCptHorizontal(self, movement):
        """
        Sets horizontal movement of the Captain
        :param movement: "a"/"A" or "d"/"D" representing left or right movement
        :type movement: str
        """
        captX = self.cap.getX()
        captY = self.cap.getY()
        movement = movement.lower()

        if movement == "a" and captX > 0:
            if self.field[captX - 1][captY] == None:
                self.cap.setX(captX - 1)
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX - 1][captY], Veggie):
                self.cap.setX(captX - 1)
                print(f"Yummy! A delicious {self.field[captX - 1][captY].getName()}")
                self.cap.addVeggie(self.field[captX - 1][captY])
                self.score += self.field[captX - 1][captY].getPoints()
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX - 1][captY], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.field[captX - 1][captY], Snake):
                print("Don't step on the snake!")

        elif movement == "d" and captX < len(self.field[0]) - 1:
            if self.field[captX + 1][captY] == None:
                self.cap.setX(captX + 1)
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX + 1][captY], Veggie):
                self.cap.setX(captX + 1)
                print(f"Yummy! A delicious {self.field[captX + 1][captY].getName()}")
                self.cap.addVeggie(self.field[captX + 1][captY])
                self.score += self.field[captX + 1][captY].getPoints()
                self.field[captX][captY] = None
                self.field[self.cap.getX()][self.cap.getY()] = self.cap

            elif isinstance(self.field[captX + 1][captY], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.field[captX + 1][captY], Snake):
                print("Don't step on the snake!")

    def moveCaptain(self):
        """
        Takes input for Captain's movement and calls appropriate function depending on
        whether the movement is horizontal or vertical
        """
        movement = input(
            "Would you like to move up(W), down(S), left(A), or right(D): "
        )
        movement = movement.lower()

        if movement not in ["w", "a", "s", "d"]:
            print(f"{movement} is not a valid option")

        if (movement == "w" and self.cap.getY() > 0) or (
            movement == "s" and self.cap.getY() < len(self.field) - 1
        ):
            self.moveCptVertical(movement)

        elif (movement == "a" and self.cap.getX() > 0) or (
            movement == "d" and self.cap.getX() < len(self.field[0]) - 1
        ):
            self.moveCptHorizontal(movement)

        else:
            print("You can't move that way!")

    def gameOver(self):
        """
        Informs the user when the game is over, displays their score, takes
        their initials to store in High Scores and displays the current High Scores
        """
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for veggie in self.cap.getVeggies():
            print(veggie.getName())

        print(f"Your score was: {self.score}")

    def highScore(self):
        highScoreList = []
        if os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, "rb") as hsf:
                highScoreList.extend(pickle.load(hsf))

        playerInitials = input(
            "Please enter your three initials to go on the scoreboard: "
        )
        playerInitials = playerInitials[:3].upper()
        newHighScore = (self.score, playerInitials)
        highScoreList.append(newHighScore)
        highScoreList = sorted(highScoreList, reverse=True)

        print("HIGH SCORES")
        print("Name\tScore")
        for score, initials in highScoreList:
            print(f"{initials}\t{score}")

        with open(self.__HIGHSCOREFILE, "wb") as hsf:
            pickle.dump(highScoreList, hsf)
