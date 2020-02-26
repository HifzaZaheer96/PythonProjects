#!/usr/bin/env python3.8

calculation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

first_number = int(input('Please Enter your first number: '))
second_number = int(input('Please Enter your second number: '))

if calculation == '+':
    print('{} + {} = '.format(first_number, second_number))
    print(first_number + second_number)

elif calculation == '-':
    print('{} - {} = '.format(first_number, second_number))
    print(first_number - second_number)

elif calculation == '*':
    print('{} * {} = '.format(first_number, second_number))
    print(first_number * second_number)

elif calculation == '/':
    print('{} / {} = '.format(first_number, second_number))
    print(first_number / second_number)

else:
    print('You have not typed a valid operator, please run the program again.')
