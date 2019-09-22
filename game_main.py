import pickle
from PythonGame.player import Player
from PythonGame.computer import SecretNumber
import os.path


def load_data_from_file(filename):
    if os.path.isfile('/Users/deborahchabbat/PycharmProjects/pycourse/PythonGame/saved_info'):
        with open(filename, 'rb') as f:
            player_data = pickle.load(f)
            secret_number = pickle.load(f)
            number_of_set = pickle.load(f)
            f.close()
            return secret_number, player_data, number_of_set


def play_the_game(player, computer):
    number_of_set = 0
    try:
        computer, player, number_of_set = load_data_from_file('saved_info')
    except FileNotFoundError:
        pass
        a = computer.set_up_computer_number()
        while number_of_set <= 20:
            number_of_set += 1
            b = player.set_up_user_number()
            computer.check_user_number(b, a)
            if get_to_next_move(b, a, number_of_set):
                break
            else:
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
            with open('saved_info', 'wb')as file:
                pickle.dump(secret_number, file)
                pickle.dump(player_data, file)
                pickle.dump(number_of_set, file)
                file.close()
                print(f'Your game is saved, it was your round number: {number_of_set}')
                return True
        else:
            return False


player1 = Player()
computer1 = SecretNumber()

print("Welcome!\n"
      "You are playing against the computer...\t"
      "Insert a number with 4 unique digits. You win if you picked the same number as the computer.\n"
      "You only have 20 trials.\n"
      "Some hints will be given to you as you are playing the game..."
      "Good Luck!")

play_the_game(player1, computer1)



