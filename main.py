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

    # Initialize a counter to keep track of the captain's number of moves
    captainMoveCounter = 0

    # Initialize an infinite while loop that runs until there are
    # no vegetables left in the field
    while remainingVeggies > 0:
        # Inform the player about the number of veggies remaining in the field and
        # their current score at the start of every round
        print(f"{remainingVeggies} veggies remaining. Current Score: {game.getScore()}")

        # Prevent the rabbits from moving before the field is printed at the time of the game's initialization
        if captainMoveCounter == 0:
            game.printField()

        # Let the rabbits move once the game has started and then print the field
        elif captainMoveCounter > 0:
            game.moveRabbits()
            game.printField()

        # Prompt the player to make the captain's move and increment the move counter
        game.moveCaptain()
        captainMoveCounter += 1

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
