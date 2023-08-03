#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import os

class ImageCounterNode:
    def __init__(self):
        self.counter = 0
        self.conv = CvBridge()

        #Subscribe to the "/webcam_img" topic
        self.sub_to_img = rospy.Subscriber('/webcam_img', Image, self.image_callback)

        #Subscribe to the "/reset" topic
        self.sub_to_reset = rospy.Subscriber('/reset', String, self.reset_callback)

        #Created a publisher to publish img paths to "/img_path" topic
        self.pub_img_path = rospy.Publisher('/img_path', String, queue_size=10)

    def image_callback(self, msg):
        try:
            #Converting ROS img back to opencv format
            cv_image = self.conv.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        except Exception as e:
            rospy.logerr("Error: " + str(e))
            return

        self.counter += 1

        #Check whether the img number is prime or not
        if self.is_prime(self.counter):
            img_file = "img_" + str(self.counter) + ".png"
            
            #Creating img path
            img_path = os.path.join(os.path.expanduser("~"), "ros_saved_imgs", img_file)

            #Creating a directory if not present previously
            if not os.path.exists(os.path.dirname(img_path)):
                os.makedirs(os.path.dirname(img_path))

            #Saved img with the generated path
            cv2.imwrite(img_path, cv_image)
            rospy.loginfo("image saved to: " + str(img_path))

            #Publishing the img path
            img_path_msg = String()
            img_path_msg.data = img_path
            self.pub_img_path.publish(img_path_msg)

    def reset_callback(self,msg):
        #Reset counter to 0 when recieved msg on "/reset" topic
        self.counter = 0
        rospy.loginfo("Counter reset to 0.")

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

def main():
    rospy.init_node('img_counter', anonymous=True)
    image_counter = ImageCounterNode()
    rospy.spin()

if __name__ == '__main__':
    main()
