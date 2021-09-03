/**
 * @file msg_collector.cpp
 * @author IDPLab sooyeon Shin
 *
 * Function to Gathering the ros message for tranfering topic to kafka
 */

#include <ros/ros.h>
#include <iostream>

#include <sensor_msgs/NavSatFix.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/PointCloud2.h>
#include <geometry_msgs/Pose.h>

#include "ros_kafka_connector/VehicleInfo.h"

class MsgCollect{

private:
  ros::NodeHandle nh;

  ros::Subscriber v_gps_sub;
  ros::Subscriber v_local_sub;
  ros::Subscriber v_image_sub;
  ros::Subscriber v_pcl_sub;
  ros::Publisher vehicle_pub;

  ros_kafka_connector::VehicleInfo vehicle_info;

public:
  MsgCollect(){
    v_gps_sub = nh.subscribe<sensor_msgs::NavSatFix>\
        ("/ublox_gps/fix", 10, &MsgCollect::VehicleGPSCb, this);
    v_local_sub = nh.subscribe<geometry_msgs::Pose>\
        ("/local/vehicle", 10, &MsgCollect::VehicleLocalCb, this);
//    v_image_sub = nh.subscribe<sensor_msgs::Image>\
//        ("/zed2/zed_node/left/image_rect_color", 10, &MsgCollect::SensorImageCb, this);
//    v_pcl_sub = nh.subscribe<sensor_msgs::PointCloud2>\
//        ("zed2/zed_node/point_cloud/cloud_registered", 10, &MsgCollect::SensorPCLCb, this);

    vehicle_pub = nh.advertise<ros_kafka_connector::VehicleInfo>("/vehicle", 10);
    ROS_INFO("[Msg Collecting]: started.");
  }
  ~MsgCollect(){}

  void VehicleGPSCb(const sensor_msgs::NavSatFixConstPtr& msg){
    vehicle_info.v_global = *msg;
    vehicle_pub.publish(vehicle_info);
  }

  void VehicleLocalCb(const geometry_msgs::PoseConstPtr& msg){
    geometry_msgs::Pose local = *msg;
    vehicle_info.v_local = msg->position;
  }

//  void SensorImageCb(const sensor_msgs::ImageConstPtr& msg){
//    vehicle_info.image_height = msg->height;
//    vehicle_info.image_width = msg->width;
//    vehicle_info.image_data = msg->data;
//  }

//  void SensorPCLCb(const sensor_msgs::PointCloud2ConstPtr& msg){
//    vehicle_info.pcl_height = msg->height;
//    vehicle_info.pcl_width = msg->width;
//    vehicle_info.pcl_data = msg->data;
//  }

  void main()
  {
    // main loop
    ros::Rate rate(10);

    ROS_INFO("[Msg Collecting] Loop Start.");
    while(nh.ok()){
      ros::Time time = ros::Time::now();

      ros::spinOnce();
      rate.sleep();
    }
  }
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "message_collecting");

    MsgCollect mc;
    mc.main();

    return 0;
}
