#!/usr/bin/env python

def import_msg_type(msg_type):

    # Adding a new msg type is as easy as including an import and updating the variable 
    if msg_type == "std_msgs/String":
        from std_msgs.msg import String
        subscriber_msg = String
    elif msg_type == "ObjectInfo":
        from ros_kafka_connector.msg import ObjectInfo
        subscriber_msg = ObjectInfo
    else:
        raise ValueError("MSG NOT SUPPORTED: Only ObjectInfo are currently supported. \
                          Please add imports to utils.py for specific msg type.")
    
    return subscriber_msg
