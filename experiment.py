
import sys
import math
import rlglue.RLGlue as RLGlue

# TO USE THIS Experiment [order doesn't matter]
# NOTE: I'm assuming the Python codec is installed an is in your Python path
#   -  Start the rl_glue executable socket server on your computer
#   -  Run the SampleSarsaAgent and SampleMinesEnvironment from this or a
#   different codec (Matlab, Python, Java, C, Lisp should all be fine)
#   -  Start this environment like:
#   $> python sample_experiment.py

# Experiment program that does some of the things that might be important when
# running an experiment.  It runs an agent on the environment and periodically
# asks the agent to "freeze learning": to stop updating its policy for a number
# of episodes in order to get an estimate of the quality of what has been learned
# so far.
#
# The experiment estimates statistics such as the mean and standard deviation of
# the return gathered by the policy and writes those to a comma-separated value file
# called results.csv.
#
# This experiment also shows off some other features that can be achieved easily
# through the RL-Glue env/agent messaging system by freezing learning (described
# above), having the environment start in specific starting states, and saving
# and loading the agent's value function to/from a binary data file.




#
#	This function will freeze the agent's policy and test it after every 25 episodes.
#
def run_learning(run_no, fileName):

	#Starting an episode
	taskSpec = RLGlue.RL_init()
	#We could run one step at a time instead of one episode at a time */
	#Start the episode */
	steps = []
	returns = []
	for i in range(1,20):
		startResponse = RLGlue.RL_start()
		stepResponse = RLGlue.RL_step()
		totalReturn = stepResponse.r
		gamma = 0.9
		x = 0
		while (stepResponse.terminal != 1):
		    stepResponse = RLGlue.RL_step()
		    totalReturn += gamma*stepResponse.r
		    gamma = gamma*0.9
		    if x == 3000:
			    break;
		    x+=1
		    
		totalSteps = RLGlue.RL_num_steps()
		
		print (i,totalReturn,totalSteps)
		steps += [totalSteps]
		returns += [totalReturn]
		
	theFile = open(fileName+"_return.csv", "w");
	theFile.write(", ".join(map(str,returns)))
	theFile.write("\n")
	theFile.close();
	theFile = open(fileName+"_steps.csv", "w");
	theFile.write(", ".join(map(str,steps)))
	theFile.close();
	RLGlue.RL_cleanup()
	

for i in xrange(0,50):
	run_learning(i, "q_learning")
	


#TODO: Policy has to be printed
