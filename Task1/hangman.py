import random

words = ["apple", "mango", "grape", "peach", "melon"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("Game Over! The word was:", word)