'''
Write a Python program in which a player can play a hit against the computer. 
The computer selects a random 4-digit number (no repetition, which means a digit can appear only once)
and 
then the player has to guess the number. 
After every guess the computer writes:
- how many "stamps" were: how many digits were in the right place
- how many "vulnerabilities" were: how many digits are part of the secret number but do not appear in the right place.
The player has 20 guesses until the game ends.
Bonus - Allow "save" a game to file and exit the game, and then the next play will continue from that point.
'''

import random
import pickle
import re

print("Welcome!\n"
      "You are playing against the computer...\t"
      "Insert a number with 4 digits. You win if you picked the same number as the computer.\n"
      "You only have 20 trials.\n"
      "Some hints will be given to you as you are playing the game..."
      "Good Luck!")


# GET THE USER NUMBER AND CONVERT IT INTO A LIST OF DIGITS
def set_up_user_number():
    user_number = input('enter a 4 digits number: ')
    if verify_number_format(user_number):
        user_numbers_to_list = [int(digit) for digit in user_number]
        print(f'Your number: {user_numbers_to_list}')
        return user_numbers_to_list


def verify_number_format(n):
    if re.match(r"(\d{4})", n):
        return True
    else:
        print("This is not 4 digits number...Try again.")
        return False


# DEFINE RANDOM COMPUTER NUMBER INTO A LIST
def set_up_computer_number():
    computer_number = [random.randint(1, 9) for _ in range(4)]
    print(computer_number)
    return computer_number


# DEFINE THE FUNCTION TO CHECK THE NUMBER OF THE USER VS THE NUMBER OF THE COMPUTER
def check_user_number(user_try, computer_solution):
    if user_try == computer_solution:
        return print('You win!')
    for i in range(len(user_try)):
        if user_try[i] == computer_solution[i]:
            print(f'You are good, you have some common digits, the number: {user_try[i]} in position: {i + 1}')


def play_the_game():
    number_of_set = 0
    a = set_up_computer_number()
    while number_of_set <= 20:
        number_of_set += 1
        b = set_up_user_number()
        check_user_number(b, a)
        if a == b:
            print(f'You had the correct number: {a}...Try to improve your score next time!')
            break
        elif a != b and number_of_set == 20:
            print(f'sorry...end of the game, you missed all your chances. The correct number was: {a}')
            break
        else:
            print(f'Round number: {number_of_set}, you have {20 - number_of_set} rounds to play!')
            # keep_on_playing = input('Do you want to keep on playing? Yes or No: ')
            # if keep_on_playing == 'No':
            # with open('saved_user_number', 'wb')as f:
            # pickle.dump(b, f)
            # print(f'user number saved: {b}')
            # break
            # else:
            # continue


play_the_game()
