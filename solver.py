from words import *
from wordle import Wordle

class Solver:
	def __init__(self):
		self.solutions = SOLUTIONS[:]
		self.guessed = {}



	def best_guess(self):
		g_scores = {}
		for g in WORDS:
			g_scores[g] = self.score_guess(g)
		
		w = best = min(g_scores, key=g_scores.get)
		while w not in self.solutions:
			g_scores[w] = float('inf')
			w = min(g_scores, key=g_scores.get)

		return best, w


	def score_guess(self, g):
		g_score = 0
		f_score = {'22222': 0}

		for a in self.solutions:
			f = self.feedback(g, a)
			if f not in f_score:
				f_score[f] = len(self.prune(g, f))
			g_score += f_score[f]
		return g_score


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

	

	def prune(self, g, f):
		pruned_answers = []
		for word in self.solutions:
			if f == self.feedback(g, word):
				pruned_answers.append(word)
		return pruned_answers



	def implement_guess(self, g, f):
		self.solutions = self.prune(g, f)
		self.guessed[g] = f
		return f



	def solve(self):
		for i in range(6):
			g = self.get_guess(i)
			f = self.get_feedback()
			if f == '22222':
				print("You Win!")
				break

			self.implement_guess(g, f)
			print(self.best_guess())

		if i == 6:
			print("Uh Oh.")


	def get_guess(self, i):
		while True:
			g = input(f"Your Guess ({i+1}): ")
			if g in WORDS or g in OTHER:
				return g
			print("Invalid Guess")


	def get_feedback(self):
		while True:
			f = input(f"Feedback: ")
			if f in FEEDBACKS or f == '22222':
				return f
			print("Invalid Feedback")




	def auto_solve(self, answer=None):
		wordle = Wordle(answer)

		g = 'raise' # self.best_guess()
		while not wordle.over:
			f = wordle.guess(g)
			print(g, f)

			self.implement_guess(g, f)
			g = self.best_guess()




if __name__ == '__main__':
	solver = Solver()
	solver.auto_solve()











