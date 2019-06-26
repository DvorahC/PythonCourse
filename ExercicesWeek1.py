# 1Write a program that is asking to enter a number and is printing out if the number is odd or even
num = int(input('please enter a number: '))

if num % 2 == 0:
    print('this number is even')
else:
    print('this number is odd')

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

# 3 Write a program that receive a number from the user and print rows of asterisks that extend up to the number entered.

n = int(input('enter a number: '))


def star(n):
    for i in range(1, n + 1):
        print(i * "*")


star(n)

# 4  Write a program that receive a number from the user and print rows of asterisks that extend up to the number entered and added 2.

n1 = int(input('enter a number: '))


def function(n1):
    k = 2 * n1 - 2  # number of spaces
    
    for i in range(0, n1 + 3, 2): # the first loop defines the number of rows
        
        for j in range(1, k): # I understand that this loop is defining the spaces 
            print(j * " ")
        k = k - 2   # we remove 2 spaces at every run of the this loop
        
        for j in range(0, i +1): # this loop is doing the number of colums
            print("* ", end="")
   

        print("\r") # ending line after each row
    
    ## THE ISSUE IS THAT i DONT GET THE EXACT SPACING BETWEEN THE STARS

function(n1)


# 5
