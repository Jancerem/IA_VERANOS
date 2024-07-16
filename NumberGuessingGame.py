#Veranos Inteligencia Artificial // Jan Carlos Morales Rives 1905790

import random

def numberGuessingGame():
    targetNumber = random.randint(1, 1000)
    guess = None

    while guess != targetNumber:
        guess = int(input("Adivina un numero entre 1 y 1000: "))
        
        if guess < targetNumber:
            print("Más grande!")
        elif guess > targetNumber:
            print("Más pequeño!")
        else:
            print("Felicidades! Adivinaste el número.")

# Usage
numberGuessingGame()