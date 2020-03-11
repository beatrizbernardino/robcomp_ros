#! /usr/bin/env python
# -*- coding:utf-8 -*-


import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan


listax=[]

def scaneou(dado):
	x=np.array(dado.ranges).round(decimals=2)
	listax.append(x[0])
	return listax



if __name__=="__main__":

	rospy.init_node("le_scan")

	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
	recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)

	while not rospy.is_shutdown():
		velocidade = Twist(Vector3(0.16, 0, 0), Vector3(0, 0, 0))
		velocidade_saida.publish(velocidade)
		rospy.sleep(2.0)

	
		x=len(listax)-1
		print(x)		
		if listax[x] <= 0.98:
			print ("entrou")
			velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)
			rospy.sleep(3.0)
			velocidade = Twist(Vector3(-0.1, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)
			rospy.sleep(5.0)
				
		elif listax[x] >= 1.02:
			print ('entrou tb')
			
			velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)
			rospy.sleep(0.5)
			velocidade = Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)
			rospy.sleep(0.5)

				
			

