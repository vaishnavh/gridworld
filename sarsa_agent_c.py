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



class sarsa_agent(Agent):
	randGenerator=Random()
	lastAction=Action()
	lastObservation=Observation()
	sarsa_stepsize = 0.4
	sarsa_epsilon = 0.1
	sarsa_gamma = 0.9
	episodeCount = 0
	numStates = 0
	numActions = 0
	value_function = None
	elig = None
	sarsa_lambda = float(sys.argv[1])
	
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
			
			self.value_function=[self.numActions*[0.0] for i in range(self.numStates)]
			self.elig=[self.numActions*[0.0] for i in range(self.numStates)]
			self.episodeCount = 0


		else:
			print "Task Spec could not be parsed: "+taskSpecString;
			
		self.lastAction=Action()
		self.lastObservation=Observation()
		
	def egreedy(self, state):
		maxIndex=0
		a=1
		if not self.exploringFrozen and self.randGenerator.random()<self.sarsa_epsilon:
			return self.randGenerator.randint(0,self.numActions-1)

                
		return self.value_function[state].index(max(self.value_function[state]))
		
		
	
	def agent_start(self,observation):
		self.elig=[self.numActions*[0.0] for i in range(self.numStates)]
		theState=observation.intArray[0]
		thisIntAction=self.egreedy(theState)
		returnAction=Action()
		returnAction.intArray=[thisIntAction]
		self.sarsa_epsilon = 0.15 + math.exp(-0.008*self.episodeCount)		
		#self.sarsa_stepsize = 0.05 + math.exp(-0.008*self.episodeCount)		
		#print self.sarsa_epsilon
		self.episodeCount += 1
		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)

		return returnAction
	
	def agent_step(self,reward, observation):
		
		newState=observation.intArray[0]
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]

		newIntAction=self.egreedy(newState)

		Q_sa=self.value_function[lastState][lastAction]
		Q_sprime_aprime=self.value_function[newState][newIntAction]

		delta = reward + self.sarsa_gamma*Q_sprime_aprime - Q_sa
		self.elig[lastState][lastAction] += 1
		for x in xrange(self.numStates):
			for a in xrange(4):
				self.value_function[x][a] += self.sarsa_stepsize * delta * self.elig[x][a]
				self.elig[x][a] = self.sarsa_gamma*self.sarsa_lambda*self.elig[x][a]
		#new_Q_sa=Q_sa + self.sarsa_stepsize * (reward + self.sarsa_gamma * Q_sprime_aprime - Q_sa)

		#if not self.policyFrozen:
		#	self.value_function[lastState][lastAction]=new_Q_sa

		returnAction=Action()
		returnAction.intArray=[newIntAction]
		
		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)

		return returnAction
	
	def agent_end(self,reward):
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]

		Q_sa=self.value_function[lastState][lastAction]

		delta = reward - Q_sa
		self.elig[lastState][lastAction] += 1
		for x in xrange(self.numStates):
			for a in xrange(4):
				self.value_function[x][a] += self.sarsa_stepsize * delta * self.elig[x][a]
				self.elig[x][a] = self.sarsa_gamma*self.sarsa_lambda*self.elig[x][a]



	
	def agent_cleanup(self):
		pass

	def save_value_function(self, fileName):
		theFile = open(fileName, "w")
		pickle.dump(self.value_function, theFile)
		theFile.close()

	def load_value_function(self, fileName):
		theFile = open(fileName, "r")
		self.value_function=pickle.load(theFile)
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

		if inMessage.startswith("reset_run"):
			self.episodeCount = 0
			print "Episode Reset."
			return "message understood, resetting run"
		return "SampleSarsaAgent(Python) does not understand your message."



if __name__=="__main__":
	AgentLoader.loadAgent(sarsa_agent())
