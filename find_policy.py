import sys
import pickle
import os

def latex_print_policy(values,env_file):
	env = []
	for l in open(env_file).readlines():
		env += [[int(i) for i in l.strip().split(',')]]
	print "\\begin{center} \n \\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|} \n \hline"
	for i in range(12):
		# i  is the row
		# j  is the column
		row_policy = []
		
		for j in range(12):
			q = values[j*12+i]		
			prepend = ""
			if env[i][j] == 1:
				prepend = "\cellcolor{black!10}"
			elif env[i][j] == 2:
				prepend = "\cellcolor{black!30}"
			elif env[i][j] == 3:
				prepend = "\cellcolor{black!60}"
			elif env[i][j] == 4:
				prepend = "\cellcolor{red!50}"
			elif i in [5,6,10,11] and j == 0:
				prepend = "\cellcolor{yellow!40}"

			m = max(q)
			action = [['$\leftarrow$','$\\rightarrow$','$\uparrow$','$\downarrow$'][u] for u, v in enumerate(q) if v == m][0]
			row_policy += [prepend+action]
		print " & ".join(row_policy) + " \\\ \hline"
	print "\end{tabular}\n\end{center}"


def aggregate(folder, env, env_type = ""): 
	files = [f for f  in os.listdir(folder) if f.endswith(".p") and f.startswith(env_type)]
	answer = [[0,0,0,0] for i in xrange(144)]
	for f in files[0:1]:
		values = pickle.load(open(folder+f))
		for i in xrange(144):
			best = [j for j in xrange(4) if values[i][j] == max(values[i])][0]
			answer[i][best] += 1
	latex_print_policy(answer,env)






