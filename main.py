# Author: Divyang, Gurbeer, Prabal
# Date: 3rd December, 2023
# Description: This program defines the main function of the game that imports
# and initializes all classes to run the game


from GameEngine import GameEngine


def main():
    game = GameEngine()
    game.initializeGame()
    game.intro()
    remainingVeggies = game.remainingVeggies()

    captainMoveCounter = 0
    while remainingVeggies > 0:
        print(f"Remaining Vegetables: {remainingVeggies}")
        print(f"Player's Score: {game.getScore()}")

        if captainMoveCounter == 0:
            game.printField()

        elif captainMoveCounter > 0:
            game.moveRabbits()
            game.printField()

        game.moveCaptain()
        captainMoveCounter += 1

        game.moveSnake()

        remainingVeggies = game.remainingVeggies()

    game.gameOver()

    game.highScore()


main()
