"""

Created by: Rishikesh Vanarse
04/05/2020

Python 3.5.2

Run: python3 analysis.py <args>

Loads/Performs multiple simulations
(depending on cmdln arg: LOAD / SIMULATE)

Performs analysis on simulation results
Plots the results


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


#Parameters:

MIN_BOTS = 5
MAX_BOTS = 40
INCREMENT = 3

CSV_PATH = "csv/"
NUM_BOTS = 20
NUM_SIMULATIONS = 30

TASK = "circle_r1-5"
METHOD = "centroid"
PREFIX = 'IGNORE__n6--'

CSV_NAME = PREFIX+TASK+"-"+METHOD+"-"+str(NUM_BOTS)+"bots-"+str(NUM_SIMULATIONS)+"sims.csv"

PLOT = True
SAVE = False


#Class for result dataframe & functions - 

class Result:
	"""
	Result class;
	Contains the pd dataframe of the simulation results
	Contains different stats of the simulation
	Contains necessary functions on the df
	"""

	def __init__(self, path):
		self.df_raw = pd.read_csv(path)

		self.df = self.df_raw
		self.df_success = None
		self.df_fail = None

		self.num_simulations = self.df.shape[0]
		self.info = self.df.columns[4]

		self.score = None	#Includes failures
		self.iterations = None
		self.success_rate = None
		

	def split_success_failure(self):
		"""
		Input: df to be split
		Creates 2 new dataframes for success and failures
		Returns: Success rate
		"""
		df = self.df
		self.df_fail = df[df['Success']==False]
		self.df_success = df[df['Success']==True]

		return self.df_success.shape[0]/self.num_simulations


	
	def get_success_rate(self):
		self.success_rate =  self.df['Success'].mean()
		return self.success_rate

	

	def extra_info_stats(self, verbose=False):
		info_max = self.df[self.info].max()
		info_min = self.df[self.info].min()

		info_fail_avg = self.df_fail[self.info].mean()

		if(verbose):
			print("Max "+self.info+": "+str(info_max))
			print("Min "+self.info+": "+str(info_min))
			print("Mean "+self.info+" for failures: "+str(info_fail_avg))
			print("")

		return info_min, info_max, info_fail_avg

	
	def mean_iter_to_success(self):
		self.iterations = self.df_success['Iterations'].mean()
		return self.iterations

	def max_iter(self):
		return self.df['Iterations'].max()+1

	def get_score(self):
		self.score = self.df['Score'].mean()
		return self.score

	def produce_stats(self):
		self.split_success_failure()
		self.get_success_rate()
		self.mean_iter_to_success()
		self.max_iter()
		self.get_score()
		

	def summary(self):
		print("No. of simulations:\t", self.num_simulations)
		print("Max iterations:\t\t", self.max_iter())
		print("")
		print("Average score:\t\t", self.score)
		print("Success rate:\t\t", self.success_rate)
		print("Avg iter for success:\t", self.iterations)
		print("")
		self.extra_info_stats(verbose=True)
		return None


#FUNCTIONS:

def run_simulations(min_bots, max_bots, increment,
	num_sim, path=CSV_PATH):
	"""
	
	Runs simulations for different swarm sizes
	& saves the results as csv

	Input: 
		min_bots: Minimum number of robots
		max_bots: Maximum number of robots
		increment: Increment in successive swarm size
		num_sim: Number of simulations
		path: Path for storing csv files

	Returns: List of Result objects
	
	"""

	results = []

	for num_bots in range(min_bots, max_bots, increment):
		
		#Run
		args = str(num_bots)+' '+str(num_sim)+' '+path
		os.system('python3 simulate_gen_data.py '+args)
		
		#Load Results
		filename = PREFIX+TASK+"-"+METHOD+"-"+str(num_bots)+"bots-"+str(num_sim)+"sims.csv"
		r = Result(path+filename)
		results.append(r)

	return results


def load_simulations(min_bots, max_bots, increment,
	num_sim, path=CSV_PATH):
	"""
	Loads previously saved simulations
	Input: 
		min_bots: Minimum number of robots
		max_bots: Maximum number of robots
		increment: Increment in successive swarm size
		num_sim: Number of simulations
		path: Path of csv files
	
	Returns: List of Result objects

	"""
	results = []

	for num_bots in range(min_bots, max_bots, increment):
		filename = PREFIX+TASK+"-"+METHOD+"-"+str(num_bots)+"bots-"+str(num_sim)+"sims.csv"
		r = Result(path+filename)
		results.append(r)

	return results


#MAIN:

if __name__ == '__main__':

	results = []

	if 'SIMULATE' in sys.argv:
		results = run_simulations(MIN_BOTS, MAX_BOTS,
			INCREMENT, NUM_SIMULATIONS)
	elif 'LOAD' in sys.argv:
		results = load_simulations(MIN_BOTS, MAX_BOTS,
			INCREMENT, NUM_SIMULATIONS)
	else:

		result = Result(CSV_PATH+CSV_NAME)
		results.append(result)

	


	#Produce Stats
	for i in range(len(results)):
		print("\t---\t\n\n")
		results[i].produce_stats()
		results[i].summary()

	#TEST Plot
	if PLOT:
		x = np.arange(MIN_BOTS,MAX_BOTS,INCREMENT)

		
		"""MULTI_GRAPH BLOCK"""

		for i in range(3):
			PREFIX = "IGNORE__n"+str(i+4)+"--"
			results = load_simulations(MIN_BOTS, MAX_BOTS,
				INCREMENT, NUM_SIMULATIONS)
			for j in range(len(results)):
				print("\t---\t\n\n")
				results[j].produce_stats()
				results[j].summary()
			y = np.array([r.success_rate for r in results])
			plt.plot(x, y, label = "Neighbourhood R = "+str(i+4))
		
		"""  

		"""
		#plt.ylim((0,1.1))
		plt.title('Circle foration - Swarm size v/s Success rate')
		plt.xlabel('Number of robots')
		plt.ylabel('Success rate')
		plt.legend()
		plt.show()



"""
Formula used for score:

Aggregation:		1 / (0.7 + RMS_score)
Circle formation:	1 / (var_score + 1*neighbourhood_radius)

"""