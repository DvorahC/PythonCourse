# 3 Write a program that receive a number from the user and print rows of asterisks that extend up to the number entered.

n = int(input('enter a number: '))


def star(n):
    for i in range(1, n + 1):
        print(i * "*")


star(n)