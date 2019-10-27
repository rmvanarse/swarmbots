"""
Created By: Rishikesh Vanarse
27/10/19

area_coverage.py
Contains: Algorithms for different kinds of area coverage

Constraints:
Functions applied to lib.SWARM by default
Output of all functions is a tuple of 2 lists, (x_list, y_list)
for new x and y coordinates of all bots

"""

DEFAULT_X_RANGE = 10
DEFAULT_Y_RANGE = 10

import numpy as np
import math

import swarm_lib as lib

"""
POTENTIAL FIELD BASED
"""

def AC_potentialField(k=0.3, width = DEFAULT_X_RANGE, height = DEFAULT_Y_RANGE, origin =(0,0)):
	"""
	Bots move away from neighbours & walls with inverse proportion to dist
	Assumption: Rectangular area

	Arguments:
	origin - tuple (x,y) denoting bottom left corner
	k = constant for potential field formula

	Method: 
	1) Add up vectors corresponding to all neighbours and walls
	2) Subtract final vectors from current x & y
	3) Goto new x & y and append lists x_new & y_new

	Returns: Tuple of Lists (x_new, y_new)

	"""
	x_new = []
	y_new = []
	for bot in lib.SWARM:
		grp = bot.neighbours()
		x_vec, y_vec = 0,0
		for nb in grp:
			dist = bot.dist(nb)
			xcap = (nb.x - bot.x)/dist
			ycap = (nb.y - bot.y)/dist

			x_vec-= k*xcap/(dist**2)
			y_vec-= k*ycap/(dist**2)

		x_vec-=k/((DEFAULT_X_RANGE-bot.x)**2)
		x_vec+=k/((origin[0]-bot.x)**2)

		y_vec-=k/((DEFAULT_Y_RANGE-bot.y)**2)
		y_vec+=k/((origin[1]-bot.y)**2)

		x_new.append(bot.x+ x_vec)
		y_new.append(bot.y+ y_vec)

	for i in range(len(lib.SWARM)):
		lib.SWARM[i].goto_direct(x_new[i], y_new[i])

	return (x_new, y_new)