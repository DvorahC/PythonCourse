# 4  Write a program that receive a number from the user and print rows of asterisks that extend up to the number entered and added 2.
n1 = int(input('enter a number: '))


def function(n1):
    k = 2 * n1 - 2  # number of spaces

    for i in range(0, n1 + 3, 2):  # the first loop defines the number of rows

        for j in range(0, k):  # I understand that this loop is defining the spaces
            print(end=" ")
        k = k - 2  # we remove 2 spaces at every run of the this loop

        for j in range(0, i + 1):  # this loop is doing the number of colums
            print("* ", end="")

        print("\r")  # ending line after each row

    ## THE ISSUE IS THAT i DONT GET THE EXACT SPACING BETWEEN THE STARS


function(n1)