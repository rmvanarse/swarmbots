import numpy as np
import math

import swarm_lib as lib

def agreement_2state():
	"""
	States: 'stop' and 'A'
	Returns: List of new states of all bots

	"""
	new_states=[]
	for bot in lib.SWARM:
		grp = bot.neighbours()
		num1=0
		for nb in grp:
			if nb.state == 'stop':
				num1+=1
		if num1>=(len(grp)-num1):
			new_states.append('stop')
		else:
			new_states.append('A')

	for i in range(len(lib.SWARM)):
		lib.SWARM[i].state = new_states[i]

	return new_states