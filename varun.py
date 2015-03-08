# 
# Copyright (C) 2008, Brian Tanner
# 
#http://rl-glue-ext.googlecode.com/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#  $Revision: 1011 $
#  $Date: 2009-02-11 22:29:54 -0700 (Wed, 11 Feb 2009) $
#  $Author: brian@tannerpages.com $
#  $HeadURL: http://rl-library.googlecode.com/svn/trunk/projects/packages/examples/mines-sarsa-python/sample_sarsa_agent.py $

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


# This is a very simple Sarsa agent for discrete-action, discrete-state
# environments.  It uses epsilon-greedy exploration.
# 
# We've made a decision to store the previous action and observation in 
# their raw form, as structures.  This code could be simplified and you
# could store them just as ints.


# TO USE THIS Agent [order doesn't matter]
# NOTE: I'm assuming the Python codec is installed an is in your Python path
#   -  Start the rl_glue executable socket server on your computer
#   -  Run the SampleMinesEnvironment and SampleExperiment from this or a
#   different codec (Matlab, Python, Java, C, Lisp should all be fine)
#   -  Start this agent like:
#   $> python sample_sarsa_agent.py

class sarsa_agent(Agent):
	randGenerator=Random()
	lastAction=Action()
	lastObservation=Observation()
	sarsa_stepsize = 0.05
	sarsa_epsilon = 0.1
	sarsa_gamma = 0.9
	numStates = 0
	numActions = 0
	value_function = None
	row_parameters = None
	row_updates = None
	column_parameters = None
	column_updates = None
	discounting=1.0
	trajectory_return = 0.0
	policyFrozen=False
	exploringFrozen=False
	updateDone=False

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
			self.row_parameters=[self.numActions*[0.0]  for i in range(12)]
			self.column_parameters=[self.numActions*[0.0]  for i in range(12)]
			self.row_updates=[self.numActions*[0.0]  for i in range(12)]
			self.column_updates=[self.numActions*[0.0]  for i in range(12)]		
			self.trajectory_return=0.0
			self.discounting=1.0
			updateDone=False

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
	
	def chooseSoftMax(self,state):
		row=state/12
		column=state%12
		preferences=[0.0 for i in range(self.numActions)]
		for i in range(self.numActions):
			preferences[i]=self.row_parameters[row][i]+self.column_parameters[column][i]
		chosenAction=self.returnSoftMax(preferences)
		return chosenAction

	def getSoftMaxPreferences(self,state):
		row=state/12
		column=state%12
		preferences=[0.0 for i in range(self.numActions)]
		for i in range(self.numActions):
			preferences[i]=self.row_parameters[row][i]+self.column_parameters[column][i]
		preferences=[math.exp(preference) for preference in preferences]
		preferenceSum=sum(preferences)
		preferences=[preference/preferenceSum for preference in preferences]
		return preferences

	def returnSoftMax(self,preferences):
		preferences=[math.exp(preference) for preference in preferences]
		preferenceSum=sum(preferences)
		preferences=[preference/preferenceSum for preference in preferences]
		runningSum=0.0
		randomDraw=random.random()
		chosenIndex=0
		for i in range(len(preferences)):
			if randomDraw<runningSum+preferences[i]:
				chosenIndex=i
				break
			else:
				runningSum+=preferences[i]	
		return chosenIndex
	
	def agent_start(self,observation):
		if not self.updateDone:
			for rowNum in range(12):
				for i in range(self.numActions):
					self.row_parameters[rowNum][i]+=self.sarsa_stepsize*self.trajectory_return*self.row_updates[rowNum][i]
					self.row_updates[rowNum][i]=0.0

			for columnNum in range(12):
				for i in range(self.numActions):
					self.column_parameters[columnNum][i]+=self.sarsa_stepsize*self.trajectory_return*self.column_updates[columnNum][i]
					self.column_updates[columnNum][i]=0.0

			self.discounting=1.0
			self.trajectory_return=0.0
			#print self.row_parameters
			#print "Update Done"
		self.updateDone=False
		theState=observation.intArray[0]
		thisIntAction=self.chooseSoftMax(theState)
		preferences=self.getSoftMaxPreferences(theState)
		returnAction=Action()
		returnAction.intArray=[thisIntAction]
		
		theRow=theState/12
		theColumn=theState%12
		for i in range(self.numActions):
			if i==thisIntAction:
				self.row_updates[theRow][i]+=1-preferences[i]
				self.column_updates[theColumn][i]+=1-preferences[i]
			else:
				self.row_updates[theRow][i]+=-preferences[i]
				self.column_updates[theColumn][i]+=-preferences[i]
		

		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)

		#self.trajectory_return+=reward*self.discounting
		self.discounting*=self.sarsa_gamma
		return returnAction
	
	def agent_step(self,reward, observation):
		newState=observation.intArray[0]
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]

		newIntAction=self.chooseSoftMax(newState)
		preferences=self.getSoftMaxPreferences(newState)

		theRow=newState/12
		theColumn=newState%12
		for i in range(self.numActions):
			if i==newIntAction:
				self.row_updates[theRow][i]+=(1-preferences[i])
				self.column_updates[theColumn][i]+=(1-preferences[i])
			else:
				self.row_updates[theRow][i]+=-preferences[i]
				self.column_updates[theColumn][i]+=-preferences[i]
		
		
		returnAction=Action()
		returnAction.intArray=[newIntAction]
		
		self.lastAction=copy.deepcopy(returnAction)
		self.lastObservation=copy.deepcopy(observation)

		self.trajectory_return+=reward*self.discounting
		self.discounting*=self.sarsa_gamma
		return returnAction
	
	def agent_end(self,reward):
		lastState=self.lastObservation.intArray[0]
		lastAction=self.lastAction.intArray[0]

		#Update parameters, set them to zero
		for rowNum in range(12):
			for i in range(self.numActions):
				self.row_parameters[rowNum][i]+=self.sarsa_stepsize*self.trajectory_return*self.row_updates[rowNum][i]
				self.row_updates[rowNum][i]=0.0
	
		for columnNum in range(12):
			for i in range(self.numActions):
				self.column_parameters[columnNum][i]+=self.sarsa_stepsize*self.trajectory_return*self.column_updates[columnNum][i]
				self.column_updates[columnNum][i]=0.0

		self.discounting=1.0
		self.trajectory_return=0.0
		self.updateDone=True
		#print self.row_parameters
		#print "Update Done"

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

		return "SampleSarsaAgent(Python) does not understand your message."



if __name__=="__main__":
	AgentLoader.loadAgent(sarsa_agent())
