"""

Created by: Rishikesh Vanarse
04/05/2020

Python 3.5.2

Performs analysis on simulation results

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Parameters:

CSV_PATH = "csv/"
NUM_BOTS = 20
NUM_SIMULATIONS = 30
TASK = "circle_r1-5"
METHOD = "centroid"

CSV_NAME = TASK+"-"+METHOD+"-"+str(NUM_BOTS)+"bots-"+str(NUM_SIMULATIONS)+"sims.csv"

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

		self.score = None
		self.iterations = None
		self.success_rate = None
		

	def split_success_failure(self, df = self.df):
		"""
		Input: df to be split
		Creates 2 new dataframes for success and failures
		Returns: Success rate
		"""
		self.df_fail = df[df['Success']==False]
		self.df_success = df[df['Success']==True]

		return self.df_success.shape[0]/self.num_simulations


	
	def success_rate(self, df = self.df):
		self.success_rate =  df['Success'].mean()
		return self.success_rate

	

	def extra_info_stats(self, verbose=False):
		info_max = self.df[info].max()
		info_min = self.df[info].min()

		info_fail_avg = self.df_fail[info].mean()

		if(verbose):
			print("Max "+info+": "+str(info_max))
			print("Min "+info+": "+str(info_min))
			print("Mean "+info+" for failures: "+str(info_fail_avg))

		return info_min, info_max, info_fail_avg

	
	def mean_iter_to_success(self):
		iterations = self.df_success['Iterations'].mean()