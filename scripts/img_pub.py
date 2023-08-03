#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def webcam_publisher():

    #initalizing 1st ROS node
    rospy.init_node('webcam_publisher', anonymous=True)

    #ROS publisher to publish images to topic '/webcam_img'
    pub = rospy.Publisher('/webcam_img', Image, queue_size=10)

    rate = rospy.Rate(10)  #Publishing Rate

    cap = cv2.VideoCapture(0) #Capturing image from internal Webcam
    conv = CvBridge() #To convert opencv images to ROS format

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logwarn("Failed to capture image from webcam")
            break

        #Converting each frame to ROS image msg
        ros_image = conv.cv2_to_imgmsg(frame, "bgr8")

        #publishing image
        pub.publish(ros_image)

        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        webcam_publisher()
    except rospy.ROSInterruptException:
        pass
