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
state_list = [bot.state for bot in lib.SWARM]

#Pseudo init

lib.SWARM[5].state = 'A'
lib.SWARM[7].state = 'A'

state_list[5] = 'A'
state_list[7] = 'A'


#States
states =['blue', 'red'] #Replce with list from dict
state_dict = {'A':'bo', 'stop':'go'} #Replace with dict from lib
bot_points = []





#Initialize figure
fig, ax = plt.subplots()

for i in range(len(state_list)):
  tempX = lib.SWARM[i].x
  tempY = lib.SWARM[i].y
  col = state_dict[state_list[i]]
  points, = ax.plot(tempX, tempY, col)
  bot_points.append(points)



#Set Limits (ToDo)
ax.set_xlim(( 0, lib.DEFAULT_XRANGE))
ax.set_ylim((0, lib.DEFAULT_YRANGE))


#Helper functions
def random_generator():
  return (np.random.rand(len(lib.SWARM))*lib.DEFAULT_XRANGE, 
    np.random.rand(len(lib.SWARM))*lib.DEFAULT_YRANGE,
    state_list)

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
  ax.cla()
  ax.set_xlim(( 0, lib.DEFAULT_XRANGE))
  ax.set_ylim((0, lib.DEFAULT_YRANGE))
  for i in range(len(state_list)):
    tempX = data[0][i]
    tempY = data[1][i]
    col = state_dict[state_list[i]]
    points, = ax.plot(tempX, tempY, col)
    bot_points[i]= points
  return bot_points

def generate_points():
  condition = True        #Change to condition from aggr library
  #task_func = aggr.go_towards_centroid 
  #task_func = formations.formation_team
  #task_func = coverage.AC_potentialField
  task_func = random_generator
  while condition:
    yield(task_func())


print len(lib.SWARM)

"""
Main

"""
ani = animation.FuncAnimation(fig, update, generate_points, interval=150)
#ani.save('../anim_saves/area_cvg_10bots.gif', writer='imagemagick', fps=10)
plt.show()