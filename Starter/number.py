import random

guessesTaken = 0
minNumber = 1
maxNumber = 20
print("""
===============================================================
                        NUMBER GUESSING
===============================================================
""")
username = input("Enter your username ~> ")

number = random.randint(minNumber, maxNumber)
print("Well, " + username + " I am thinking in a number between " + str(number) 
        + " and " + str(maxNumber))

while guessesTaken < 6:
    guess = input("Take a guess ~> ")
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1

    if guess < number:
        print("$ Your guess is too low")
    if guess > number:
        print("$ Your guess is too high")
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("=====================================================")
    print("$ Good job " + username + " you guessed my number in " + 
            guessesTaken + " guesses")
if guess != number:
    number = str(number)
    print("=================================================")
    print("$ No. the number i was thinking of was " + number)