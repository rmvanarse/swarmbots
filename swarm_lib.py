"""

Created: 24/06/19
Last Updated: 24:06/19


Library for general classes and functions for swarm simulation
Import this file for simulations

Functions need to be added and optimized
"""

import numpy as np


DEFAULT_NEIGHBOURHOOD_VAL = 5 #Radius of neighbourhood 

SWARM =[] #List of all bots in the swarm

class Bot:

	def __init__(self, x,y, state= 0, neighbourhood_radius = DEFAULT_NEIGHBOURHOOD_VAL):
		self.x = x
		self.y = y
		self.state = state
		self.neighbourhood_radius = neighbourhood_radius
		SWARM.apeend(self)

	def dist(self, bot):
		return np.sqrt(np.square(self.x - bot.x) + np.square(self.y, bot.y))


