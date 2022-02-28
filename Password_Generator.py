import random

print("Welcome to my Password Generator")

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,?'

number = input("Enter amount of passwords needed: ")

number = int(number)

length = input("Enter password length: ")
length = int(length)

print('\nHere are the password(s)')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)
    print(passwords)
