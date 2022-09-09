######################################################
'''
This solver file is a work in progress.



'''
#######################################################

from datetime import *
from words import *
from wordle import Wordle
import json
import sys



class Solver:
	def __init__(self, answer=None):
		self.solutions = SOLUTIONS
		if not answer:
			self.answer = real_world_wordle_word()
		else:
			self.answer = answer


		self.guesses_made = []
		self.g_letters = set()
		self.y_letters = set()
		self.b_letters = set()

	def score_guess(self, g):
		g_score = 0
		f_score = {'22222': 0}
		for a in self.solutions:
			f = self.feedback(g, a)
			if f not in f_score:
				f_score[f] = len(self.prune(g, f))
			g_score += f_score[f]
		return g_score#/len(self.solutions)

	def best_guess(self):
		g_scores = {}
		for g in WORDS:
			g_scores[g] = self.score_guess(g)
		best = min(g_scores, key=g_scores.get)

		# Find Ties
		sorted_keys = sorted(g_scores, key=g_scores.get)
		ties = []
		x = sorted_keys[0]
		for k in sorted_keys:
			ratio = g_scores[k]/g_scores[x]
			if ratio < 1.45:
				ties.append(k)
			else:
				break
		# Get Lucky
		print(f'Finding Lucky: {ties} {len(ties)}')
		lucky = self.get_lucky(ties)

		return best, lucky

	def get_lucky(self, guesses):
		print("Getting Lucky")
		if len(guesses) == 1:
			start = datetime.now()
			guesses = self.generate_lucky_guesses(guesses[0])
			stop = datetime.now()
			print(f'{len(guesses)}: {stop-start}')

		a = self.answer
		# b, f, g, j, k, m, q, v, x, y, z
		best_p = float('inf')
		best_g = guesses[0]
		for g in guesses:
			f = self.feedback(g,a)
			if f == '22222':
				return g
			p = self.prune(g,f)
			# print(g,a,f,s,len(p))
			if len(p) < best_p:
				best_p = len(p)
				best_g = g
		return best_g

	def generate_lucky_guesses(self, g):
		print("Generating Lucky:", g)
		guesses = second_guesses
		lc = self.count_letters()

		g_score = self.score_guess(g)
		gl_score = self.score_letters(g, lc)
		gf = self.feedback(g, self.answer)
		gp = len(self.prune(g, gf))

		x = []
		start = datetime.now()
		for word in WORDS:
			if any(c in word for c in self.b_letters):
				continue
			
			f = self.feedback(word, g)
			f = self.sum_feedback(f)
			if f < 1:
				continue

			ls = self.score_letters(word, lc)
			if ls < gl_score/2:
				continue

			clue = self.feedback(word, self.answer)
			p = len(self.prune(word, clue))
			if p < gp:
				x.append((word,f,ls))

		stop = datetime.now()
		print(f"Getting Words ({len(x)}): {stop-start}")

		x.sort(key=lambda i: (i[1],i[2]), reverse=True)

		start = datetime.now()
		y = []
		for word,f,ls in x:
			w_score = self.score_guess(word)
			if w_score/g_score < 1.45:
				guesses.append(word)
			y.append((word, w_score, f, ls, w_score/g_score))
		stop = datetime.now()
		print(f"Scoring Words ({len(x)*len(self.solutions)}): {stop-start}")

		y.sort(key=lambda i: i[1])
		for t in y:
			print(t)

		return guesses

	def sum_feedback(self, f):
		x = 0
		for c in f:
			x += int(c)
		return x

	def count_letters(self):
		letter_count = {}
		for word in self.solutions:
			for c in word:
				if c in letter_count:
					letter_count[c] += 1
				else:
					letter_count[c] = 1
		return letter_count

	def score_letters(self, word, letter_count):
		lc = dict(letter_count)
		ls = 0
		for c in word:
			if c not in lc:
				continue
			if c in self.y_letters:
				ls += lc[c]
				lc[c] = 0
			elif c not in self.g_letters:
				ls += lc[c]*2
				lc[c] = 0
		return ls

	def prune(self, guess, clues):
		pruned_answers = []
		for word in self.solutions:
			if clues == self.feedback(guess, word):
				pruned_answers.append(word)
		return pruned_answers

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


	def implement_guess(self, g):
		f = self.feedback(g, self.answer)
		self.solutions = self.prune(g, f)

		# Tracking Data
		self.guesses_made.append(g)
		self.color_letters(g, f)

	def color_letters(self, g, f):
		for c,x in zip(g,f):
			if x == '0':
				self.b_letters.add(c)
			elif x == '1':
				self.y_letters.add(c)
			elif x == '2':
				self.g_letters.add(c)
				self.y_letters.discard(c)










