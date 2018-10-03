# Import Random
import random

keywords = ['seal', 'skunk', 'sheep', 'lizard', 'chameleon', 'rabbit', 'crocodile', 'panda', 'mouse', 'panther',
            'antelope', 'grizzly', 'leopard', 'badger', 'butterfly']


def create_list(word):
    letters = []
    for x in word:
        letters.append("_")
    return letters


def progress(list_a, list_b, guess):
        letter_count = 0
        for l in range(len(list_a)):
            if guess == list_a[l]:
                list_b[l] = guess
                letter_count += 1

        if letter_count > 0:
            print("\033[92m Correct! The letter " + guess + " is in the word " + str(letter_count) + " times. \033[0m")
            return list_b


def print_noose(lives):
    if lives == 10:
        print(" __________")
        print(" |/")
        print(" | \n |\n |\n |\n |\n |")
        print("_|__")
    elif lives == 9:
        print(" __________")
        print(" |/      |")
        print(" | \n |\n |\n |\n |\n |")
        print("_|__")
    elif lives == 8:
        print(" __________")
        print(" |/      |")
        print(" |      (")
        print(" | \n |\n |\n |\n |")
        print("_|__")
    elif lives == 7:
        print(" __________")
        print(" |/      |")
        print(" |      (_")
        print(" | \n |\n |\n |\n |")
        print("_|__")
    elif lives == 6:
        print(" __________")
        print(" |/      |")
        print(" |      (_)")
        print(" | \n |\n |\n |\n |")
        print("_|__")
    elif lives == 5:
        print(" __________")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\")
        print(" | \n |\n |\n |")
        print("_|__")
    elif lives == 4:
        print(" __________")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|")
        print(" | \n |\n |\n |")
        print("_|__")
    elif lives == 3:
        print(" __________")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" | \n |\n |\n |")
        print("_|__")
    elif lives == 2:
        print(" __________")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |")
        print(" | \n |\n |")
        print("_|__")
    elif lives == 1:
        print(" __________")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |      /")
        print(" | \n |\n |")
        print("_|__")
    elif lives == 0:
        print(" __________")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / \\")
        print(" | \n |\n |")
        print("_|__")


output = "string"
game = True

while game:
    word = random.choice(keywords)
    progress_list = create_list(word)
    lives = 10
    incorrect = []

    print("---------------------------------------")
    print("Welcome to Hangman!")
    print("Enter a letter to try and guess my word.")
    print("----------------------------------------")

    while output != word:
        if progress_list == word.split():               # guessed one letter at a time to win
            output = word
            print("That's right! You win!")
            break
        elif lives == 0:
            print("Game over! You have run out of lives. The correct word was " + word)
            break
        else:
            print("You have " + str(lives) + " lives left.")
            print("Your current correct letters are " + str(progress_list) + "\nYour incorrect letters are " + str(incorrect))
            guess = input("What is your guess?")

        if guess == word:
            output = word
            print("That's right! You win!")
            break
        elif len(guess) > 1 and guess != word or guess.isdigit() or len(guess) < 1:    # error checking
            print("Please guess one letter at a time")
            lives -= 1
        elif len(guess) == 1:
            list1 = progress(word, progress_list, guess)
            if list1 is None:
                print("\033[91m Sorry! There are no " + guess + "'s in the word! \033[0m")
                incorrect.append(guess)
                lives -= 1
                print_noose(lives)
        else:
            print("Incorrect")
            lives -= 1

    cont = input("Would you like to play again?(Y/N)")
    if cont.lower() == "y":
        game = True
    else:
        game = False



