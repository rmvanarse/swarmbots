"""
Temporarily standalone

** SHIFT CODE TO FORMATIONS.PY WHEN DONE **

"""


import numpy as np
import random
import swarm_lib as lib
import math

#the points between which line is to be formed
a=[1,1] #point with smaller x coordinate

b=[9,9] #point with larger x coordinate



length=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)   #length of line
slope=(a[1]-b[1])/(a[0]-b[0]) 					  #slope of line
intercept=(-b[1]*a[0]+b[0]*a[1])/(b[0]-a[0])      #intercept of line

theta=math.atan(slope)							  #angle made with x axis		


def y(x): 									      #returns y coord on line for given x coord
	return slope*x+intercept

def assign_x_on_line(bot):	      #assigns a position on line based on current position of bot 
	
	if bot.x>b[0]:				   
			x_new=b[0]-random.uniform(0.7,1)*(b[0]-a[0])
	elif bot.x<a[0]:
			x_new=a[0]+random.uniform(0,0.3)*(b[0]-a[0])
	else:
			x_new=bot.x
			
	return x_new


def right_distance(bot):                   #finds the distance from nearest bot to the right
	separation=length/len(lib.SWARM) 	                #optimum separation between bots
	
	neighbours=	bot.neighbours()
	
	for i in range(len(neighbours)):
		neighbours[i].x=assign_x_on_line(neighbours[i])
	
	min_sep=100
	index=0
	for i in range(len(neighbours)):
		sep=neighbours[i].x-bot.x		
		if((sep>0)&(sep<min_sep)):
			min_sep=sep
			index=i

	min_rdist=math.sqrt((bot.x-neighbours[index].x)**2+(bot.y-neighbours[index].y)**2)
	#print(separation)
	if min_rdist>separation and index>0:
		return min_rdist-separation
	else:
		return 0

	
def linef():
	
	x_new=[]
	y_new=[]

	for i in range(len(lib.SWARM)):
		
		bot=lib.SWARM[i]				
		
		r_shift=right_distance(bot)
		x_goal=assign_x_on_line(bot)+r_shift*math.cos(theta)
		y_goal=y(assign_x_on_line(bot))+r_shift*math.sin(theta)			
			

		rem_dist=math.sqrt((x_goal-bot.x)**2+(y_goal-bot.y)**2) 		
		if rem_dist>0:			
			x_step=(x_goal-bot.x)/rem_dist
			y_step=(y_goal-bot.y)/rem_dist
			step_size=0.05
			x_goal = bot.x + x_step * step_size
			y_goal = bot.y + y_step * step_size
		
		bot.goto_direct(x_goal,y_goal)

		x_new.append(x_goal)
		y_new.append(y_goal)		
	
	
	
	return (x_new,y_new)
		
																					
	
"""	
if __name__ =="__main__":
	print("Done")
"""


