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
        self.__field = []
        self.__rabbits = []
        self.__cap = None
        self.__vegetables = []
        self.__snake = None
        self.__score = 0

    def initVeggies(self):
        """
        Create vegetable file with vegetable data.
        """
        veg = input("Enter the name of the veggie file: ")
        while not os.path.exists(veg):
            print(f"{veg} does not exist!")
            veg = input("Enter the name of the veggie file: ")

        with open(veg, "r") as File:
            dimensions = File.readline().strip().split(",")
            rows, cols = int(dimensions[1]), int(dimensions[2])
            self.__field = [[None for j in range(cols)] for i in range(rows)]
            for i in File:
                info = i.strip().split(",")
                v = Veggie(info[0], info[1], int(info[2]))
                self.__vegetables.append(v)

            for _ in range(self.__NUMBEROFVEGGIES):
                while True:
                    row = random.randint(0, rows - 1)
                    col = random.randint(0, cols - 1)
                    if self.__field[row][col] is None:
                        randomVeggie = random.choice(self.__vegetables)
                        self.__field[row][col] = randomVeggie
                        break

    def initCaptain(self):
        """
        Initialize Captain position
        """
        goon = True
        while goon:
            rows = random.randint(0, len(self.__field) - 1)
            cols = random.randint(0, len(self.__field[1]) - 1)

            if self.__field[rows][cols] is None:
                self.__cap = Captain(cols, rows)
                self.__field[rows][cols] = self.__cap
                goon = False

    def initRabbits(self):
        """
        Initialize number of Rabbits on the field.
        """

        for i in range(self.__NUMBEROFRABBITS):
            goon = True
            while goon:
                rows = random.randint(0, len(self.__field) - 1)
                cols = random.randint(0, len(self.__field[1]) - 1)
                if self.__field[rows][cols] is None:
                    rabbit = Rabbit(cols, rows)
                    self.__rabbits.append(rabbit)
                    self.__field[rows][cols] = rabbit
                    goon = False

    def initSnake(self):
        """
        Initialize number of Snakes on the field
        """
        goon = True
        while goon:
            rows = random.randint(0, len(self.__field) - 1)
            cols = random.randint(0, len(self.__field[1]) - 1)
            if self.__field[rows][cols] is None:
                self.__snake = Snake(cols, rows)
                self.__field[rows][cols] = self.__snake
                goon = False

    def initializeGame(self):
        """
        Initialize the game.
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()

    def remainingVeggies(self):
        """
        This function shows amount of vegetables remaining in the field
        :return: count of vegetables
        :rtype: int
        """

        count = 0
        for i in range(len(self.__field)):
            for j in range(len(self.__field[i])):
                if isinstance(self.__field[i][j], Veggie):
                    count += 1

        return count

    def intro(self):
        """
        This function introduce us to the game and its rules
        """

        print(
            """Welcome to Captain Veggie!
The rabbits have invaded your garden and you must harvest
as many vegetables as possible before the rabbits eat them
all! Each vegetable is worth a different number of points
so go for the high score! Beware of a slithering snake in 
the garden—it inches closer to you, and if it catches you,
you'll lose five of the vegetables you've collected. 
Let the vegetable-harvesting adventure begin!\n"""
        )

        print("The vegetables are: ")
        for v in self.__vegetables:
            print(v)

        print(
            """\nCaptain Veggie is V, and the rabbits are R's.

Good luck!\n"""
        )

    def printField(self):
        """
        This function prints out the whole field
        """
        out = "###" * (len(self.__field[0])) + "#" * 2 + "\n"

        for i in range(len(self.__field)):
            out += "# "
            for j in range(len(self.__field[i])):
                out += self.__field[i][j].getSymbol() + " "

            out += " #\n"

        out = "###" * (len(self.__field[0])) + "#" * 2

        print(out)

    def getScore(self):
        """
        This function returns our score
        :return: returns the current score
        :rtype: int
        """
        return self.__score

    def moveRabbits(self):
        """
        This function defines the movement of rabbit in the field
        """
        for rabbit in self.__rabbits:
            new_x = random.randint(rabbit.getX() - 1, rabbit.getX + 1)
            new_y = random.randint(rabbit.getY() - 1, rabbit.getY() + 1)

            if (
                new_x < 0
                or new_x >= len(self.__field[0])
                or new_y < 0
                or new_y >= len(self.__field)
            ):
                continue

            elif (isinstance(self.__field[new_x][new_y], Rabbit)
                  or isinstance(self.__field[new_x][new_y], Captain)
                  or isinstance(self.__field[new_x][new_y], Snake)
                  ):
                continue

            else:
                old_x = rabbit.getX()
                old_y = rabbit.getY()

                self.__field[new_x][new_y] = rabbit
                rabbit.setX(new_x)
                rabbit.setY(new_y)

                self.__field[old_x][old_y] = None

    def moveSnake(self):
        snake_x = self.__Snake.getX()
        snake_y = self.__Snake.getY()

        captain_x = self.__cap.getX()
        captain_y = self.__cap.getY()

        distance = 1000

        moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        final_move = None

        for move in moves:
            snake_new_x = snake_x + move[0]
            snake_new_y = snake_y + move[1]

            if (
                    snake_new_x < 0
                    or snake_new_x >= len(self.__field[0])
                    or snake_new_y < 0
                    or snake_new_y > len(self.__field)
            ):
                continue

            elif (
                    isinstance(self.__field[snake_new_x][snake_new_y], Rabbit)
                    or isinstance(self.__field[snake_new_x][snake_new_y], Veggie)
            ):
                continue

            else:
                temp = abs(captain_x - snake_new_x) + \
                    abs(captain_y - snake_new_y)
                if temp <= distance:
                    distance = temp
                    final_move = [snake_new_x, snake_new_y]

        snake_new_x = final_move[0]
        snake_new_y = final_move[1]

        if isinstance(self.__field[snake_new_x][snake_new_y], Captain):
            veggies_basket = len(self.__cap.getVeggies)
            if veggies_basket >= 5:
                for i in range(5):
                    remove = self.__cap.removeVeggies()
                    self.__score -= remove.getPoints()
                print("Oops! The snake caught you! You lost 5 vegetables.")
            else:
                for i in range(veggies_basket):
                    remove = self.__cap.removeVeggies()
                    self.__score -= remove.getPoints()
                print("Oops! The snake caught you! You lost all vegetables.")

            self.initSnake()

        else:
            self.__field[snake_new_x][snake_new_y] = self.__Snake
            self.__field[snake_x][snake_y] = None

    def moveCptVertical(self, movement):
        """
        Sets vertical movement of the Captain
        :param movement: "w"/"W" or "s"/"S" representing up or down movement
        :type movement: str
        """
        captX = self.__cap.getX()
        captY = self.__cap.getY()
        movement = movement.lower()

        if movement == "w" and captY > 0:
            if self.__field[captX][captY - 1] == None:
                self.__cap.setY(captY - 1)
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX][captY - 1], Veggie):
                self.__cap.setY(captY - 1)
                print(
                    f"Yummy! A delicious {self.__field[captX][captY - 1].getName()}")
                self.__cap.addVeggie(self.__field[captX][captY - 1])
                self.__score += self.__field[captX][captY - 1].getPoints()
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX][captY - 1], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.__field[captX][captY - 1], Snake):
                print("Don't step on the snake!")

        elif movement == "s" and captY < len(self.__field) - 1:
            if self.__field[captX][captY + 1] == None:
                self.__cap.setY(captY + 1)
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX][captY + 1], Veggie):
                self.__cap.setY(captY + 1)
                print(
                    f"Yummy! A delicious {self.__field[captX][captY + 1].getName()}")
                self.__cap.addVeggie(self.__field[captX][captY + 1])
                self.__score += self.__field[captX][captY + 1].getPoints()
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX][captY + 1], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.__field[captX][captY + 1], Snake):
                print("Don't step on the snake!")

    def moveCptHorizontal(self, movement):
        """
        Sets horizontal movement of the Captain
        :param movement: "a"/"A" or "d"/"D" representing left or right movement
        :type movement: str
        """
        captX = self.__cap.getX()
        captY = self.__cap.getY()
        movement = movement.lower()

        if movement == "a" and captX > 0:
            if self.__field[captX - 1][captY] == None:
                self.__cap.setX(captX - 1)
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX - 1][captY], Veggie):
                self.__cap.setX(captX - 1)
                print(
                    f"Yummy! A delicious {self.__field[captX - 1][captY].getName()}")
                self.__cap.addVeggie(self.__field[captX - 1][captY])
                self.__score += self.__field[captX - 1][captY].getPoints()
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX - 1][captY], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.__field[captX - 1][captY], Snake):
                print("Don't step on the snake!")

        elif movement == "d" and captX < len(self.__field[0]) - 1:
            if self.__field[captX + 1][captY] == None:
                self.__cap.setX(captX + 1)
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX + 1][captY], Veggie):
                self.__cap.setX(captX + 1)
                print(
                    f"Yummy! A delicious {self.__field[captX + 1][captY].getName()}")
                self.__cap.addVeggie(self.__field[captX + 1][captY])
                self.__score += self.__field[captX + 1][captY].getPoints()
                self.__field[captX][captY] = None
                self.__field[self.__cap.getX()][self.__cap.getY()] = self.__cap

            elif isinstance(self.__field[captX + 1][captY], Rabbit):
                print("Don't step on the bunnies!")

            elif isinstance(self.__field[captX + 1][captY], Snake):
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

        if (movement == "w" and self.__cap.getY() > 0) or (
            movement == "s" and self.__cap.getY() < len(self.__field) - 1
        ):
            self.moveCptVertical(movement)

        elif (movement == "a" and self.__cap.getX() > 0) or (
            movement == "d" and self.__cap.getX() < len(self.__field[0]) - 1
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
        for veggie in self.__cap.getVeggies():
            print(veggie.getName())

        print(f"Your score was: {self.__score}")

    def highScore(self):
        highScoreList = []
        if os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, "rb") as hsf:
                highScoreList.extend(pickle.load(hsf))

        playerInitials = input(
            "Please enter your three initials to go on the scoreboard: "
        )
        playerInitials = playerInitials[:3].upper()
        newHighScore = (self.__score, playerInitials)
        highScoreList.append(newHighScore)
        highScoreList = sorted(highScoreList, reverse=True)

        print("HIGH SCORES")
        print("Name\tScore")
        for score, initials in highScoreList:
            print(f"{initials}\t{score}")

        with open(self.__HIGHSCOREFILE, "wb") as hsf:
            pickle.dump(highScoreList, hsf)
