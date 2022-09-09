

from words import *
from quordle import Quordle
from solver import Solver



class QSolver:
	def __init__(self):
		self.solvers = [Solver() for i in range(4)]
		for solver in self.solvers:
			solver.done = False


		self.done = lambda: all(solver.done for solver in self.solvers)
		self.guessed = {}



	def best_guess(self):
		if self.done():
			return

		g_scores = {}
		for solver in self.solvers:
			if solver.done:
				continue
			if len(solver.solutions) == 1:
				return solver.solutions[0]

			bg = solver.best_guess()
			g_score = 0
			for solver in self.solvers:
				x = solver.score_guess(bg)
				g_score += x
			g_scores[bg] = g_score

		best = min(g_scores, key=g_scores.get)
		return best



	def implement_guess(self, g, feedback):
		if self.done():
			return

		for solver,f in zip(self.solvers,feedback):
			if f not in FEEDBACKS:
				solver.done = True
				continue
			solver.implement_guess(g, f)
		self.guessed[g] = feedback



	def solve(self):
		for i in range(9):
			g = self.get_guess(i)
			f = self.get_feedback()
			self.implement_guess(g, f)
			if self.done():
				break
			print(self.best_guess())

		if self.done():
			print("You Win!")
		else:
			print("Uh Oh.")



	def get_guess(self, i):
		while True:
			g = input(f"Your Guess ({i+1}): ")
			if g in WORDS or g in OTHER:
				return g
			print("Invalid Guess")


	def get_feedback(self):
		feedback = []
		i = 0
		while len(feedback) < 4:
			if self.solvers[len(feedback)].done:
				feedback.append('     ')
				continue

			f = input(f"Feedback from word {len(feedback)+1}: ")

			if f in FEEDBACKS or f == '22222':
				feedback.append(f)
			else:
				print("Invalid Feedback")

		return feedback










if __name__ == '__main__':
	solver = QSolver()
	solver.solve()












