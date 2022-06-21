
//ros dependencies
#include "image_processor/image_processor_node.h"
#include <sensor_msgs/image_encodings.h>
#include <cv_bridge/cv_bridge.h>
#include "image_processor/image_processor.h"
#include <tf2/LinearMath/Quaternion.h>

#include "geometry_msgs/Vector3.h"
#include "geometry_msgs/Pose.h"


#include <sensor_msgs/image_encodings.h>

//node main
int main(int argc, char **argv)
{

      //init ros
      ros::init(argc, argv, "image_processor");

      //create ros wrapper object
      ImageProcessorRos imgp_ros;

      //set node loop rate
      ros::Rate loopRate(imgp_ros.getRate());

      //node loop
      while ( ros::ok() )
      {
            //execute pending callbacks
            ros::spinOnce();

            //do things
           imgp_ros.process();

            //publish things
            imgp_ros.publish();

            //relax to fit output rate
            loopRate.sleep();
      }
      //exit program
      return 0;
}



ImageProcessorRos::ImageProcessorRos() :
    nh_(ros::this_node::getName()),
    img_tp_(nh_)
{
	//loop rate [hz], Could be set from a yaml file
	rate_=10;

	//sets publishers
	image_pub_ = img_tp_.advertise("image_out", 100);
  circle_center_pub   = nh_.advertise<geometry_msgs::Vector3>("circle_center", 1);

  //create publisher for vision
  pub_positie = nh_.advertise<geometry_msgs::Pose>("vision_pose", 1);
  geometry_msgs::Pose visionpose;

  // image_pub_ = img_tp_.advertise("image_out", 100);
  // std::cout << part<<"\t"<< color <<"\n";   = nh_.advertise<std_msgs::string>("LEGO", 1);


  // cv::int ImageProcessor::getPosition(){
  //   return x0;
  //   return y0;



	//sets subscribers
	image_subs_ = img_tp_.subscribe("image_in", 1, &ImageProcessorRos::imageCallback, this);
	camera_info_subs_ = nh_.subscribe("camera_info_in", 100, &ImageProcessorRos::cameraInfoCallback, this);
}


ImageProcessorRos::~ImageProcessorRos()
{

}

void ImageProcessorRos::process(){
  imgp.process();

}

void ImageProcessorRos::publish()
{
  cv_img_out_.image = imgp.getOutputImage();
  circle_center = imgp.getCircleCenter();

  //image_raw topic
	if(cv_img_out_.image.data)
	{
      //ROS_INFO("Publish image out");
	    cv_img_out_.header.seq ++;
	    cv_img_out_.header.stamp = ros::Time::now();
	    cv_img_out_.header.frame_id = "camera";
	    cv_img_out_.encoding = img_encoding_;
	    image_pub_.publish(cv_img_out_.toImageMsg());

      geometry_msgs::Pose visionpose;
      visionpose.position.x = 0;
      visionpose.position.y = 0;
      visionpose.position.z = 0;

      tf2::Quaternion myQuaternion;
      myQuaternion.setRPY( 0, 0, 0 );  // Create this quaternion from roll/pitch/yaw (in radians)

      visionpose.orientation.x = myQuaternion.getX();
      visionpose.orientation.y = myQuaternion.getY();
      visionpose.orientation.z = myQuaternion.getZ();
      visionpose.orientation.w = myQuaternion.getW();
      pub_positie.publish(visionpose);

      // Publish circle center
      geometry_msgs::Vector3 center;

      center.x = circle_center.x;
      center.y = circle_center.y;
      center.z = 0;

      circle_center_pub.publish(center);
	}
}

double ImageProcessorRos::getRate() const
{
    return rate_;
}

void ImageProcessorRos::imageCallback(const sensor_msgs::ImageConstPtr& image_topic)
{
  try
  {
      img_encoding_ = image_topic->encoding;//get image encodings
      cv_img_ptr_in_ = cv_bridge::toCvCopy(image_topic, image_topic->encoding);//get image
      imgp.setInputImage(&cv_img_ptr_in_->image);
  }
  catch (cv_bridge::Exception& e)
  {
      ROS_ERROR("ImageProcessorRos::image_callback(): cv_bridge exception: %s", e.what());
      return;
  }
}

void ImageProcessorRos::cameraInfoCallback(const sensor_msgs::CameraInfo & _msg)
{

  //Camera matrix
  cv::Mat matrixP_;
  cv::Mat matrixK_;

	matrixP_ = (cv::Mat_<double>(3,3) << _msg.P[0],_msg.P[1],_msg.P[2],
                                        _msg.P[3],_msg.P[4],_msg.P[5],
                                        _msg.P[6],_msg.P[7],_msg.P[8]);

  matrixK_ = (cv::Mat_<double>(3,3) << _msg.K[0],_msg.K[1],_msg.K[2],
                                        _msg.K[3],_msg.K[4],_msg.K[5],
                                        _msg.K[6],_msg.K[7],_msg.K[8]);

  imgp.setCameraInfo(matrixP_, matrixK_);
}