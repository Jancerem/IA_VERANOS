#Veranos Inteligencia Artificial // Jan Carlos Morales Rives 1905790

import random

def hangman():
    words = ["inteligencia", "artificial", "maquina", "programar", "phyton"]
    word = random.choice(words)
    guessedWord = ["_"] * len(word)
    attempts = 6
    guessedLetters = set()

    while attempts > 0 and "_" in guessedWord:
        print(" ".join(guessedWord))
        guess = input("Adivina una letra: ").lower()

        if guess in guessedLetters:
            print("Ya adivinaste esa letra.")
            continue

        guessedLetters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessedWord[i] = guess
        else:
            attempts -= 1
            print(f"Equivocado. Tienes {attempts} intentos restantes.")

    if "_" not in guessedWord:
        print("Felicidades! adivinaste la palabra:", word)
    else:
        print("Te quedaste sin intentos. La polabra era:", word)

# Jugar
hangman()