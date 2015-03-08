import sys
import pickle
import os

def latex_print_policy(values):
	for i in range(12):
		# i  is the row
		# j  is the column
		row_policy = []
		
		for j in range(12):
			q = values[j*12+i]		
			m = max(q)
			action = [['\leftarrow','\\rightarrow','\uparrow','\downarrow'][u] for u, v in enumerate(q) if v == m][0]
			row_policy += [action]
		print " & ".join(row_policy) + " \\\ \hline"


def aggregate(folder): 
	files = [f for f  in os.listdir(folder) if f.endswith(".p")]
	print files
	answer = [[0,0,0,0] for i in xrange(144)]
	print answer
	for f in files[0:1]:
		values = pickle.load(open(folder+f))
		for i in xrange(144):
			best = [j for j in xrange(4) if values[i][j] == max(values[i])][0]
			answer[i][best] += 1
	latex_print_policy(answer)






