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
import matplotlib.pyplot as plt

DEFAULT_NEIGHBOURHOOD_VAL = 5

#DEFAULT_NEIGHBOURHOOD_VAL = 5 #Radius of neighbourhood 
DEFAULT_SIZE = 0.5 #Radius of chassis
MAX_SPEED = 1.5
STEP = 0.2	#Used in aggr

DEFAULT_XRANGE = 10	#Used in simulation limits
DEFAULT_YRANGE =10



SWARM =[] #List of all bots in the swarm

class Bot:

	def __init__(self, x,y, theta=0, state= 'stop', neighbourhood_radius = DEFAULT_NEIGHBOURHOOD_VAL):
		self.x = float(x)
		self.y = float(y)
		self.theta = theta
		self.state = state
		self.neighbourhood_radius = neighbourhood_radius
		SWARM.append(self)

	def get_state(self):
		return self.state

	def distPt(self, x_pt, y_pt):
		return math.sqrt((self.x-x_pt)**2+(self.y-y_pt)**2)

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

	def goto_direct(self, x_new, y_new):
		#Updates x,y
		self.x = x_new
		self.y = y_new

	def print_state(self):
		print("BOT " +str(SWARM.index(self)))
		print("Position: "+ str(self.x)+ ","+str(self.y))
		print("Direction: "+str(self.theta))
		print("State: "+str(self.state))
		print("")


def dummy():
	return None

def swarm_size():
	return len(SWARM)
#Show bots in pyplot

def show_swarm():
	x_list = [bot.x for bot in SWARM]
	y_list = [bot.y for bot in SWARM]
	plt.scatter(x_list, y_list)
	plt.show()


