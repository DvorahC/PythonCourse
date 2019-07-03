
import re


count = 0
with open(r'C:\Users\wishtrip\Desktop\pythonRegex.txt') as listOfPasswords:
    for line in listOfPasswords:
        searchInLines = re.search(r'(\b[a-z]+\b)', line)
        count += 1

    print(f'{count} passwords are matching the request')
