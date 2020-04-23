"""
Created by: Rishikesh Vanarse
22/04/20

Version: Python 3.5.2

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
import decision_making as decisions

#Parameters
TASK_FUNC = aggr.go_towards_centroid
SUCCESS = aggr.success
INFO_FUNC = aggr.num_clusters
METRIC = aggr.metric_rms


TASK = "aggr"
METHOD = "centroid"
EXTRA_INFO = "Num Clusters"

NUM_BOTS = 10
ITERATIONS = 130
NUM_SIMULATIONS = 30

CSV_PATH = "csv/"
#CSV_NAME = f"{TASK}-{METHOD}-iter{ITERATIONS}-sims{NUM_SIMULATIONS}.csv"
CSV_NAME = TASK+"-"+METHOD+"-"+str(NUM_BOTS)+"bots-"+str(NUM_SIMULATIONS)+"sims.csv"
SAVE = True




#Initialize swarm
sw.random_initializer_with_state(NUM_BOTS, verbose=True)
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
"""
for i in range(ITERATIONS):
	TASK_FUNC()
	if(not i%5):
		print("Iter ",i, "\tClusters: ", aggr.num_clusters())
	if SUCCESS():
		print("\nSuccess at iter: ", i,"\n\n")
		break
if(not SUCCESS()):
	print("\n\nFailed")
"""




"""
Main
"""

if __name__ == "__main__":
	df = pd.DataFrame(columns = [
		'Simulation', 
		'Iterations', 
		'Success',
		'Score',
		EXTRA_INFO
		])

	for _id in range(NUM_SIMULATIONS):

		sw.random_initializer_with_state(NUM_BOTS, verbose=False)

		for i in range(ITERATIONS):
			TASK_FUNC()
			
			if SUCCESS():
				print("Simulation", _id, "Success at iter: ", i)
				break

		if(not SUCCESS()):
			print("Simulation", _id,"Failed")

		df_temp = pd.DataFrame({
					'Simulation':[_id+1],
					'Iterations':[i],
					'Success':[str(SUCCESS())],
					'Score':[METRIC()],
					EXTRA_INFO: [INFO_FUNC()]
					})


		df = df.append(df_temp, ignore_index = True, sort=False)
	print("\n\n", df)

	if(SAVE):
		df.to_csv(CSV_PATH+CSV_NAME, index=False)