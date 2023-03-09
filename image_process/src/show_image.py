#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image as ImageMsg
import numpy as np
from PIL import Image
import cv2

def get_image(ros_image):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(ros_image, desired_encoding="passthrough")
    cv2.imshow("gray",cv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('show_image', anonymous=True)
    rospy.Subscriber("/camera/color/image_raw", ImageMsg, callback=get_image, queue_size=10)
    rospy.Subscriber("/camera/depth/image_raw", ImageMsg, callback=get_image, queue_size=10)
    rospy.spin()