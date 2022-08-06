import random
from words import *




class Wordle():

	def __init__(self):
		self.answer = random.choice(WORDS)
		self.over = False

	def guess(self, g):
		if self.over:
			return

		g = g.lower()
		if g == self.answer:
			self.over = True
			print("You Win!")

		print(self.feedback(g))

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


def main():
	game = Wordle()

	for i in range(6):
		guess = input("Your Guess: ")
		game.guess(guess)
		print()
		if game.over:
			return

	print("You Lost :(")
	print("The Answer Was:". game.answer)

if __name__ == '__main__':
	g = Wordle()
	guess = input("Guess: ")
	g.guess(guess)
	
	main()