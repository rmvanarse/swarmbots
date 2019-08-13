"""
Rishikesh Vanarse

Created: 24/06/19
Last Updated: 25/06/19


Library for general classes and functions for swarm simulation
Import this file for simulations

Functions need to be added and optimized
"""

import numpy as np
import math

DEFAULT_NEIGHBOURHOOD_VAL = 5 #Radius of neighbourhood 
DEFAULT_SIZE = 0.5 #Radius of chassis
MAX_SPEED = 1.5



SWARM =[] #List of all bots in the swarm

class Bot:

	def __init__(self, x,y, theta=0, state= 0, neighbourhood_radius = DEFAULT_NEIGHBOURHOOD_VAL):
		self.x = float(x)
		self.y = float(y)
		self.theta = theta
		self.state = state
		self.neighbourhood_radius = neighbourhood_radius
		SWARM.append(self)

	def dist(self, bot):
		return math.sqrt((bot.x - self.x)**2 + (bot.y - self.y)**2)

	def neighbours(self):
		neighbours =[]
		for b in SWARM:
			if b.dist(self) < self.neighbourhood_radius and b != self:
				neighbours.append(b)
		return neighbours

	def group(self):
		grp = self.neighbours()
		grp.append(self)
		return grp

