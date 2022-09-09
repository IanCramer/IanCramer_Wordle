import random
from words import *
from wordle import Wordle
from solver import Solver




class Quordle:
	def __init__(self, answers=[]):
		if type(answers) is not list or \
			len(answers) != 4 or \
			any(x not in WORDS for x in answers):
				answers = [random.choice(WORDS) for i in range(4)]

		self.wordles = [Wordle(answer) for answer in answers]
		self.answers = lambda: [wordle.answer for wordle in self.wordles]


	def over(self):
		for wordle in self.wordles:
			if not wordle.over:
				return False
		return True


	def answer(self):
		return [wordle.answer for wordle in self.wordles]


	def guess(self, g):
		if self.over():
			return
		
		g = g.lower()

		feedback = []
		for wordle in self.wordles:
			f = wordle.guess(g)
			if f == '22222':
				feedback.append('Done!')
			elif f:
				feedback.append(f)
			else:
				feedback.append('     ')

		return feedback



	def play(self):
		for i in range(9):
			g = self.get_guess(i)
			feedback = self.guess(g)
			for f in feedback:
				print(f, end='\t')
			print()
			if self.over():
				print("You Win!")
				return

		print("You Lost :(")
		print("The Answer Was:", game.answer())


	def get_guess(self, i):
		while True:
			g = input(f"Your Guess ({i+1}): ")
			if g in WORDS or g in OTHER:
				return g
			print("Invalid Guess")







if __name__ == '__main__':
	game = Quordle()
	game.play()







