import pickle

def print_policy(values):
	
	policy = []
	for i in range(12):
		# i  is the row
		# j  is the column
		row_policy = []
		for j in range(12):
			q = values[j*12+i]		
			m = max(q)
			action = [['L','R','U','D'][u] for u, v in enumerate(q) if v == m][0]
			print (i,j,action)
			row_policy += [action]
		policy += [row_policy]
	return policy
	
			
