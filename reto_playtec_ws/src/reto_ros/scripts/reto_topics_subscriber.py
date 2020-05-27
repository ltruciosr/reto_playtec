#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("from node: " + rospy.get_caller_id() + ", I heard [%s]", data.data)
    
def listener():
    rospy.init_node('reto_listener', anonymous=False)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()