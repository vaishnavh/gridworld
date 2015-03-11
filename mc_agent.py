import random
import sys
import copy
import pickle
from rlglue.agent.Agent import Agent
from rlglue.agent import AgentLoader as AgentLoader
from rlglue.types import Action
from rlglue.types import Observation
from rlglue.utils import TaskSpecVRLGLUE3
from random import Random
import math

#SIZE=float(sys.argv[1])
STEP=float(sys.argv[1])

class mc_agent(Agent):
	randGenerator=Random()
	lastAction=Action()
	lastObservation=Observation()
	baseline = 0.0
	lastReturn = 0.0
	timeStep = 0
	mc_stepsize = STEP
	SIZE = 0.0
	
	mc_gamma = 0.9
	episodeCount = 0
	numStates = 0
	numActions = 0
	theta = None
	preferences = None
	delta = None
	curr_delta = None
	value_function = None
	
	policyFrozen=False
	exploringFrozen=False
	lastBatch = 0.0
	
	def agent_init(self,taskSpecString):
		TaskSpec = TaskSpecVRLGLUE3.TaskSpecParser(taskSpecString)
		if TaskSpec.valid:
			assert len(TaskSpec.getIntObservations())==1, "expecting 1-dimensional discrete observations"
			assert len(TaskSpec.getDoubleObservations())==0, "expecting no continuous observations"
			assert not TaskSpec.isSpecial(TaskSpec.getIntObservations()[0][0]), " expecting min observation to be a number not a special value"
			assert not TaskSpec.isSpecial(TaskSpec.getIntObservations()[0][1]), " expecting max observation to be a number not a special value"
			self.numStates=TaskSpec.getIntObservations()[0][1]+1;

			assert len(TaskSpec.getIntActions())==1, "expecting 1-dimensional discrete actions"
			assert len(TaskSpec.getDoubleActions())==0, "expecting no continuous actions"
			assert not TaskSpec.isSpecial(TaskSpec.getIntActions()[0][0]), " expecting min action to be a number not a special value"
			assert not TaskSpec.isSpecial(TaskSpec.getIntActions()[0][1]), " expecting max action to be a number not a special value"
			self.numActions=TaskSpec.getIntActions()[0][1]+1;
			
			self.episodeCount = 0.0
			self.value_function=[self.numActions*[0.0] for i in range(self.numStates)]
			self.theta = [self.numActions*[0.0] for i in range(24)]
			self.delta = [self.numActions*[0.0] for i in range(24)]
			self.curr_delta = [self.numActions*[0.0] for i in range(24)]
			self.preferences = [self.numActions*[0.25] for i in range(self.numStates)]
			self.baseline = 0.0
			self.lastBatch = 0.0

		else:
			print "Task Spec could not be parsed: "+taskSpecString;
			
		self.lastAction=Action()
		self.lastObservation=Observation()
		
		

	def softmax(self, state):
		pref = self.preferences[state]

		#print pref
		#pref = self.preferences(state)
		choose = self.randGenerator.random()
		for i in xrange(3):
			if choose <= pref[i]:
				return i
			choose -= pref[i]
		return 3


	
	def agent_start(self,observation):
		theState=observation.intArray[0]
		thisIntAction=self.softmax(theState)
		returnAction=Action()
		returnAction.intArray=[thisIntAction]
		self.curr_delta = [self.numActions*[0.0] for i in range(24)]
		#self.mc_stepsize = 0.05 + math.exp(-0.008*self.episodeCount)		
		#self.mc_stepsize = math.exp(-0.003*self.episodeCount) - 0.3
		self.episodeCount += 1
		#if self.episodeCount == 400:
		#	self.mc_stepsize/=2.0
		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)
		self.lastReturn = 0.0
		self.timeStep = 1.0

		return returnAction
	
	def agent_step(self,reward, observation):
		
		newState=observation.intArray[0]
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]
		self.lastReturn += reward*self.timeStep
		self.timeStep *= self.mc_gamma
		#Update delta for the appropiate parameters
		pref = self.preferences[lastState]
		row = lastState%12
		col = lastState/12
		for a in xrange(4):
			self.curr_delta[row][a] += (a == lastAction) - pref[a]
			self.curr_delta[col + 12][a] += (a == lastAction) - pref[a]

		newIntAction=self.softmax(newState)

		returnAction=Action()
		returnAction.intArray=[newIntAction]
		
		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)

		return returnAction
	
	def agent_end(self,reward):
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]


		self.lastReturn += reward*self.timeStep
		#Update delta for the appropiate parameters
		pref = self.preferences[lastState]

		row = lastState%12
		col = lastState/12
		factor = self.mc_stepsize*(self.lastReturn-self.baseline)
		for a in xrange(4):
			self.curr_delta[row][a] += (a == lastAction) - pref[a]
			self.curr_delta[col + 12][a] += (a == lastAction) - pref[a]
		self.delta = [[self.delta[i][a] + factor*self.curr_delta[i][a] for a in range(4)] for i in xrange(24)]
		self.lastBatch += self.lastReturn

	def force_end(self):
		factor = self.mc_stepsize*(self.lastReturn-self.baseline)
		self.delta = [[self.delta[i][a] + factor*self.curr_delta[i][a] for a in range(4)] for i in xrange(24)]
		self.lastBatch += self.lastReturn



	def update_preferences(self):
		for state in range(self.numStates):
			row = state%12
			col = state/12
			row_pref = self.theta[row]
			col_pref = self.theta[12 + col]
			pref = [math.exp(row_pref[i] + col_pref[i]) for i in xrange(4)]
			sum_pref = sum(pref)
			pref = [pref[i]/sum_pref for i in xrange(4)]
			self.preferences[state] = pref
	

	def force_reset(self):
		self.theta = [[self.theta[i][a]/2.0 for a in range(4)] for i in xrange(24)]
		self.update_preferences()
		



	def update_policy(self):
		#factor = self.mc_stepsize*(self.lastReturn-self.baseline)
		#print (factor, self.baseline)
		self.theta = [[self.theta[i][a] + self.delta[i][a] for a in range(4)] for i in xrange(24)]
		self.update_preferences()
		self.delta = [self.numActions*[0.0] for i in range(24)]
		self.baseline = 0.4*self.baseline +0.6*self.lastBatch/self.SIZE
		self.lastBatch = 0.0
		self.episodeCount += self.SIZE
		
		

	
	def agent_cleanup(self):
		pass

	def save_value_function(self, fileName):
		theFile = open(fileName, "w")
		pickle.dump(self.preferences, theFile)
		theFile.close()

	def load_value_function(self, fileName):
		theFile = open(fileName, "r")
		self.preferences=pickle.load(theFile)
		theFile.close()
	
	def agent_message(self,inMessage):
		
		#	Message Description
	 	# 'freeze learning'
		# Action: Set flag to stop updating policy
		#
		if inMessage.startswith("freeze learning"):
			self.policyFrozen=True
			return "message understood, policy frozen"

		#	Message Description
	 	# unfreeze learning
	 	# Action: Set flag to resume updating policy
		#
		if inMessage.startswith("unfreeze learning"):
			self.policyFrozen=False
			return "message understood, policy unfrozen"

		#Message Description
	 	# freeze exploring
	 	# Action: Set flag to stop exploring (greedy actions only)
		#
		if inMessage.startswith("freeze exploring"):
			self.exploringFrozen=True
			return "message understood, exploring frozen"

		#Message Description
	 	# unfreeze exploring
	 	# Action: Set flag to resume exploring (e-greedy actions)
		#
		if inMessage.startswith("unfreeze exploring"):
			self.exploringFrozen=False
			return "message understood, exploring frozen"

		#Message Description
	 	# save_policy FILENAME
	 	# Action: Save current value function in binary format to 
		# file called FILENAME
		#
		if inMessage.startswith("save_policy"):
			splitString=inMessage.split(" ");
			self.save_value_function(splitString[1]);
			print "Saved.";
			return "message understood, saving policy"


		if inMessage.startswith("update_policy"):
			splitString=inMessage.split(" ");
			self.update_policy()
			return ""
		#Message Description
	 	# load_policy FILENAME
	 	# Action: Load value function in binary format from 
		# file called FILENAME
		#
		if inMessage.startswith("load_policy"):
			splitString=inMessage.split(" ")
			self.load_value_function(splitString[1])
			print "Loaded."
			return "message understood, loading policy"
		
		if inMessage.startswith("set_batch_size"):
			splitString=inMessage.split(" ")
			self.SIZE = float(splitString[1])
			print "Setting size."
			return "message understood, setting size"

	
		if inMessage.startswith("force_end"):
			self.force_end()
			print "Forcing end"
			return "message understood, forcing an end"

	
		if inMessage.startswith("force_reset"):
			self.force_reset()
			print "Forcing reset"
			return "message understood, force resetting"

		#if inMessage.startswith("reset_run"):
		#	self.episodeCount = 0
		#	print "Episode Reset."
		#	return "message understood, resetting run"
		return "SampleSarsaAgent(Python) does not understand your message."



if __name__=="__main__":
	AgentLoader.loadAgent(mc_agent())
