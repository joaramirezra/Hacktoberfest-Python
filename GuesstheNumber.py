"""
OOPS Practise #1

GuessingNumberGame : Python 3.9.0

"""

import random

class GuessingNumberGame:

    def __init__(self, max_range = 100):
        self.max_range = max_range
        self.rand_value = -1

    def set_max_range(self):
        """
        Set the maximum range
        """

        while(True):
            print("Add the maximum value in between you want to guess :", end=" ")
            value = int(input())
            if value == 0:
                print("Invalid Range Given")
            else:
                break
        self.max_range = value
        print('Max Range updated...')

    def get_rand_value(self):
        """
        Generate the random value
        """

        self.rand_value = random.randint(1, self.max_range)
        print('Random Value generated...')

    def validate(self, guessed_number):
        """
        Validate the number is guessed correctly or not
        """

        if guessed_number == self.rand_value:
            print("You guessed the correct number!")
            return 0
        elif guessed_number < self.rand_value:
            print("Guess a higher one!")
            return 1
        else:
            print("Guess a lower one")
            return 1

    def round(self):
        """
        Rounds of the games
        """

        print("Guess the Number : ", end = " ")
        guessed_number = int(input())
        if guessed_number > self.max_range:
            print("Invalid Number. Out of bounds!")
            return 1
        else:
            result = self.validate(guessed_number)
            return result

    def play(self):
        """
        Start the game
        """

        self.set_max_range()
        self.get_rand_value()
        print("Game has been started...")
        while self.round():
            pass
        print('THE END...\n')


if __name__ == "__main__":
    while(True):
        print("Type 1 to start , 0 to close :", end = " ")
        choice = int(input())
        if choice == 1:
            game = GuessingNumberGame()
            game.play()
        elif choice == 0:
            print("Thanks for playing!!!\n")
            break
        else:
            print("Invalid Input! Try again")