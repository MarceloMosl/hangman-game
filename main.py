from words import easy, medium, hard
import random


def main():
    difficulties = ["hard", "medium", "easy"]
    difficulty = input(f"Choose difficulty ({', '.join(difficulties)})").lower()

    while difficulty not in difficulties:
        print("Valid one please :D")
        difficulty = input(f"Choose difficulty ({', '.join(difficulties)})").lower()

    word_list = {"easy": easy, "medium": medium, "hard": hard}

    word = random.choice(word_list[difficulty])
    chancesLeft = 6
    guessedLetters = []

    displayWord = ["_"] * len(word)

    while True:
        print(f"Current word: {' '.join(displayWord)}")
        print(f"Guessed letters: {', '.join(guessedLetters)}")

        userChar = input("Guess a letter: ")

        while len(userChar) > 1 or userChar in displayWord or userChar.isnumeric():
            print("Please use a valid/new letter")
            userChar = input("Guess a letter: ")

        guessedLetters.append(userChar)

        if userChar in word:

            for i in range(len(word)):
                if userChar == word[i]:
                    displayWord[i] = word[i]

            print(f"Good job! '{userChar}' is in the word.")
            if "".join(displayWord) == word:
                print(f"Congratulations! You guessed the word: {word}")
                break

        else:
            print(f"Incorrect guesses remaining: {chancesLeft-1}")
            chancesLeft = chancesLeft - 1
            if chancesLeft == 0:
                print(f"Sorry! you lost the word was: {word}")
                break


main()
