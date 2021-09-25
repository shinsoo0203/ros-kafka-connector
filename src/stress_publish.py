#!/usr/bin/env python

import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
import rospy
from rospy_message_converter import json_message_converter
from utils import import_msg_type

import std_msgs.msg

def on_send_success(record_metadata):
    meta_time = record_metadata.timestamp

class stress_publish():

    def __init__(self):

        # initialize node
        rospy.init_node("stress_publish")
        rospy.on_shutdown(self.shutdown)

        # Retrieve parameters from launch file
        bootstrap_server = rospy.get_param("~bootstrap_server", "114.70.21.162:9092")
        self.ros_topic = rospy.get_param("~ros_topic", "/grid/obj")
        self.kafka_topic = rospy.get_param("~kafka_topic", "vehicle")
        self.msg_type = rospy.get_param("~msg_type", "ObjectInfo")

        # Create kafka producer
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_server, value_serializer=lambda m: json.dumps(m).encode('ascii'))


    def run(self):
        rate = rospy.Rate(100)
        count = 1
        while not rospy.is_shutdown() and count!=1001:

            #print(t, count)
            json_str = "\"car_id\":\"",count,str(rospy.Time.now()), "{\"v_global\": {\"status\": {\"status\": 0, \"service\": 3}, \"altitude\": 44.204, \"longitude\": 127.0787276, \"position_covariance\": [601.132324, 0.0, 0.0, 0.0, 601.132324, 0.0, 0.0, 0.0, 1601.200225], \"header\": {\"frame_id\": \"gps\", \"seq\": 186}, \"latitude\": 37.541206599999995, \"position_covariance_type\": 2}, \"v_local\": {\"y\": -14.754055225675113, \"x\": 226.96239794447146, \"z\": 1.2}}"

            t= float(str(rospy.Time.now()))/1000000000.0
            p = self.producer.send(self.kafka_topic, json_str).add_callback(on_send_success)
            self.producer.flush()
            now = float(str(rospy.Time.now()))/1000000000.0
            print(now-t)

            '''
            record_metadata = p.get(timeout=10)
            now = float(str(rospy.Time.now()))/1000000000.0
            print(now - t)
            edge_time = float(str(t))/1000000000.0
            meta_time = float(record_metadata.timestamp)/1000.0
            '''

            count = count+1
            rate.sleep()

        #print("End of Test")

    def shutdown(self):
        #rospy.loginfo("Shutting down")
        a=1

if __name__ == "__main__":

    try:
        node = stress_publish()
        node.run()
    except rospy.ROSInterruptException:
        pass

    #rospy.loginfo("Exiting")
