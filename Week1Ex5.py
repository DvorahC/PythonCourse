# 5 Le programme recevra deux numéros et une action (addition, soustraction, multiplication, division ou possession)
# de l'utilisateur et
# imprimera le résultat de l'opération sur les deux numéros.
# Notez que si l’utilisateur n’a pas saisi d’entrées valides, vous devez l’informer poliment et demander des entrées supplémentaires.


while True:

    try:
        n1 = int(input('Please enter a first number:'))
        break
    except Exception:
        print("You did not enter a number, please try again")

while True:
    try:
        n2 = int(input('Please enter a second number:'))
        break
    except Exception:
        print("You did not enter a number, please try again: ")
        

def calculation(number1, number2, operation):
    if operation == '+':
        total = number1 + number2
    elif operation == '-':
        total = number1 - number2
    elif operation == '/':
        total = number1 / number2
    elif operation == '*':
        total = number1 * number2
    else:
        raise Exception('Error')
    return print(total)


while True:
    try:
        operator = input('Please enter which operation you want to do between those 2 numbers: +, -, / or *: ')
        calculation(n1, n2, operator)
        break
    except Exception:
        print("the operator is not valid, please try again")
