#ifndef COLOR_DETECTOR_H
#define COLOR_DETECTOR_H
//#include "color_detector.h"

//OpenCV
#include "opencv2/opencv.hpp"
#include "opencv2/core.hpp"
#include <opencv2/videoio.hpp>
#include <vector>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/features2d.hpp>
#include "opencv2/calib3d/calib3d.hpp"

#include <iostream>

using namespace std;
using namespace cv;


// =========================================================================
cv::Mat color_detector::returnimage()
{
    //Here _g is the origional image.
    cv::Mat cv_mat_out_ =_g;
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







#endif
