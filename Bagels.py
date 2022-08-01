

import random
#can be any number from 1 - 10
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(""" Bagels, a deductive logic game.

bagels is a deductive logic game in which you have to guess a secret three-digit number based on clues
In response to your guess, the game offers one of the following hints: pico(when your guess has a correct digit in the wrong place),
fermi(when your guess has a correct digit in the correct place) and bagels(if your guess has no correct digits).
you have 10 tries to guess the secret number""".format(NUM_DIGITS))
#main loop for the group
    while True:
        #this stores the secret number the player needs to guess
        secretNum = getsecretNum()
        print("I have thought up a number.")
        print(" you have {} guesses to get it.".format(MAX_GUESSES))


        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print ("Guess #{}:".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
            #they're correct, so break out of this loop    
                break
            if numGuesses > MAX_GUESSES:
                print("you ran out of guesses.")
                print("The answer was {}.".format(secretNum))

        #Ask player if they want to play again
        print("Do you want to play again ? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def getsecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    #create a list of digits from 0-9
    numbers = list("0123456789")
    #shuffle them into random order
    random.shuffle(numbers)
    #get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for l in range(NUM_DIGITS):
        secretNum += str(numbers[1])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
and secret number pair."""
    if guess == secretNum:
         return "you got it !!"

    clues = []

    for l in range(len(guess)):
         if guess[1] == secretNum[1]:
             #A correct digit is in the correct place.
             clues.append("Fermi")

         elif guess[1] in secretNum:
             #A correct digit is in the incorrect place.
             clues.append("pico")

    if len(clues) == 0:
         #There are no correct digits at all
         return "Bagels"

    else:
         #this sorts the clues in alphabetical order,
         #so their original order doesnt give away the information
         clues.sort()
         #Make a single string from the list of string clues
         return "".join(clues)

#if the program is run (instead of imported), ru the game:
if __name__ == "__main__":
    main()
             
    






        
