#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('reto_talker', anonymous=False)
    rate = rospy.Rate(10) # freq: 10hz
    while not rospy.is_shutdown():
        reto_msg = "reto playtec" 
        pub.publish(reto_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass