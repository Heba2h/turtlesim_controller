#!/bin/env python3
import math
from tkinter import Y
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

rospy.init_node("turtlesim_controller")

vel=Twist()

xpose=0
ypose=0
theta=0
#choose the prefered target positions 
xtarget=3 
ytarget=2

def callback(pose):
    global xpose
    global ypose
    global theta
    xpose=pose.x
    ypose=pose.y
    theta=pose.theta

rospy.Subscriber("/turtle1/pose",Pose,callback)
velPub= rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1)

delta_x=0
delta_y=0
dist=0
delta_theta=0

k=1.5
t=6

def Publisher():
    delta_x= xtarget-xpose
    delta_y= ytarget-ypose
    dist= k*math.sqrt((delta_x**2)+(delta_y**2))
    delta_theta= t*(-theta + math.atan2(delta_y,delta_x))
    print (delta_theta,"delta theta")
    vel.linear.x=dist 
    vel.angular.z= delta_theta
    print(dist)
    velPub.publish(vel)          

rate = 10
r = rospy.Rate(rate)
while not rospy.is_shutdown(): 
    r.sleep()

    delta_x= xtarget-xpose
    delta_y= ytarget-ypose
    print(ypose,"ypose")
    dist = k*math.sqrt((delta_x**2)+(delta_y**2))

    
    delta_theta= t*(-theta + math.atan2(delta_y,delta_x))
    print (delta_theta,"delta theta")
    vel.linear.x=dist 
    vel.angular.z= delta_theta
    print(dist)
    velPub.publish(vel)  

    if (dist<0.5):
        break
        