"""
Created by: Rishikesh Vanarse
27/10/19

formations.py

Contains functions for different formations 

"""

RADIUS = 1.5
SUCCESS_VAR = 0.002


import numpy as np
import math

import swarm_lib as lib
import aggregation as aggr

"""
ARRANGE AT EQUAL DIST
"""

def formation_team(dist = RADIUS):
	centroids_x, centroids_y = aggr.get_local_centroids()
	x_new = []
	y_new = []
	for i in range(len(lib.SWARM)):
		bot = lib.SWARM[i]
		remaining_dist = bot.distPt(centroids_x[i], centroids_y[i])
		x_step = (centroids_x[i] - bot.x)/max(0.0001, remaining_dist)
		y_step = (centroids_y[i] - bot.y)/max(0.0001, remaining_dist)

		x_goal = (bot.x + x_step * (remaining_dist-dist)/4)
		y_goal = (bot.y + y_step * (remaining_dist-dist)/4)

		lib.SWARM[i].goto_direct(x_goal, y_goal)

		x_new.append(x_goal)
		y_new.append(y_goal)

		"""
		Gives unexpected behaviour - Why?
		"""

	return (x_new, y_new)



"""
EVALUATION METRICS
"""

def metric_variance():
	x_sum=0
	y_sum=0
	n = len(lib.SWARM)
	for bot in lib.SWARM:
		x_sum+=bot.x
		y_sum+=bot.y
	centroid = x_sum/n , y_sum/n

	dist_list = []
	for bot in lib.SWARM:
		dist_list.append(bot.distPt(centroid[0], centroid[1]))

	return np.array(dist_list).var()/RADIUS



def success():
	return metric_variance()<SUCCESS_VAR


def true_radius():
	x_sum=0
	y_sum=0
	n = len(lib.SWARM)
	for bot in lib.SWARM:
		x_sum+=bot.x
		y_sum+=bot.y
	centroid = x_sum/n , y_sum/n

	dist_sum=0
	for bot in lib.SWARM:
		dist_sum+=bot.distPt(centroid[0], centroid[1])

	return dist_sum/n

