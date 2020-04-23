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


"""
EVALUATION METRICS
"""

def state_count():
	"""
	Returns: A list of all states and their counts
	"""
	states_dict = {}

	for i in range(len(lib.SWARM)):
		state =  lib.SWARM[i].get_state()
		if state in states_dict:
			states_dict[state]+=1
		else:
			states_dict[state] = 1

	print(states_dict)
	return states_dict


def success():
	states_dict = state_count()
	return states_dict[max(states_dict)] == len(lib.SWARM)

def metric_ratio():
	"""
	(For 2 states only)
	Returns: ( Ratio (max:total) - 0.5 ) * 2
	"""
	states_dict = state_count()

	if len(states_dict) == 1:
		return 1.0
	else:
		return 2*(-0.5 + states_dict[max(states_dict)]/len(lib.SWARM))