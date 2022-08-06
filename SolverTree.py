'''
This file will create a tree for solving any wordle word.
'''
import sys
import json
from words import *

class SolverTree:
	def __init__(self, ans=WORDS):
		self.ans = ans
		self.word = self.best_guess(ans)
		self.children = {}

		if len(ans) > 1:
			self.make_children(ans)

	def make_children(self, ans):
		for f in FEEDBACKS:
			pruned = self.prune(self.word, f, ans)
			if len(pruned) > 0:
				self.children[f] = SolverTree(pruned)


	def best_guess(self, ans):
		g_scores = {}
		for g in WORDS:
			g_scores[g] = self.score_guess(g, ans)
		return min(g_scores, key=g_scores.get)

	def score_guess(self, g, ans):
		g_score = 0
		f_score = {}
		for f in FEEDBACKS:
			f_score[f] = len(self.prune(g, f, ans))

		for a in ans:
			f = self.feedback(g, a)
			if f != '22222':
				g_score += f_score[f]
		return g_score/len(ans)

	def prune(self, g, f, ans):
		pruned = []
		for a in ans:
			if f == self.feedback(g, a):
				pruned.append(a)
		return pruned

	def feedback(self, g, a):
		feedback = ['', '', '', '', '']
		a = [c for c in a]
		for i in range(5):
			if g[i] == a[i]:
				feedback[i] = '2'
				a[i] = ' '
		for i in range(5):
			if feedback[i]:
				continue
			if g[i] in a:
				feedback[i] = '1'
				j = a.index(g[i])
				a[j] = ' '
			else:
				feedback[i] = '0'
		return ''.join(feedback)

	def show(self, depth=1):
		print(self.word, end=f' ({depth})\n')
		for c in self.children:
			print('\t'*depth, end=f'{c}: ')
			self.children[c].show(depth+1)

	def write(self, file, depth=1):
		file.write(f'{self.word} ({depth})\n')
		for c in self.children:
			tabs = '\t'*depth
			file.write(f'{tabs}{c}: ')
			self.children[c].write(file, depth+1)

	def make_json(self):
		if len(self.children) == 0:
			return self.word
		sub_dict = {}
		for c in self.children:
			sub_dict[c] = self.children[c].make_json()

		return {self.word: sub_dict}


def make_file():
	if len(sys.argv) < 2:
		print("Need file to write to.")
		return

	if '.txt' in sys.argv[1]:
		filename = sys.argv[1]
		f = open(filename, 'x')
		tree = SolverTree(WORDS[:5])
		tree.write(f)
		f.close()
	else:
		print("Takes filename.txt as second arguement.")
		return


def main():
	# make_file()
	tree = SolverTree()
	j = json.dumps(tree.make_json(), indent=4)
	print(j)

if __name__ == '__main__':
	main()