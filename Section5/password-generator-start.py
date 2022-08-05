#Password Generator Project
import random
from re import L
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_list = []
for _ in range(0, nr_letters):
    random_letter = random.randint(0, len(letters) - 1)
    letters_list.append(letters[random_letter])

symbols_list = []
for _ in range(0, nr_symbols):
    random_symbol = random.randint(0, len(symbols) - 1)
    symbols_list.append(symbols[random_symbol])

number_list = []
for _ in range(0, nr_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    number_list.append(numbers[random_number])

password_list = letters_list + symbols_list + number_list
print(password_list)
shuffled = random.sample(password_list, len(password_list))
print(shuffled)
password = "".join(shuffled)

print(f"Your password is: {password}")

# Another way to do it

password2 = ""
for char in range(1, nr_letters +1):
    password2 += random.choice(letters)

for char in range(1, nr_symbols +1):
    password2 += random.choice(symbols)

for char in range(1, nr_numbers +1):
    password2 += random.choice(numbers)

print(password2)

password2_list = list(password2)
print(password2_list)
random.shuffle(password2_list)
new_password = "".join(password2_list)
print(f"Your password is: {new_password}")