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

    # Constants for the game
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        """
        Constructor for GameEngine class
        """
        # Initialize instance variables for the game
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
        # Get the name of the veggie file from the user
        veg = input("Please enter the name of the vegetable point file: ")

        # Check if the file exists, prompt until a valid file is provided
        while not os.path.exists(veg):
            veg = input(f"{veg} does not exist! Please enter the name of the vegetable point file: ")

        # Read vegetable data from the file and initialize the game field with veggies
        with open(veg, "r") as File:
            dimensions = File.readline().strip().split(",")
            rows, cols = int(dimensions[1]), int(dimensions[2])
            self.__field = [[None for j in range(cols)] for i in range(rows)]

            # Populate the list of vegetables with data from the file
            for i in File:
                info = i.strip().split(",")
                v = Veggie(info[0], info[1], int(info[2]))
                self.__vegetables.append(v)

            # Place a random selection of veggies on the game field
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
            # Generate random coordinates for Captain's initial position
            rows = random.randint(0, len(self.__field) - 1)
            cols = random.randint(0, len(self.__field[1]) - 1)

            # Instantiate Captain and place it on the field
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
                # Generate random coordinates for Rabbit's initial position
                rows = random.randint(0, len(self.__field) - 1)
                cols = random.randint(0, len(self.__field[1]) - 1)

                # Instantiate Rabbit and place it on the field
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
            # Generate random coordinates for Snake's initial position
            rows = random.randint(0, len(self.__field) - 1)
            cols = random.randint(0, len(self.__field[1]) - 1)

            # Instantiate Snake and place it on the field
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
the garden, it inches closer to you, and if it catches you,
you'll lose five of the vegetables you've collected. 
Let the vegetable-harvesting adventure begin!\n"""
        )

        print("The vegetables are: ")
        for v in self.__vegetables:
            print(v)

        print(
            """\nCaptain Veggie is V, the rabbits are R's, and the snake is S.

Good luck!"""
        )

    def printField(self):
        """
        This function prints out the whole field
        """
        print("##" + "###" * (len(self.__field[0])))

        out = ""
        for i in range(len(self.__field)):
            out += "# "
            for j in range(len(self.__field[i])):
                if self.__field[i][j] is not None:
                    out += self.__field[i][j].getSymbol() + "  "
                else:
                    out += "  " + " "

            out = out[:-1]
            out += "#\n"
        print(out + "##" + "###" * (len(self.__field[0])))

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
        for i in range(len(self.__rabbits)):

            # Generate random coordinates for rabbit's movement
            newX = random.randint(
                self.__rabbits[i].getX() - 1, self.__rabbits[i].getX() + 1
            )
            newY = random.randint(
                self.__rabbits[i].getY() - 1, self.__rabbits[i].getY() + 1
            )

            # Check if the new position is within the field boundaries
            if 0 <= newX < len(self.__field[0]) and 0 <= newY < len(self.__field):

                # Check if the new position is empty or contains a veggie
                if (
                    self.__field[newY][newX] is not None
                    and isinstance(self.__field[newY][newX], Veggie)
                ) or self.__field[newY][newX] is None:
                    # Move the rabbit to the new position
                    self.__field[newY][newX] = self.__rabbits[i]
                    self.__field[self.__rabbits[i].getY()][
                        self.__rabbits[i].getX()
                    ] = None
                    self.__rabbits[i].setX(newX)
                    self.__rabbits[i].setY(newY)

    def moveSnake(self):
        """
        This function defines the movement of rabbit in the field such that,
        the snake tries to move closer to the captain on every move
        """
        snake_x = self.__snake.getX()
        snake_y = self.__snake.getY()

        captain_x = self.__cap.getX()
        captain_y = self.__cap.getY()

        distance = 1000

        moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        final_move = [snake_x, snake_y]

        # Iterate through possible moves to find the one closest to the captain
        for move in moves:
            snake_new_x = snake_x + move[0]
            snake_new_y = snake_y + move[1]

            # Check if the new position is within the field boundaries
            if (
                snake_new_x < 0
                or snake_new_x >= len(self.__field[0])
                or snake_new_y < 0
                or snake_new_y >= len(self.__field)
            ):
                continue

            # Check if the new position is not occupied by rabbits or veggie
            elif isinstance(
                self.__field[snake_new_y][snake_new_x], Rabbit
            ) or isinstance(self.__field[snake_new_y][snake_new_x], Veggie):
                continue

            # calculate the shortest distance and take it as final move
            else:
                temp = abs(captain_x - snake_new_x) + abs(captain_y - snake_new_y)
                if temp <= distance:
                    distance = temp
                    final_move = [snake_new_x, snake_new_y]

        snake_new_x = final_move[0]
        snake_new_y = final_move[1]

        # when snake catches captain, and loses its vegetables
        if isinstance(self.__field[snake_new_y][snake_new_x], Captain):
            veggies_basket = len(self.__cap.getVeggies())
            if veggies_basket > 5:
                for i in range(5):
                    remove = self.__cap.removeVeggies()
                    self.__score -= remove.getPoints()
                print("Oops! The snake caught you! You lost 5 vegetables.")
            else:
                for i in range(veggies_basket):
                    remove = self.__cap.removeVeggies()
                    self.__score -= remove.getPoints()
                print("Oops! The snake caught you! You lost all vegetables.")

            self.__field[snake_y][snake_x] = None
            self.initSnake()

        # Moving snake to the new position
        else:
            self.__field[snake_y][snake_x] = None
            self.__field[snake_new_y][snake_new_x] = self.__snake
            self.__snake.setX(snake_new_x)
            self.__snake.setY(snake_new_y)

    def moveCptVertical(self, movement):
        """
        Sets vertical movement of the Captain
        :param movement: "w"/"W" or "s"/"S" representing up or down movement
        :type movement: str
        """
        captX = self.__cap.getX()
        captY = self.__cap.getY()

        if movement == "w":
            # Check if the cell above Captain contains a veggie and moving to that position.
            if isinstance(self.__field[captY - 1][captX], Veggie):
                print(f"Yummy! A delicious {self.__field[captY - 1][captX].getName()}")
                self.__cap.addVeggie(self.__field[captY - 1][captX])
                self.__score += self.__field[captY - 1][captX].getPoints()
                self.__cap.setY(captY - 1)
                self.__field[captY - 1][captX] = self.__cap
                self.__field[captY][captX] = None

            # Check if the cell below is empty and move to that position.
            elif self.__field[captY - 1][captX] is None:
                self.__cap.setY(captY - 1)
                self.__field[captY - 1][captX] = self.__cap
                self.__field[captY][captX] = None

            # Check if cell above has rabbit and thus not move the captain.
            else:
                if isinstance(self.__field[captY - 1][captX], Rabbit):
                    print("Don't step on the bunnies!")

        if movement == "s":
            # Check if the cell below Captain contains a veggie and moving to that position.
            if isinstance(self.__field[captY + 1][captX], Veggie):
                print(f"Yummy! A delicious {self.__field[captY + 1][captX].getName()}")
                self.__cap.addVeggie(self.__field[captY + 1][captX])
                self.__score += self.__field[captY + 1][captX].getPoints()
                self.__cap.setY(captY + 1)
                self.__field[captY + 1][captX] = self.__cap
                self.__field[captY][captX] = None

            # Check if the cell below is empty and move to that position.
            elif self.__field[captY + 1][captX] is None:
                self.__cap.setY(captY + 1)
                self.__field[captY + 1][captX] = self.__cap
                self.__field[captY][captX] = None

            # Check if cell below has rabbit and thus not move the captain.
            else:
                if isinstance(self.__field[captY + 1][captX], Rabbit):
                    print("Don't step on the bunnies!")

    def moveCptHorizontal(self, movement):
        """
        Sets horizontal movement of the Captain
        :param movement: "a"/"A" or "d"/"D" representing left or right movement
        :type movement: str
        """
        captX = self.__cap.getX()
        captY = self.__cap.getY()

        if movement == "a":
            # Check if the cell to the left of Captain contains a veggie and moving to that position.
            if isinstance(self.__field[captY][captX - 1], Veggie):
                print(f"Yummy! A delicious {self.__field[captY][captX - 1].getName()}")
                self.__cap.addVeggie(self.__field[captY][captX - 1])
                self.__score += self.__field[captY][captX - 1].getPoints()
                self.__cap.setX(captX - 1)
                self.__field[captY][captX - 1] = self.__cap
                self.__field[captY][captX] = None

            # Check if the cell to the left is empty and move to that position.
            elif self.__field[captY][captX - 1] is None:
                self.__cap.setX(captX - 1)
                self.__field[captY][captX - 1] = self.__cap
                self.__field[captY][captX] = None

            # Check if cell to the left has rabbit and thus not move the captain.
            else:
                if isinstance(self.__field[captY][captX - 1], Rabbit):
                    print("Don't step on the bunnies!")

        if movement == "d":
            # Check if the cell to the right of Captain contains a veggie and moving to that position.
            if isinstance(self.__field[captY][captX + 1], Veggie):
                print(f"Yummy! A delicious {self.__field[captY][captX + 1].getName()}")
                self.__cap.addVeggie(self.__field[captY][captX + 1])
                self.__score += self.__field[captY][captX + 1].getPoints()
                self.__cap.setX(captX + 1)
                self.__field[captY][captX + 1] = self.__cap
                self.__field[captY][captX] = None

            # Check if the cell to the right is empty and move to that position.
            elif self.__field[captY][captX + 1] is None:
                self.__cap.setX(captX + 1)
                self.__field[captY][captX + 1] = self.__cap
                self.__field[captY][captX] = None

            # Check if cell to the right has rabbit and thus not move the captain.
            else:
                if isinstance(self.__field[captY][captX + 1], Rabbit):
                    print("Don't step on the bunnies!")

    def moveCaptain(self):
        """
        Takes input for Captain's movement and calls appropriate function depending on
        whether the movement is horizontal or vertical
        """
        movement = input(
            "Would you like to move up(W), down(S), left(A), or right(D):"
        )
        movement = movement.lower()

        # Check if a move is valid
        if movement not in ["w", "a", "s", "d"]:
            print(f"{movement} is not a valid option")

        # Check if the movement is vertical and within field boundaries
        elif (movement == "w" and self.__cap.getY() > 0) or (
            movement == "s" and self.__cap.getY() < len(self.__field) - 1
        ):
            self.moveCptVertical(movement)

        # Check if the movement is horizontal and within field boundaries
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

        # Load existing high scores if the file exists
        if os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, "rb") as hsf:
                highScoreList.extend(pickle.load(hsf))

        # Prompt the player for their initials
        playerInitials = input(
            "Please enter your three initials to go on the scoreboard: "
        )
        playerInitials = playerInitials[:3].upper()

        # Create a new high score entry and add it to the list
        newHighScore = (self.__score, playerInitials)
        highScoreList.append(newHighScore)

        # Sort high scores in descending order
        highScoreList = sorted(highScoreList, reverse=True)

        print("HIGH SCORES")
        print("Name\tScore")
        for score, initials in highScoreList:
            print(f"{initials}\t\t{score}")

        # Save the updated high scores to the file
        with open(self.__HIGHSCOREFILE, "wb") as hsf:
            pickle.dump(highScoreList, hsf)
