import re


class Player:

    def __init__(self):

        def set_up_user_number(self):
            while True:
                user_number = input('enter a 4 digits number: ')
                if verify_number_format(user_number):
                    user_numbers_to_list = [int(digit) for digit in user_number]
                    print(f'Your number: {user_numbers_to_list}')
                    return user_numbers_to_list
                else:
                    continue

        def verify_number_format(self):
            if re.match(r'^\d{4}$', self) and not re.match(r'(\d).*\1', self):
                return True
            else:
                print("This is not 4 digits number without repetition...Try again.")
                return False
