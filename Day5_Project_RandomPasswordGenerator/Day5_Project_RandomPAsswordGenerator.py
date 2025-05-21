import random
from ref import letters,symbols,numbers
print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n"))
symb = int(input(f"How many symbols would you like?\n"))
numb = int(input(f"How many numbers would you like?\n"))
password = ""
for char in range(0, let):
    password += random.choice(letters)

for char in range(0, symb):
    password += random.choice(symbols)

for char in range(0, numb):
    password += random.choice(numbers)

print("Your password is :" ,password)