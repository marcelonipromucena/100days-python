import random


word_list = ['ardvark', 'baboon', 'camel']

display = []

chosen_word = random.choice(word_list)

guess = input('Guess a letter: ').lower()

for _ in range(len(chosen_word)):
    display += '_'

print(display)


for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')