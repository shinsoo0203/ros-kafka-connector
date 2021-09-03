#!/usr/bin/env python

def import_msg_type(msg_type):

    # Adding a new msg type is as easy as including an import and updating the variable 
    if msg_type == "std_msgs/String":
        from std_msgs.msg import String
        subscriber_msg = String
    elif msg_type == "ObjectInfo":
        from ros_kafka_connector.msg import ObjectInfo
        subscriber_msg = ObjectInfo
    elif msg_type == "VehicleInfo":
        from ros_kafka_connector.msg import VehicleInfo
        subscriber_msg = VehicleInfo
    elif msg_type == "std_msgs/Uint8":
        from std_msgs.msg import Uint8
        subscriber_msg = Uint8
    elif msg_type == "std_msgs/Uint32":
        from std_msgs.msg import Uint32
        subscriber_msg = Uint32
    elif msg_type == "sensor_msgs/NavSatFix":
        from sensor_msgs.msg import NavSatFix
        subscriber_msg = NavSatFix
    elif msg_type == "geometry_msgs/Pose":
        from geometry_msgs.msg import Pose
        subscriber_msg = Pose
    else:
        raise ValueError("MSG NOT SUPPORTED: Please add imports to utils.py for specific msg type.")
    
    return subscriber_msg
