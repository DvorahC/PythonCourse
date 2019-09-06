import random


class Numero_Secret:

    def set_up_computer_number(self):
        computer_number = [random.randint(1, 9) for _ in range(4)]
        print(computer_number)
        return computer_number

    def check_user_number(self, user_try, computer_solution):
        if user_try == computer_solution:
            return print('You win!')
        for i in range(len(user_try)):
            if user_try[i] == computer_solution[i]:
                print(f'You are good, you have some common digits, the number: {user_try[i]} in position: {i + 1}')
