import random as r

letters = ['A', 'B', 'C', 'D' 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

n_letters = int(input('How many letters do you want inside your password?\n'))
n_numbers = int(input('How many numbers do you want inside your password?\n'))
n_symbols = int(input('How many symbols do you want inside your password?\n'))

CHOICE = int(input('Do you want 1. basic password generator or 2. random?\n'))
def p_gen(letters, numbers, symbols, n_letters, n_numbers, n_symbols):
    password = ''
    for i in range(0, n_letters):
        password += r.choice(letters)
    for i in range(0, n_numbers):
        password += r.choice(numbers)
    for i in range(0, n_symbols):
        password += r.choice(symbols)
    print(password)    
def r_p_gen(letters, numbers, symbols, n_letters, n_numbers, n_symbols):
    password = ''
    password = r.choice(letters) + r.choice(numbers) + r.choice(symbols)
    for i in range(n_letters - 1):
        password += r.choice(letters)
    for i in range(n_numbers - 1):
        password += r.choice(numbers)
    for i in range(n_symbols - 1):
        password += r.choice(symbols)
    print(password)
if CHOICE == 1:
    p_gen(letters, numbers, symbols, n_letters, n_numbers, n_symbols)
elif CHOICE == 2:
    r_p_gen(letters, numbers, symbols, n_letters, n_numbers, n_symbols)
else:
    r_p_gen(letters, numbers, symbols, n_letters, n_numbers, n_symbols)