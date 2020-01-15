import numpy as np
import math

import swarm_lib as lib

"""

PRELIMINARIES

"""
DEFAULT_X_RANGE = lib.DEFAULT_XRANGE
DEFAULT_Y_RANGE = lib.DEFAULT_YRANGE




"""
CENTROID BASED:

"""

def get_local_centroids():
	"""
	Returns: Tuple of 2 lists: centroids_x, centroids_y
	Each corresponding emelent gives coordinates of the centroid of the
	neighbourhood of each bot.
	"""
	centroids_x =[]
	centroids_y =[]
	for bot in lib.SWARM:
		grp = bot.group()
		n = len(grp)
		centroids_x.append(sum([b.x for b in grp])/n)
		centroids_y.append(sum([b.y for b in grp])/n)
	return (centroids_x, centroids_y)


def go_to_centroid():
	"""
	Returns: (centroids_x, centroids_y)
	Same as get_local_centroids, but additionally updates the position of the bots,
	by calling swarm_lib.goto_direct()
	"""
	(centroids_x, centroids_y) = get_local_centroids()
	for i in range(len(lib.SWARM)):
		lib.SWARM[i].goto_direct(centroids_x[i], centroids_y[i])
	return (centroids_x, centroids_y)



def go_towards_centroid(step_size = lib.STEP, pid=True):
	"""
	Arguments: step_size - max size of a single step
	pid: smaller steps are proportional to remaining distance  

	Use: Every bot takes a single step in the direction of the local centroid
	Returns: (new_x, new_y)
	Calls: get_local_centroids() and swarm_lib.goto_direct

	*optimization needed
	
	"""
	centroids_x, centroids_y = get_local_centroids()
	x_new = []
	y_new = []
	for i in range(len(lib.SWARM)):
		bot = lib.SWARM[i]
		remaining_dist = bot.distPt(centroids_x[i], centroids_y[i])
		x_step = (centroids_x[i] - bot.x)/remaining_dist
		y_step = (centroids_y[i] - bot.y)/remaining_dist

		x_goal = (bot.x + x_step * step_size)
		y_goal = (bot.y + y_step * step_size)

		lib.SWARM[i].goto_direct(x_goal, y_goal)

		x_new.append(x_goal)
		y_new.append(y_goal)

		# PID Part NOT implemeted yet

	return (x_new, y_new)



"""
POTENTIAL FIELD BASED

"""

def aggr_potentialField(k=0.1, width = DEFAULT_X_RANGE, height = DEFAULT_Y_RANGE, origin =(0,0)):
	"""
	Bots move towards neighbours & away from walls with inverse proportion to dist
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

			MAX_VEC = dist/20


			x_vec+= min(k*xcap/(dist**2), MAX_VEC)
			y_vec+= min(k*ycap/(dist**2), MAX_VEC)

		x_vec-=k/((DEFAULT_X_RANGE-bot.x)**2)
		x_vec+=k/((origin[0]-bot.x)**2)

		y_vec-=k/((DEFAULT_Y_RANGE-bot.y)**2)
		y_vec+=k/((origin[1]-bot.y)**2)

		x_new.append(bot.x+ x_vec)
		y_new.append(bot.y+ y_vec)

	for i in range(len(lib.SWARM)):
		lib.SWARM[i].goto_direct(x_new[i], y_new[i])

	return (x_new, y_new)