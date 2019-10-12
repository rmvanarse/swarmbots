"""
Created by: Aditya Bidwai

12/10/2019
"""
import rospy
import random
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


def cb(odom):
	global x
	global y
	x=odom.pose.pose.position.x
	y=odom.pose.pose.position.y
	print x
	print y

rospy.init_node('random_motion_controller')

pub=rospy.Publisher('robot1/cmd_vel',Twist) #confirm your robot name
rate_obj=rospy.Rate(10)

twist_obj=Twist()

while not rospy.is_shutdown():
	sub=rospy.Subscriber('robot1/odom',Odometry,cb) #confirm your robot name
	a=random.random()*2*3.14
	twist_obj.linear.x=(math.cos(a))*10
	twist_obj.linear.y=(math.sin(a))*10
	pub.publish(twist_obj)
	rate_obj.sleep()


