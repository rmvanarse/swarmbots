import numpy as np

import swarm_lib as lib

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


def go_towards_centroid():
	pass

def go_to_centroid():
	(centroids_x, centroids_y) = get_local_centroids()
	for i in range(len(lib.SWARM)):
		lib.SWARM[i].goto_direct(centroids_x[i], centroids_y[i])
	return (centroids_x, centroids_y)
