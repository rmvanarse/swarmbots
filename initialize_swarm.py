"""
Created By: Rishikesh Vanarse
26/10/19

initialize_swarm.py

Contains: Different initialization methods for a swarm

"""
import random

import swarm_lib

DEFAULT_X_RANGE=10
DEFAULT_Y_RANGE =10


def random_initializer(num_bots, x_range=DEFAULT_X_RANGE, y_range=DEFAULT_Y_RANGE, origin = (0,0), verbose=False):
	for i in range(num_bots):
		xpos = origin[0] + random.random()*x_range
		ypos = origin[1] + random.random()*y_range
		theta = random.random()*3.1415926*2
		bot = swarm_lib.Bot(xpos, ypos, theta)

	if(verbose):
		for bot in swarm_lib.SWARM:
			bot.print_state()

"""
if __name__ == "__main__":
	random_initializer(10, verbose=True)
	swarm_lib.show_swarm()


	print("Random Tests:\n")
	#swarm_lib.SWARM[3].neighbours()[0].print_state()

"""