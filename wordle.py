import random
from words import *




class Wordle():

	def __init__(self, answer=None):
		if answer in WORDS:
			self.answer = answer
		else:
			self.answer = real_world_wordle_word()
		self.over = False

	def random(self):
		self.answer = random.choice(WORDS)

	def guess(self, g):
		if self.over:
			return

		g = g.lower()
		if g == self.answer:
			self.over = True

		return(self.feedback(g, self.answer))

	def feedback(self, g, a):
		feedback = ''
		a = [c for c in a]
		for i in range(5):
			# print(i, g, a)
			if g[i] == a[i]:
				feedback += '2'
				a[i] = ' '
			elif g[i] in a:
				feedback += '1'
				j = a.index(g[i])
				a[j] = ' '
			else:
				feedback += '0'
		# print(feedback)
		return feedback



	def play(self):
		for i in range(6):
			guess = self.get_guess(i)
			print(self.guess(guess), '\n')
			if self.over:
				print("You Win")
				return

		print("You Lost :(")
		print("The Answer Was:". self.answer)


	def get_guess(self, i):
		while True:
			g = input(f"Your Guess ({i+1}): ")
			if g in WORDS or g in OTHER:
				return g
			print("Invalid Guess")



if __name__ == '__main__':
	wordle = Wordle()
	wordle.play()









