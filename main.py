from datetime import *
from words import *
from wordle import Wordle
import json
import sys
from solver import Solver

def auto_solver(x=0):
	try:
		f = open('SolverTree.json', 'r')
		s_dict = json.load(f)
		f.close()
	except:
		pass

	if x in SOLUTIONS:
		a = x
		print("Using given word:", x)
	else:
		a = real_world_wordle_word(int(x))

	s = Solver(a)
	g = 'raise'

	# Solve it
	i = 1
	while g != a:
		h = s.feedback(g, a)
		s.implement_guess(g)
		n = len(s.solutions)
		if (x != 'tries'):
			print(f'{i}: {g}\t{h}\t{n}')
		i += 1

		if n == 1:
			g = s.solutions[0]
			print()
			break

		if n <= 10 and x != 'tries':
			print(s.solutions)

		try:
			# Attempt a faster method by parsing json
			x = 0/0
			s_dict = s_dict[g][h]
			best = list(s_dict.keys())[0]
			lucky = s.get_lucky([best])
			print("Used JSON")
		except:
			# If parsing json didn't work, compute best next guess
			print("JSON Failed")
			best, lucky = s.best_guess()
			print("Used Algorithm")

		if x != 'tries':
			print(f'best: {best}\tlucky: {lucky}')
		g = lucky
		print()

	if x == 'tries':
		print(i)
	else:
		print(f'Answer: {g}\t{i} tries')


def main():
	# '''
	f = open('SolverTree.json', 'r')
	s_dict = json.load(f)
	f.close()

	s = Solver()
	guesses = []
	while len(guesses) < 6:
		g = input("Your Guess: ")
		h = input("Hint Received: ")

		s.implement_guess(g)

		n = len(s.solutions)
		if n == 0:
			print("Something Went Wrong")
			quit()
		elif n == 1:
			print(f"The solution  is {s.solutions[0]} in {len(guesses)+2} tries.")
			break
		elif n == 2:
			print(f"There are {len(s.solutions)} possible solutions:\n", s.solutions)
			print(f"The lucky guess is {real_world_wordle_word()}")
			break
		elif len(s.solutions) <= 25:
			print(f"There are {len(s.solutions)} possible solutions:\n", s.solutions)
		else:
			print(f"There are {len(s.solutions)} possible solutions left")

		# Guess sucessfully made, log it
		guesses.append((g,h))

		# Get Best Guess
		try:
			# Attempt a faster method by parsing json
			s_dict = s_dict[g][h]
			best = list(s_dict.keys())[0]
			print("JSON")
		except:
			# If parsing json didn't work, compute best next guess
			best = s.best_guess()
			print("Computed")

		# Show Best Guess
		print("The best next guess is: ", best)




if __name__ == '__main__':
	main()