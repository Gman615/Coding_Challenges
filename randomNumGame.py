import random
import sys

# creates a random number between 1-50
randomNum = random.randrange(1,50)
score = 50
print(randomNum)
print("Hello, welcome to the Random Number game!\nYou have 5 guesses to figure out\nwhich number I am thinking of between 1 and 50")

user1 = input("First guess?\n")
userGuess1 = int(user1)
# if/else statements offer clues based on guesses, also ends the program if correct number is guessed.
if userGuess1 == randomNum:
    print("Wow, got it on the first try! Amazing!")
    print("Your score is: " + str(score))
    sys.exit()
elif userGuess1 > randomNum:
    print("Wrong Number, this number is a bit too high")
    score = score - 10
elif userGuess1 < randomNum:
    print("Incorrect, this number is too low ")
    score = score - 10
else:
    ("That's not right at all.")
user2 = input("Second guess?\n")
userGuess2 = int(user2)
if userGuess2 == randomNum:
    print("You guessed the correct number!")
    print("Your score is: " + str(score))
    sys.exit()    
elif userGuess2 > randomNum:
    print("Wrong Number, this number is a bit too high")
    score = score - 10    
elif userGuess2 < randomNum:
    print("Incorrect, this number is too low ")
    score = score - 10    
else:
    ("That's not right at all.")
user3 = input("Third guess?\n")
userGuess3 = int(user3)
if userGuess3 == randomNum:
    print("You guessed the correct number!")
    print("Your score is: " + str(score))
    sys.exit()    
elif userGuess3 > randomNum:
    print("Wrong Number, this number is a bit too high")
    score = score - 10    
elif userGuess3 < randomNum:
    print("Incorrect, this number is too low ")
    score = score - 10    
else:
    ("That's not right at all.")
user4 = input("Fourth guess?\n")
userGuess4 = int(user4)
if userGuess4 == randomNum:
    print("You guessed the correct number!")
    print("Your score is: " + str(score))
    sys.exit()
elif userGuess4 > randomNum:
    print("Wrong Number, this number is a bit too high")
    score = score - 10    
elif userGuess4 < randomNum:
    print("Incorrect, this number is too low ")
    score = score - 10    
else:
    ("That's not right at all.")
user5 = input("Fifth guess?\n")
userGuess5 = int(user5)
if userGuess5 == randomNum:
    print("You guessed the correct number!")
    print("Your score is: " + str(score))
    sys.exit()
elif userGuess5 > randomNum:
    print("Wrong Number, this number is a bit too high")
    print("I'm sorry, you have lost.")
elif userGuess5 < randomNum:
    print("Incorrect, this number is too low ")
    print("I'm sorry, you have lost.")
else:
    ("That's not right at all.")



