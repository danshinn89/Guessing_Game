import sys
import random


# Define function guessing game
# Game is created inside this function and at the end depending on user input it will restart

def guessingGame():
    number = random.randint(1, 10)

    counter = 0

    name = input("Please enter your name: ")
    start = input("Ok " + name + " Lets Play A Guessing Game [Y]/[N]: ")

    if start == "n":
        print("That's Tragic"), sys.exit()

    while True:
        if start == "y":
            guess = int(input("Ok take a guess on a number 1-10: "))
            if guess > number:
                print("You guessed too high")
            if guess < number:
                print("You guessed too low")

                while guess != number:
                    counter += 1
                    guess = int(input("Try Again: "))
                if counter == 2 and guess != number:
                    print("Its taken you", counter, "tries")
                if counter == 5 and guess != number:
                    print("Yikes", counter, "Tries. Pack It UP!")
                if counter == 7 and guess != number:
                    print(counter, "tries. I think this is a record")

                if guess == number:
                    print("Correct. You took", counter, "tries")
                    restart = input("Would You Like To Play Again? y/n")
                    if restart == 'y':
                        guessingGame()
                    else:
                        print("Goodbye"), sys.exit()
                        break
guessingGame()
