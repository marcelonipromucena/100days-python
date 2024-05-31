print('''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '--'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              """"-""""""""""""""""""""""""""-""""''')

print('Welcome to Treasure Island')
print('Your mission is to find the treasure')

if input('left or right?') != 'left':
    print('Fall into a hole. Game Over')
else:
    if input('swim or wait') != 'wait':
        print('Attacked by trout. Game Over.')
    else:
        if input('which door? red, blue or yellow?') == 'red':
            print('Burned by fire. Game Over.')
        elif input('which door? red, blue or yellow?') == 'blue':
            print('Eaten by beasts. Game Over.')
        elif input('which door? red, blue or yellow?') == 'yellow':
            print('You win.')
        else:
            print('Game over.')


