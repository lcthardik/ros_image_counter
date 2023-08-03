#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import os

class ImagePathSaverNode:
    def __init__(self):
        #file_path saves img paths
        self.file_path = os.path.join(os.path.expanduser("~"), "ros_saved_img_paths.txt")

        #Subscribe to "img_path" topic
        self.sub_img_path = rospy.Subscriber('/img_path', String, self.img_path_callback)

        #Subscribe to "/reset" topic
        self.sub_reset = rospy.Subscriber('/reset', String, self.reset_callback)

    def img_path_callback(self, msg):
        try:
            #getting img path from msg
            img_path = msg.data

            #opening file in append mode
            with open(self.file_path, 'a') as file:
                file.write(img_path + '\n')

            rospy.loginfo("Saved image path: " + self.file_path)

        except Exception as e:
            rospy.logerr("Error while saving: " + str(e))

    def reset_callback(self,msg):
        try:
            #Clearing file content
            with open(self.file_path, 'w') as file:
                file.write('')
            rospy.loginfo("Cleared text file")
        except Exception as e:
            rospy.logerr("Error while clearing file: " + str(e))

def main():
    rospy.init_node('img_path_saver', anonymous=True)
    image_path_saver = ImagePathSaverNode()
    rospy.spin()

if __name__ == '__main__':
    main()
