"""
Purpose
    Demostrar el uso de ingreso basico de datos en un programa

Running the code
    py main.py

Additional information
    Python 3.9.7

"""
import random

guessesTaken = 0
minNumber = 1
maxNumber = 20
guees = None

print("===============================================================")
print("                        NUMBER GUESSING                        ")
print("===============================================================")

username = str(input("Enter your username ~> "))

number = random.randint(minNumber, maxNumber)
print("Well {} I am thinking in a number between {} and {} ".format
        (username, str(number), str(maxNumber)))

while guessesTaken < 6:
    guess = int(input("Take a guess ~> "))
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
    print("$ Good job {} you guessed my number in {} guesses".format
            (username, guessesTaken))

if guess != number:
    number = str(number)
    print("=================================================")
    print("$ No. the number i was thinking of was {}".format(number))

"""Se define los parametros
:param guessesTaken: Numero de intentos durante el juego
:param minNumber: Numero minimo del rango de numeros para adivinar
:param maxNumer: Numero maximo del rango de numeros para adivinar
:param username: Nombre del usuario para el juego
:param number: Numero generado por el programa
"""
