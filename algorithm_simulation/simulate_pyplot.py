"""
Created by: Rishikesh Vanarse
27/10/19

Simulates a swarm of any number of bots
on pyplot, for performing any imported task

Modularity:

1) Initialization:
   Any initialization function from initialize_swarm (imported) can be used

2) Swarm task:
   The generate_points function can call any swarm task
   from any of the imported modules
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import swarm_lib as lib
import initialize_swarm as sw
import aggregation as aggr
import formations
import area_coverage as coverage


#Initialize swarm
sw.random_initializer(10, verbose=True)
x_list = [bot.x for bot in lib.SWARM]
y_list = [bot.y for bot in lib.SWARM]
state_list = ['o' for i in range(len(lib.SWARM))]


#Initialize figure
fig, ax = plt.subplots()
bot_points, = ax.plot(x_list, y_list, 'o')

#Set Limits (ToDo)
ax.set_xlim(( 0, lib.DEFAULT_XRANGE))
ax.set_ylim((0, lib.DEFAULT_YRANGE))


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
  condition = True        #Change to condition from aggr library
  task_func = aggr.aggr_potentialField
  #task_func = formations.formation_team
  #task_func = coverage.AC_potentialField
  while condition:
    yield(task_func())


print len(lib.SWARM)

"""
Main

"""
ani = animation.FuncAnimation(fig, update, generate_points, interval=150)
#ani.save('../anim_saves/area_cvg_10bots.gif', writer='imagemagick', fps=10)
plt.show()