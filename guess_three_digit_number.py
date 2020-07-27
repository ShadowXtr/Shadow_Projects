# To build a Python Guessing Game, The AI Guesses a random 3 digit number.
print('Your job is to keep guessing the 3 digit number until we find the correct one.')
print('According to your guess, the AI will let us know if we are Close, we have a Match or None.')
print()
print('Close --> A number we guessed is right but not in the correct position.')
print('Match --> A number we guessed is right and it is in the correct position.')
print('None  --> None of the above.')
print()
print('The Program will not end unless the number is guessed correctly.')
print()

import random

number_guessed = str(random.randint(100, 999))

def check_match(correct, guess):
	for i in range(3):
		if correct[i] == guess[i]: return True
	else: return False


def check_close(correct, guess):
	for i in range(10):
		if str(i) in correct and str(i) in guess: return True
	else: return False

if __name__ == '__main__':
	turns = 0
	while True:
		try:
			input_guess = input('What would be your Guess? ')
			if check_match(number_guessed, input_guess): print('Match')
			elif check_close(number_guessed, input_guess): print('Close')
			else: print('None')
			turns += 1

			if input_guess == number_guessed:
				print()
				print("Congratulations for Guessing Correct!")
				print("You took", turns, "turns to guess.")
				break
		except: pass
	input('Press Enter to Exit!')
