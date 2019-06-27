# 2 Write a program that is receiving 3 numbers from the user and is checking if one of
# the numbers is the sum of the 2 other numbers

number1 = int(input('Please enter a first number: '))
number2 = int(input('Please enter a second number: '))
number3 = int(input('Please enter a third number: '))
if number1 == number2 + number3:
    print(f'{number1} is the sum of {number2} and {number3}')
elif number2 == number1 + number3:
    print(f'{number2} is the sum of {number1} and {number3}')
elif number3 == number1 + number2:
    print(f'{number3} is the sum of {number1} and {number2}')
else:
    print('none of the 3 numbers is the sum of the other 2')