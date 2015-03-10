import os
import sys

f = sys.argv[1]

output = open(sys.argv[1]+".corr","w")
f = open(f).readlines()[0].split(', ')
print len(f)

while len(f) > 499:
	nextOut = f[:499]
	f = f[499:]
	if len(nextOut[498]) <= 5:
		i = 2
	else:
		i = 3


	i=len(nextOut[498])-i
	f = [nextOut[498][-i:]] + f
	nextOut[498] = nextOut[498][:-i]
	output.write(", ".join(nextOut))
	output.write("\n")
output.write(", ".join(f))
output.close()


	
	

