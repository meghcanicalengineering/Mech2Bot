#!/usr/bin/env python

import rospy
import tf2_ros
import geometry_msgs.msg

def main():
    rospy.init_node('tf_broadcaster_node')

    tf_broadcaster = tf2_ros.StaticTransformBroadcaster()

    # Define the transform
    static_transformStamped = geometry_msgs.msg.TransformStamped()
    static_transformStamped.header.stamp = rospy.Time.now()
    static_transformStamped.header.frame_id = "base_link"
    static_transformStamped.child_frame_id = "laser"
    static_transformStamped.transform.translation.x = 0.0
    static_transformStamped.transform.translation.y = 0.0
    static_transformStamped.transform.translation.z = 0.0
    static_transformStamped.transform.rotation.x = 0.0
    static_transformStamped.transform.rotation.y = 0.0
    static_transformStamped.transform.rotation.z = 0.0
    static_transformStamped.transform.rotation.w = 1.0

    while not rospy.is_shutdown():
        # Publish the transform
        tf_broadcaster.sendTransform(static_transformStamped)
        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
