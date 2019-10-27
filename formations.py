"""
Created by: Rishikesh Vanarse
27/10/19

formations.py

Contains functions for different formations 

"""

import numpy as np
import math

import swarm_lib as lib
import aggregation as aggr

"""
ARRANGE AT EQUAL DIST
"""

def formation_team(dist = 0.5):
	centroids_x, centroids_y = aggr.get_local_centroids()
	x_new = []
	y_new = []
	for i in range(len(lib.SWARM)):
		bot = lib.SWARM[i]
		remaining_dist = bot.distPt(centroids_x[i], centroids_y[i])
		x_step = (centroids_x[i] - bot.x)/remaining_dist
		y_step = (centroids_y[i] - bot.y)/remaining_dist

		x_goal = (bot.x + x_step * (remaining_dist-dist)/4)
		y_goal = (bot.y + y_step * (remaining_dist-dist)/4)

		lib.SWARM[i].goto_direct(x_goal, y_goal)

		x_new.append(x_goal)
		y_new.append(y_goal)

		"""
		Gives unexpected behaviour - Why?
		"""

	return (x_new, y_new)