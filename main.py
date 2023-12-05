# Author: Divyang, Gurbeer, Prabal
# Date: 3rd December, 2023
# Description: This program defines the main function of the game that imports
# and initializes all classes to run the game


from GameEngine import GameEngine


# Define main function that initializes and runs the game simulation
def main():
    # Create a GameEngine object to run the game
    game = GameEngine()
    # Initialize the game and introduce it to the player using the intro() method
    game.initializeGame()
    game.intro()
    remainingVeggies = game.remainingVeggies()

    # Initialize an infinite while loop that runs until there are
    # no vegetables left in the field
    while remainingVeggies > 0:
        # Inform the player about the number of veggies remaining in the field and
        # their current score at the start of every round
        print(f"{remainingVeggies} veggies remaining. Current Score: {game.getScore()}")

        # Print the field
        game.printField()

        # Move the rabbits in the field
        game.moveRabbits()

        # Prompt the player to make the captain's move
        game.moveCaptain()

        # Move the snake
        game.moveSnake()

        # Fetch the number of remaining veggies in the field
        remainingVeggies = game.remainingVeggies()

    # Once there are no veggies remaining in the field, finish the game by calling the gameOver() function
    game.gameOver()

    # Get the player's initials and print the current High Score table including the current game's score
    game.highScore()


# Call the main function to start the game
main()
