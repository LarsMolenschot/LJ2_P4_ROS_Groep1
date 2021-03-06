#ifndef ROS_IMG_PROCESSOR_NODE_H
#define ROS_IMG_PROCESSOR_NODE_H

//std C++
#include <iostream>

//ROS headers for image I/O
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <sensor_msgs/CameraInfo.h>
#include <vector>

#include "geometry_msgs/Vector3.h"

#include "image_processor.h"


/** \brief Simple Image Processor
 *
 * Simple Image Processor with opencv calls
 *
 */
class ImageProcessorRos
{
    protected:
        //ros node handle
        ros::NodeHandle nh_;

        //image transport
        image_transport::ImageTransport img_tp_;

        // subscribers to the image and camera info topics
        image_transport::Subscriber image_subs_;
        ros::Subscriber camera_info_subs_;

        //publishers
        image_transport::Publisher image_pub_;
        ros::Publisher circle_center_pub;
	ros::Publisher pub_positie;
	
 

        //pointer to received (in) and published (out) images
        cv_bridge::CvImagePtr cv_img_ptr_in_;
        cv_bridge::CvImage cv_img_out_;

        // ray direction in camera frame.

        //image encoding label
        std::string img_encoding_;

        //wished process rate, [hz]
        double rate_;

        ImageProcessor imgp;

        cv::Point circle_center;
	//std::vector<double> poses = imgp.getposes();
	

	
	
    protected:
        // callbacks
        void imageCallback(const sensor_msgs::ImageConstPtr& _msg);
        void cameraInfoCallback(const sensor_msgs::CameraInfo & _msg);

    public:
        /** \brief Constructor
        *
        * Constructor
        *
        */
        ImageProcessorRos();

        /** \brief Destructor
        *
        * Destructor
        *
        */
        ~ImageProcessorRos();
	


	

  	//std::cout << matrixP_ << std::endl;
      /** \brief Process input image
        *
        * Process input image
        *
        **/
        void process();


        /** \brief Publish output image
        *
        * Publish output image
        *
        */
        void publish();

        /** \brief Returns rate_
         *
         * Returns rate_
         *
         **/
        double getRate() const;
};
#endif
