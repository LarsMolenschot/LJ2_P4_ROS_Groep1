#include "image_processor/image_processor.h"
#include "image_processor/circle_detector.h"
#include "image_processor/camera.h"

//OpenCV
#include "opencv2/opencv.hpp"
#include <opencv2/videoio.hpp>
#include <vector>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/features2d.hpp>
#include "opencv2/calib3d/calib3d.hpp"

using namespace std;
using namespace cv;


// do not use ROS functions/headers/etc. in this file

ImageProcessor::ImageProcessor()
{
  std::cout << "Constructor" << std::endl;
}

ImageProcessor::~ImageProcessor()
{
    //
}

void ImageProcessor::setInputImage(cv::Mat *cv_mat_ptr){
  cv_mat_ptr_in_ = cv_mat_ptr;
}

void ImageProcessor::setCameraInfo(cv::Mat matrixP, cv::Mat matrixK){
  matrixP_ = matrixP;
  matrixK_ = matrixK;
}

void ImageProcessor::process()
{
    cv::Rect_<int> box;

    //check if new image is there
    if ( cv_mat_ptr_in_ != nullptr )
    {
        cv_mat_out_ = *cv_mat_ptr_in_;

// =========================================================================

//  //crop
// //(a,b,c,d)
// //a,b : Coordinates of the top-left corner (X,Y)
// //c,d : Rectangle width and height(X,Y)
// cv::Rect crop_region(0, 0, 200, 200);
//
// //new image crop
// cv_mat_out_=cv_mat_out_(crop_region);

// =========================================================================

    // // wit
    // //Convert origional image to grayscale.
    // cv::Mat grayscale { cv_mat_out_ };
    // if (grayscale.channels() == 3 || grayscale.channels() == 4)
    //     cvtColor(grayscale, grayscale, cv::COLOR_BGR2GRAY);
    // assert(grayscale.type() == CV_8UC1);
    //
    //
    // //Convert grayscale image to binary.
    // int th { 230 };
    // cv::Mat binary { };
    // cv::threshold(grayscale, binary, th, 255, cv::THRESH_BINARY);
    //
    // cv::Mat mask = binary;
    //
    //
    //
    //  int rows = mask.rows;
    //  int cols = mask.cols;
    //
    //  cv::Mat black(rows, cols, CV_8U, cv::Scalar(0, 0, 0));
    //
    //
    //  std::vector<cv::Mat> images(3);
    //
    //  // OpenCV works natively with RGB ordering
    //  images.at(0) = mask;
    //  images.at(1) = mask;
    //  images.at(2) = mask;
    //
    //  cv::Mat color;
    //  cv::merge(images, color);
    //  cv_mat_out_ = color;

// =========================================================================
    // // rood
    // cvtColor(cv_mat_out_,cv_mat_out_,CV_BGR2HSV);
    //
    // cv::Mat mask1 , mask2;
    // inRange(cv_mat_out_, cv::Scalar(0, 65, 75), cv::Scalar(1, 70, 80), mask1);
    // inRange(cv_mat_out_, cv::Scalar(100, 90, 70), cv::Scalar(120, 255, 255), mask2);
    //
    // cv::Mat mask = mask1 | mask2;
    // int rows = mask.rows;
    // int cols = mask.cols;
    //
    // cv::Mat black(rows, cols, CV_8U, cv::Scalar(0, 0, 0));
    //
    //
    // std::vector<cv::Mat> images(3);
    //
    // // OpenCV works natively with RGB ordering
    // images.at(0) = mask;
    // images.at(1) = mask;
    // images.at(2) = mask;
    //
    // cv::Mat color;
    // cv::merge(images, color);
    // cv_mat_out_ = color;
// =========================================================================

    //geel
    cvtColor(cv_mat_out_,cv_mat_out_,CV_BGR2HSV);

    cv::Mat mask1 , mask2;
    inRange(cv_mat_out_, cv::Scalar(0, 65, 75), cv::Scalar(1, 70, 80), mask1);
    inRange(cv_mat_out_, cv::Scalar(40, 90, 70), cv::Scalar(100, 255, 255), mask2);

    cv::Mat mask = mask1 | mask2;

     int rows = mask.rows;
     int cols = mask.cols;

     cv::Mat black(rows, cols, CV_8U, cv::Scalar(0, 0, 0));


     std::vector<cv::Mat> images(3);

     // OpenCV works natively with RGB ordering
     images.at(0) = mask;
     images.at(1) = mask;
     images.at(2) = black;

     cv::Mat color;
     cv::merge(images, color);
     cv_mat_out_ = color;
// =========================================================================

// // find contours:
//   std::vector<std::vector<cv::Point> > contours;
//   std::vector<cv::Vec4i> hierarchy;
//   findContours(mask, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE,cv::Point(0, 0));
//
//   // draw contours:
//   cv::Mat imgWithContours = cv::Mat::zeros(mask.rows, mask.cols, CV_8UC3);
//   cv::RNG rng(12345);
//   for (int i = 0; i < contours.size(); i++)
//   {
//     cv::Scalar colorcon = cv::Scalar(rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255));
//     drawContours(imgWithContours, contours, i, colorcon, 1, 8, hierarchy, 0);
//   }
//
//   cv_mat_out_= imgWithContours;



// =========================================================================
//std::vector<KeyPoint> head::KeyPoints()


    // Setup SimpleBlobDetector parameters.
    SimpleBlobDetector::Params params;

    // Change thresholds
    //params.thresholdStep = 100;
    params.minThreshold = 1;
    params.maxThreshold = 255;


    // Filter by Area.
    params.filterByArea = true;
    params.minArea = 1200;
    params.maxArea = 85000000;

    // Filter by Circularity
    params.filterByCircularity = false;
    params.minCircularity = 0.1;
    params.maxCircularity = 1;

    // Filter by Convexity
    params.filterByConvexity = false;
    params.minConvexity = 0.1;
    params.maxConvexity = 1;

    // Filter by Inertia
    params.filterByInertia = false;
    params.minInertiaRatio = 0.01;
    params.maxInertiaRatio = 0.7;

    //params.minRepeatability = 2;
    params.filterByColor = false;



    //Set up detector with params
        std::vector<KeyPoint> keypoints { };
        cv::Ptr<SimpleBlobDetector> detector { SimpleBlobDetector::create(params) };

        // Detect blobs
        detector->detect(cv_mat_out_, keypoints);
        //_keypoints = keypoints;
        //return _keypoints;
// =========================================================================

//head h1 { image };
//std::vector<KeyPoint> vectorhead { };
//vectorhead = h1.KeyPoints();

cv::Mat pictureUpdateHead { cv_mat_out_ };
    std::vector<KeyPoint> h { };

    for (auto l: keypoints)
    {
        h.push_back(l);
        drawKeypoints(pictureUpdateHead, h, pictureUpdateHead, Scalar(200, 80, 20), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
        h.erase(h.begin());

        float x0 = keypoints[0].pt.x;
        float y0 = keypoints[0].pt.y;
    

        std::cout << x0 << "\t" << y0;

    cv_mat_out_ = pictureUpdateHead;

 //ihead ->writeRGB8(pictureUpdateHead);


// =========================================================================

// =========================================================================
}


}
    //reset input image
    cv_mat_ptr_in_ = nullptr;
}

void ImageProcessor::draw_circle(const cv::Point & center, int radius, bool draw_center_coordinates)
{
  // // circle center in yellow
  // cv::circle(cv_mat_out_, center, 5, cv::Scalar(255, 255, 0), -1, 8, 0 );
  // // circle perimeter in purple.
  // cv::circle(cv_mat_out_, center, radius, cv::Scalar(255, 0, 255), 3, cv::LINE_8, 0 );

  // if (draw_center_coordinates)
  // {
  //   // circle center point x and y coordinates.
  //   std::ostringstream stringStream;
  //   stringStream  << "  x:" << center.x << "\n" << " y:" << center.y;
  //   // print circle center coordinates
  //   cv::putText(cv_mat_out_, stringStream.str(), center, cv::FONT_HERSHEY_PLAIN, 0.8, cv::Scalar(255, 153, 51), 2, 0.5);
  // }
}

cv::Mat ImageProcessor::getOutputImage(){
  return cv_mat_out_;
}

cv::Point ImageProcessor::getCircleCenter(){
  return circle_center_;
}
