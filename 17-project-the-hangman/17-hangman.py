import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

game_over = False

correct_letters = []

lives = 6

print(logo)

while not game_over:
    guess = input('Guess a letter: ').lower()

    word_length = len(chosen_word)

    display = ""

    if guess in correct_letters:
        print(f'You have already guessed {guess}.')

    if guess not in chosen_word:
        print(f'The letter {guess} is not part of the word.')

    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You lose! The correct word was', chosen_word)

    print(display)


    if "_" not in display:
        game_over = True
        print('You win! The correct word is: ',chosen_word)

    print(stages[lives])

    print(f'######### You have {lives} left. #########')