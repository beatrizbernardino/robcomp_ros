#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from geometry_msgs.msg import Twist, Vector3

v = 0.2  # Velocidade linear
w = 0.5  # Velocidade angular

if __name__ == "__main__":
    rospy.init_node("roda_exemplo")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)

    try:
        while not rospy.is_shutdown():

            rospy.sleep(1.0)

            vel = Twist(Vector3(v,0,0), Vector3(0,0,0))
            pub.publish(vel)
            rospy.sleep(3.0)
            print ("indo")
            vel = Twist(Vector3(0,0,0), Vector3(0,0,0))
            pub.publish(vel)
            rospy.sleep(3.0)
            print ("acabou de para")
            vel = Twist(Vector3(0,0,0), Vector3(0,0,w))
            pub.publish(vel)
            rospy.sleep(2.0)
            print ("virou")
    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")