# Write your code here
import random

# Variable initialization
word_list = ("python", "java", "swift", "javascript")
wins = 0
losses = 0

print("H A N G M A N")

while True:
    target_word = random.choice(word_list)
    guessed_word = '-' * len(target_word)
    played_chars = []
    guessed_character = ""
    lives = 8

    option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    if option == "play":
        # Game loop
        while lives > 0:
            # Check for valid input
            valid_input = False
            while valid_input is False:
                print('\n' + guessed_word)
                guessed_character = input("Input a letter: ")

                if (guessed_character.isalpha() and guessed_character.islower()) or (not guessed_character):
                    if (len(guessed_character) >= 2) or (not guessed_character):
                        print("Please, input a single letter.")
                    else:
                        if guessed_character in played_chars:
                            print("You've already guessed this letter.")
                        else:
                            played_chars.append(guessed_character)
                            valid_input = True
                else:
                    print("Please, enter a lowercase letter from the English alphabet.")

            # Check if guessed char is in the target word
            if guessed_character in target_word:
                if guessed_character in guessed_word:
                    print("You've already guessed this letter.")
                    continue

                # Reveal correct char in obfuscated target word
                found_char_indices = [i for i, ltr in enumerate(target_word) if ltr == guessed_character]
                for i in found_char_indices:
                    guessed_word = guessed_word[:i] + guessed_character + guessed_word[i + 1:]

                if guessed_word == target_word:
                    break
            else:
                print("That letter doesn't appear in the word.")
                lives -= 1

        if lives > 0:
            print(f"You guessed the word {target_word}!")
            print("You survived!")
            wins += 1
        else:
            print("You lost!")
            losses += 1
    elif option == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {losses} times.")
    elif option == "exit":
        break
