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


class mc_agent(Agent):
	randGenerator=Random()
	lastAction=Action()
	lastObservation=Observation()
	baseline = 0.0
	mc_stepsize = 0.4
	mc_epsilon = 0.1
	mc_gamma = 0.9
	episodeCount = 0
	numStates = 0
	numActions = 0
	theta = None
	delta = None
	value_function = None
	
	policyFrozen=False
	exploringFrozen=False
	
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
			self.theta = [self.numAction*[0.0] for i in range(24)]
			self.baseline = 0.0

		else:
			print "Task Spec could not be parsed: "+taskSpecString;
			
		self.lastAction=Action()
		self.lastObservation=Observation()
		
	'''
	def get_row(self,state):
		return state%12

	def get_col(self,state):
		return int(state/12)


	def preferences(self, state):
		row = state%12
		col = state/12
		row_pref = self.theta[row]
		col_pref = self.theta[12 + col]
		pref = [math.exp(row_pref[i] + col_pref[i]) for i in xrange(4)]
		sum_pref = sum(pref)
		pref = [pref/sum_pref for i in xrange(4)]
		return pref
	'''
		

	def softmax(self, state):
		row = state%12
		col = state/12
		row_pref = self.theta[row]
		col_pref = self.theta[12 + col]
		pref = [math.exp(row_pref[i] + col_pref[i]) for i in xrange(4)]
		sum_pref = sum(pref)
		pref = [pref/sum_pref for i in xrange(4)]
		#pref = self.preferences(state)
		choose = self.randGenerator.random()
		for i in xrange(4):
			if choose <= pref[i]:
				return i
			choose -= pref[i]
		return 3


	
	def agent_start(self,observation):
		theState=observation.intArray[0]
		thisIntAction=self.softmax(theState)
		returnAction=Action()
		returnAction.intArray=[thisIntAction]
		self.delta = [self.numAction*[0.0] for i in range(24)]
		self.mc_epsilon = 0.1 + math.exp(-0.008*self.episodeCount)		
		self.mc_stepsize = 0.05 + math.exp(-0.008*self.episodeCount)		
		self.episodeCount += 1
		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)

		return returnAction
	
	def agent_step(self,reward, observation):
		
		newState=observation.intArray[0]
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]

		#Update delta for the appropiate parameters
		row = lastState % 12
		col = lastState / 12
		for a in xrange(4):
			self.delta[row][a] += (a == lastAction) - self.theta[row][a]
			self.delta[col + 12][a] += (a == lastAction) - self.theta[col + 12][a]

		newIntAction=self.softmax(newState)

		returnAction=Action()
		returnAction.intArray=[newIntAction]
		
		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)

		return returnAction
	
	def agent_end(self,reward):
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]

		#Update delta for the appropiate parameters
		row = lastState % 12
		col = lastState / 12
		for a in xrange(4):
			self.delta[row][a] += (a == lastAction) - self.theta[row][a]
			self.delta[col + 12][a] += (a == lastAction) - self.theta[col + 12][a]
		Q_sa=self.value_function[lastState][lastAction]

	def update_policy(self, lastReturn):
		factor = self.mc_stepsize*(lastReturn - self.baseline)
		self.theta = [self.theta[i] + factor*self.delta[i] for i in xrange(24)]
		self.baseline = (self.baseline*self.episodeCount + lastReturn)/episodeCount

	
	def agent_cleanup(self):
		pass

	def save_value_function(self, fileName):
		theFile = open(fileName, "w")
		pickle.dump(self.theta, theFile)
		theFile.close()

	def load_value_function(self, fileName):
		theFile = open(fileName, "r")
		self.theta=pickle.load(theFile)
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
			self.update_policy(float(splitString[1]))
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

		#if inMessage.startswith("reset_run"):
		#	self.episodeCount = 0
		#	print "Episode Reset."
		#	return "message understood, resetting run"
		return "SampleSarsaAgent(Python) does not understand your message."



if __name__=="__main__":
	AgentLoader.loadAgent(mc_agent())
