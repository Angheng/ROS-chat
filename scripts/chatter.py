#!/usr/bin/env python

import time
import rospy
from chat.msg import chatMsg

class Chatter():
    
    def __init__(self, _name, _topic):
        self.topic = _topic
        self.name = _name
        rospy.init_node(self.name, anonymous=True)
        rospy.Subscriber(self.topic, chatMsg, self.received)
        rospy.loginfo('Now you Subcribed {} Topic'.format(self.topic))

        self.send()

    def received(self, data):
        if data.name == self.name:
            return

        rospy.loginfo('==========================================')
        rospy.loginfo('DATE: {}'.format(
            time.strftime('%c')
            )
        )
        rospy.loginfo('[{}] :: {}'.format(data.name, data.text))
        rospy.loginfo('==========================================')

    def send(self):
        pub = rospy.Publisher(self.topic, chatMsg, queue_size=10)
        rospy.loginfo('Ready to Send.')

        while not rospy.is_shutdown():
            text = raw_input()

            if text == '@quit':
                return
            
            pub.publish(rospy.Time.now(), self.name, text)

if __name__ == '__main__':
	name, topic = raw_input('set name & topic\n').rstrip().split(' ')
	c = Chatter(name, topic)
