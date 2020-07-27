from os import system, name
import random

def clear_output():
	if name == 'nt': _ = system('cls')
	else: _ = system('clear')

clear_output()
print("This algorithm will generate Random 16-digit Credit Card Numbers (No Company Specific)")
print("The purpose of this piece of code is to test E-commerce websites which")
print("require a Credit Card Number to be inputted to check if the website")
print("is functioning properly on valid and invalid CC inputs")
print("These are completely fake and the Date and CVV number can be anything")
print()
print("Press Enter to Generate a Number, Press 'NO' to Stop the program.")
choice = input()

def check_luhn(cc_number):
	dictionary = dict(zip(range(0,10), [0,2,4,6,8,1,3,5,7,9]))
	for i in range(0, len(cc_number), 2):
		cc_number[i] = dictionary[cc_number[i]]
	if sum(cc_number) % 10 == 0: return True
	else: return False

while choice == '':
	cc_number = [random.randint(0,9) for _ in range(15)]
	changed_number = cc_number[::-1]
	dictionary = dict(zip(range(0,10), [0,2,4,6,8,1,3,5,7,9]))
	for i in range(0, len(changed_number), 2):
		changed_number[i] = dictionary[changed_number[i]]
	last_digit = (10-(sum(changed_number)%10))%10
	cc_number.append(last_digit)
	# check = check_luhn(cc_number)
	cc_number = "".join([str(x) for x in cc_number])

	# This line of code is used only for visualising the credit card number in 4 parts.
	cc_number = cc_number[0:4]+'-'+cc_number[4:8]+'-'+cc_number[8:12]+'-'+cc_number[12:16]
	clear_output()
	print("This Program is used to Generate a Random 16-digit Credit Card Number (No Company Specific)")
	print(cc_number)
	print()
	print("Press Enter to Generate a Number, Press 'NO' to Stop the program.")
	choice = input()
