import random

# creates a random number between 1-100
randomNum = random.randrange(1,100)
score = 50
#print(randomNum)
userNum = input("Hello, welcome to the Random Number game!\nPlease pick a number between 1 and 100")
print("You now have 5 guesses, push any key to play")
user1 = input("First guess?\n")
userGuess1 = int(user1)
if userGuess1 == randomNum:
    print("Wow, got it on the first try! Amazing!")
    print("Your score is:" + str(score))
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
    print("Your score is:" + str(score))
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
    print("Your score is:" + str(score))
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
    print("Your score is:" + str(score))    
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
    print("Your score is:" + str(score))
elif userGuess5 > randomNum:
    print("Wrong Number, this number is a bit too high")
    print("I'm sorry, you have lost.")
elif userGuess5 < randomNum:
    print("Incorrect, this number is too low ")
    print("I'm sorry, you have lost.")
else:
    ("That's not right at all.")



