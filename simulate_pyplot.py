import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import swarm_lib as lib
import initialize_swarm as sw


#Initialize swarm
sw.random_initializer(10, verbose=True)
x_list = [bot.x for bot in lib.SWARM]
y_list = [bot.y for bot in lib.SWARM]

#Initialize figure
fig, ax = plt.subplots()
bot_points, = ax.plot(x_list, y_list, 'o')

#Set Limits (ToDo)

#Helper functions
def random_generator():
	return (np.random.rand(len(lib.SWARM)), np.random.rand(len(lib.SWARM)))

#-----------------------
#UPDATION:

"""
- Different 'update functions' will be imported from a header

- 'task_func' will be set to the required update function, eg:aggr_centroid

- Return type of each call of tassk_func should be the next goalpoints for all bots;
  i.e. a tuple of 2 lists: new x_list and new  y_list

- The 'data' argument of 'update' the default output from 
  the 'generate_points' function.

- 'task_func' call resides in the 'generate_points' function. 

"""
def update(data):
    bot_points.set_ydata(data[1])
    bot_points.set_xdata(data[0])
    return bot_points,

def generate_points():
	condition = True				#Change to condition from aggr library
	task_func = random_generator	#Change to function from aggr lib
	while condition:
		yield(task_func())


print len(lib.SWARM)

"""
Main

"""
ani = animation.FuncAnimation(fig, update, generate_points, interval=300)
#ani.save('animation.gif', writer='imagemagick', fps=4);
plt.show()