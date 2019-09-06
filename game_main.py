import pickle
from player import Player
from computer import Numero_Secret
import os.path


def play_the_game(joueur, ordinateur):
    number_of_set = 0
    a = ordinateur.set_up_computer_number()
    while number_of_set <= 20:
        number_of_set += 1
        b = joueur.set_up_user_number()
        ordinateur.check_user_number(b, a)
        if a == b:
            print(f'You had the correct number: {a}...You Won! Mazal Tov!')
            break
        elif a != b and number_of_set == 20:
            print(f'sorry...end of the game, you missed all your chances. The correct number was: {a}')
            break
        else:
            print(f'Round number: {number_of_set}, you have {20 - number_of_set} rounds to play!')


def get_to_next_move(secret_number, player_data, number_of_set):
    user_answer = input('If you want to save your game and come back later, type YES if not type NO: ')
    while True:
        if user_answer == 'YES':
            with open('saved_info', 'wb')as f:
                pickle.dump(secret_number, f)
                pickle.dump(player_data, f)
                pickle.dump(number_of_set, f)
                print(f'Your game is saved, it was your round number:{number_of_set}')
                return True
        else:
            return False


joueur1 = Player()
ordinateur1 = Numero_Secret()

print("Welcome!\n"
      "You are playing against the computer...\t"
      "Insert a number with 4 unique digits. You win if you picked the same number as the computer.\n"
      "You only have 20 trials.\n"
      "Some hints will be given to you as you are playing the game..."
      "Good Luck!")


while True:
    play_the_game(joueur1, ordinateur1)
    if get_to_next_move(b, a, number_of_set) and os.path.isfile('PythonGame/saved_info'):
        with open('saved_info', 'rb') as f:
            b = pickle.load(ordinateur1.secret_number, f)
            a = pickle.load(joueur1.player_data, f)
            number_of_set = pickle.load(number_of_set, f)
    else:
        continue


