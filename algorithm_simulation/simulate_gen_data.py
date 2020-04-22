"""
Created by: Rishikesh Vanarse
22/04/20

Runs multiple simulations of a given task,
Saves results as CSV


"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import swarm_lib as lib
import initialize_swarm as sw
import aggregation as aggr
import formations
import area_coverage as coverage
import line_formation as lf


#Parameters
TASK_FUNC = aggr.go_towards_centroid
SUCCESS = aggr.success
METRIC = None

TASK = "aggr"
METHOD = "centroid"

NUM_BOTS = 20
ITERATIONS = 150
NUM_SIMULATIONS = 30

CSV_PATH = ""
#CSV_NAME = f"{TASK}-{METHOD}-iter{ITERATIONS}-sims{NUM_SIMULATIONS}.csv"
CSV_NAME = TASK+"-"+METHOD+"-iter"+str(ITERATIONS)+"-sims"+str(NUM_SIMULATIONS)+".csv"

#Initialize swarm
sw.random_initializer(NUM_BOTS, verbose=True)
x_list = [bot.x for bot in lib.SWARM]
y_list = [bot.y for bot in lib.SWARM]


#Helper functions
def random_generator():
  return (np.random.rand(len(lib.SWARM)), np.random.rand(len(lib.SWARM)))


"""

LOOP:

Reinitializes environment NUM_SIMULATIONS no. of times
Runs ITERATIONS iterations
Uses METRIC to analyze completion/quality of task
Fills the dataframe with: --> Decide!!
Saves the csv

"""




#Aggregation test:
#Basic structure of general code
#Remove later

for i in range(ITERATIONS):
	TASK_FUNC()
	if(not i%5):
		print("Iter ",i, "\tClusters: ", aggr.num_clusters())
	if SUCCESS():
		print("\nSuccess at iter: ", i,"\n\n")
		break
if(not SUCCESS()):
	print("\n\nFailed")