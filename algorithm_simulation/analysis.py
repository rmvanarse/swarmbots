"""

Created by: Rishikesh Vanarse
04/05/2020

Python 3.5.2

Performs analysis on simulation results

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#Parameters:

CSV_PATH = "csv/"
NUM_BOTS = 20
NUM_SIMULATIONS = 30
TASK = "circle_r1-5"
METHOD = "centroid"
PREFIX = 'IGNORE__'

CSV_NAME = PREFIX+TASK+"-"+METHOD+"-"+str(NUM_BOTS)+"bots-"+str(NUM_SIMULATIONS)+"sims.csv"

PLOT = False
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


if __name__ == '__main__':
	result = Result(CSV_PATH+CSV_NAME)
	result.produce_stats()
	result.summary()

