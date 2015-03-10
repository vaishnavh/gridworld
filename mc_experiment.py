
import sys
import math
import rlglue.RLGlue as RLGlue
import pickle
import os



#TODO
# Understand why start state has L
# Understand why top state has U

learning_type = sys.argv[1]
no_trials = int(sys.argv[2])
no_episodes = int(sys.argv[3])
batch_size = int(sys.argv[4])

def print_policy(policy_file):
	preferences = pickle.load(open(policy_file))

	policy = []
	for i in range(12):
		# i  is the row
		# j  is the column
		row_policy = []
		for j in range(12):
			pref = preferences[j*12 + i]
			m = max(pref)
			action = [['L','R','U','D'][u] for u, v in enumerate(pref) if v == m][0]
			row_policy += [action]
		policy += [row_policy]
	return policy

	
def run_learning(run_no, fileName):

	#Starting an episode
	taskSpec = RLGlue.RL_init()
	print("Running "+str(run_no))
	#We could run one step at a time instead of one episode at a time */
	#Start the episode */
	steps = []
	returns = []
	rewards = []
		
	for i in range(1,no_episodes):
		startResponse = RLGlue.RL_start()
		stepResponse = RLGlue.RL_step()
		#if startResponse.o.intArray[0] == 11 :
		#	print(startResponse.o.intArray[0],stepResponse.a.intArray[0],stepResponse.o.intArray[0])
		totalReturn = stepResponse.r
		totalReward = stepResponse.r

		gamma = 0.9
		x = 0
		while (stepResponse.terminal != 1):
		    stepResponse = RLGlue.RL_step()
		    totalReturn += gamma*stepResponse.r
		    totalReward += stepResponse.r

		    gamma = gamma*0.9
		    x+=1
		    #if x%1000 == 0:
		    #	    print x
		totalSteps = RLGlue.RL_num_steps()
		print (run_no, i,totalReturn,totalSteps)
		steps += [totalSteps]
		returns += [totalReturn]
		rewards += [totalReward]
		if i%batch_size == 0:
			RLGlue.RL_agent_message("update_policy");
	policy_file = learning_type+"_"+str(run_no)+".p"
	RLGlue.RL_agent_message("save_policy "+policy_file);
	policy = print_policy(policy_file)
	for row in policy:
		print (row)
	theFile = open(fileName+"_rewards.csv", "a");
	theFile.write(", ".join(map(str,rewards)))
	theFile.write("\n")
	theFile.close();
	
	theFile = open(fileName+"_return.csv", "a");
	theFile.write(", ".join(map(str,returns)))
	theFile.write("\n")
	theFile.close();
	theFile = open(fileName+"_steps.csv", "a");
	theFile.write(", ".join(map(str,steps)))
	theFile.write("\n")
	theFile.close();
	RLGlue.RL_cleanup()
	print(str(run_no)+" done")
	

if os.path.isfile(learning_type+"_return.csv"):
	sys.exit()
theFile = open(learning_type+"_return.csv","w")
theFile.close()
theFile = open(learning_type+"_steps.csv","w")
theFile.close()
for i in xrange(0,no_trials):
	run_learning(i, learning_type)
	


#TODO: Policy has to be printed
