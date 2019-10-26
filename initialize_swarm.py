"""
Created By: Rishikesh Vanarse
26/10/19
"""
import random

import swarm_lib

DEFAULT_X_RANGE=10
DEFAULT_Y_RANGE =10


def random_initializer(num_bots, x_range=DEFAULT_X_RANGE, y_range=DEFAULT_Y_RANGE, origin = (0,0)):
	for i in range(num_bots):
		xpos = origin[0] + random.random()*x_range
		ypos = origin[1] + random.random()*y_range
		theta = random.random()*3.1415926*2
		swarm_lib.SWARM.append(swarm_lib.Bot(xpos, ypos, theta))