import re


class Player:

    def __init__(self):
        pass

    def set_up_user_number(self):
        while True:
            user_number = input('enter a 4 digits number: ')
            if self.verify_number_format(user_number):
                user_numbers_to_list = [int(digit) for digit in user_number]
                print(f'Your number: {user_numbers_to_list}')
                return user_numbers_to_list
            else:
                continue

    def verify_number_format(self, n):
        if re.match(r'^\d{4}$', n) and not re.match(r'(\d).*\1', n):
            return True
        else:
            print("This is not 4 digits number without repetition...Try again.")
            return False


