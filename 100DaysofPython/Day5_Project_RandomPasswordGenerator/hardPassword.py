import random
from ref import letters,symbols,numbers
print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n"))
symb = int(input(f"How many symbols would you like?\n"))
numb = int(input(f"How many numbers would you like?\n"))
password_list=[]
for char in range(0,let):
    password_list.append(random.choice(letters))
for number in range(0,numb):
    password_list.append((random.choice(numbers)))
for symbol in range(0,symb):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print("You password is:",password)