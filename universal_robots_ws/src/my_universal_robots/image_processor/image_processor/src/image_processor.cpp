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

#include <iostream>

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

// =========================================================================
  //fuction draw circle and get orientation
void drawAxis(Mat& img, Point p, Point q, Scalar colour, const float scale = 0.2)
{
    double angle = atan2( (double) p.y - q.y, (double) p.x - q.x ); // angle in radians
    double hypotenuse = sqrt( (double) (p.y - q.y) * (p.y - q.y) + (p.x - q.x) * (p.x - q.x));
    // Here we lengthen the arrow by a factor of scale
    q.x = (int) (p.x - scale * hypotenuse * cos(angle));
    q.y = (int) (p.y - scale * hypotenuse * sin(angle));
    line(img, p, q, colour, 1, LINE_AA);
    // create the arrow hooks
    p.x = (int) (q.x + 9 * cos(angle + CV_PI / 4));
    p.y = (int) (q.y + 9 * sin(angle + CV_PI / 4));
    line(img, p, q, colour, 1, LINE_AA);
    p.x = (int) (q.x + 9 * cos(angle - CV_PI / 4));
    p.y = (int) (q.y + 9 * sin(angle - CV_PI / 4));
    line(img, p, q, colour, 1, LINE_AA);
}

double getOrientation(const vector<Point> &pts, Mat imagecrop)
{
    //Construct a buffer used by the pca analysis
    int sz = static_cast<int>(pts.size());
    Mat data_pts = Mat(sz, 2, CV_64F);
    for (int i = 0; i < data_pts.rows; i++)
    {
        data_pts.at<double>(i, 0) = pts[i].x;
        data_pts.at<double>(i, 1) = pts[i].y;
    }


    //Perform PCA analysis
    PCA pca_analysis(data_pts, Mat(), PCA::DATA_AS_ROW);

    //Store the center of the object
    Point cntr = Point(static_cast<int>(pca_analysis.mean.at<double>(0, 0)),
                       static_cast<int>(pca_analysis.mean.at<double>(0, 1)));

    //Store the eigenvalues and eigenvectors
    vector<Point2d> eigen_vecs(2);
    vector<double> eigen_val(2);
    for (int i = 0; i < 2; i++)
    {
        eigen_vecs[i] = Point2d(pca_analysis.eigenvectors.at<double>(i, 0),
                                pca_analysis.eigenvectors.at<double>(i, 1));
        eigen_val[i] = pca_analysis.eigenvalues.at<double>(i);
    }

    // Draw the principal components
    circle(imagecrop, cntr, 3, Scalar(255, 0, 255), 2);
    Point p1 = cntr + 0.02 * Point(static_cast<int>(eigen_vecs[0].x * eigen_val[0]), static_cast<int>(eigen_vecs[0].y * eigen_val[0]));
    Point p2 = cntr - 0.02 * Point(static_cast<int>(eigen_vecs[1].x * eigen_val[1]), static_cast<int>(eigen_vecs[1].y * eigen_val[1]));
    drawAxis(imagecrop, cntr, p1, Scalar(0, 255, 0), 1);
    drawAxis(imagecrop, cntr, p2, Scalar(255, 255, 0), 5);
    double angle = atan2(eigen_vecs[0].y, eigen_vecs[0].x); // orientation in radians

    //double angle = 2.0;
    return angle;
}
// =========================================================================

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
      int rows = cv_mat_out_.rows;
      int cols = cv_mat_out_.cols;

      cv::Mat blackim(rows, cols, CV_8U, cv::Scalar(0, 0, 0));
      cv::Mat mask = blackim;

      for (int i = 0; i < 1; i++) {
                // =========================================================================
                // wit
                //Convert origional image to grayscale.
                cv::Mat grayscale { cv_mat_out_ };
                if (grayscale.channels() == 3 || grayscale.channels() == 4)
                    cvtColor(grayscale, grayscale, cv::COLOR_BGR2GRAY);
                assert(grayscale.type() == CV_8UC1);

                //Convert grayscale image to binary.
                int th { 220};
                cv::Mat binary { };
                cv::threshold(grayscale, binary, th, 255, cv::THRESH_BINARY);

                cv::dilate(binary, binary, cv::Mat(), cv::Point(-1,-1));
                // floodFill(binary, cv::Point(0,0), cv::Scalar(255));
                // cv::Mat im_floodfill_inv;
                // bitwise_not(binary, im_floodfill_inv);


                cv::Mat white = binary;
                // =========================================================================

                // rood
                cvtColor(cv_mat_out_,cv_mat_out_,CV_BGR2HSV);

                cv::Mat red1 , red2;
                inRange(cv_mat_out_, cv::Scalar(0, 65, 75), cv::Scalar(1, 70, 80), red1);
                inRange(cv_mat_out_, cv::Scalar(100, 90, 70), cv::Scalar(115, 255, 255), red2);


                cv::Mat red = red1 | red2;
                // =========================================================================

                //geel
                cvtColor(cv_mat_out_,cv_mat_out_,CV_BGR2HSV);

                cv::Mat yellow1 , yellow2;
                inRange(cv_mat_out_, cv::Scalar(0, 65, 75), cv::Scalar(1, 70, 80), yellow1);
                inRange(cv_mat_out_, cv::Scalar(80, 90, 70), cv::Scalar(105, 255, 255), yellow2);

                // inRange(cv_mat_out_, cv::Scalar(0, 65, 75), cv::Scalar(1, 70, 80), yellow1);
                // inRange(cv_mat_out_, cv::Scalar(30, 90, 70), cv::Scalar(100, 255, 255), yellow2);
                // inRange(cv_mat_out_, cv::Scalar(45, 85, 90), cv::Scalar(120, 210, 255), yellow2);


                 cv::Mat yellow = yellow1 | yellow2;
                 // cv::Mat yellow = yellow2;
                // =========================================================================

                cv::Mat bw1;
                string color;
                string part;
                //for loop for every color
                for (int j = 0; j < 3; j++) {
                          if (j == 0) {
                            bw1 = white;
                            color = "white";
                          }
                          else if (j == 1) {
                            bw1= red;
                            color = "red";
                          }
                          else if (j == 2) {
                          //if (j == 2) {
                            bw1 = yellow;
                            color = "yellow";
                          }
                          vector<vector<Point> > contours1;
                          findContours(bw1, contours1, RETR_LIST, CHAIN_APPROX_NONE);
                          for (size_t i = 0; i < contours1.size(); i++)
                          {
                              // Calculate the area of each contour
                              double area = contourArea(contours1[i]);
                              // Ignore contours that are too small or too large
                              //part = "nothing found";
                              //std::cout << "area =" <<"\t"<< area <<"\n";
                              if (area > 3000){
                                std::cout << "area = " << area <<"\n";
                                std::cout << "color = " << color <<"\n";
                                //std::cout << "area =" <<"\t"<< area <<"\n";
                                  if ((area > 8300 && area < 8600)&&(color == "white")){
                                    part = "pants small";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                                  else if ((area > 35000 && area < 37000)&&(color == "white")){
                                    part = "pants big";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                                  else if ((area > 9000 && area < 11000)&&(color == "red")){
                                    part = "shirt small";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                                  else if ((area > 38000 && area < 40000)&&(color == "red")){
                                    part = "shirt big";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                                  else if ((area > 3300 && area < 3900)&&(color == "yellow")){
                                    part = "hands small";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                                  else if ((area > 15500 && area < 16500)&&(color == "yellow")){
                                    part = "hands big";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                                  else if ((area > 14400 && area < 15400)&&(color == "yellow")){
                                    part = "head small";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                                  else if ((area > 65000 && area < 66000)&&(color == "yellow")){
                                    part = "head big";
                                    std::cout << part<<"\t"<< color <<"\n";
                                  }
                              // std::cout << part<<"\t"<< color <<"\n";
                              mask = bw1;
                              object = part;
                             }
                          }
                    }
                // =========================================================================
      }
      // =========================================================================

          cv::Mat black(rows, cols, CV_8U, cv::Scalar(0, 0, 0));

          std::vector<cv::Mat> images(3);

          // OpenCV works natively with RGB ordering
          images.at(0) = black;
          images.at(1) = mask;
          images.at(2) = black;

          cv::Mat color;
          cv::merge(images, color);
          cv_mat_out_ = color;
      // // =========================================================================
      //
          // Setup SimpleBlobDetector parameters.
          SimpleBlobDetector::Params params;

          // Change thresholds
          //params.thresholdStep = 100;
          params.minThreshold = 1;
          params.maxThreshold = 255;

          // Filter by Area.
          params.filterByArea = true;
          params.minArea = 3000;
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

      //draw circle and find x , y
      cv::Mat pictureUpdateHead { cv_mat_out_ };
          std::vector<KeyPoint> h { };

          for (auto l: keypoints)
          {
              h.push_back(l);
              drawKeypoints(pictureUpdateHead, h, pictureUpdateHead, Scalar(200, 80, 20), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
              h.erase(h.begin());

              positionX = keypoints[0].pt.x;
              positionY = keypoints[0].pt.y;


          cv_mat_out_ = pictureUpdateHead;


      // =========================================================================

      Mat src = cv_mat_out_;
      double angle;
      // Convert image to grayscale
      Mat gray;
      cvtColor(src, gray, COLOR_BGR2GRAY);
      // Convert image to binary
      Mat bw;
      threshold(gray, bw, 50, 255, THRESH_BINARY | THRESH_OTSU);
      // Find all the contours in the thresholded image
      vector<vector<Point> > contours;
      findContours(bw, contours, RETR_LIST, CHAIN_APPROX_NONE);
      for (size_t i = 0; i < contours.size(); i++)
      {
          // Calculate the area of each contour
          double area = contourArea(contours[i]);
          // Ignore contours that are too small or too large
          if (area < 1e2 || 1e5 < area) continue;
          // Draw each contour only for visualisation purposes
          drawContours(src, contours, static_cast<int>(i), Scalar(0, 0, 255), 2);
          // Find the orientation of each shape
          angle = getOrientation(contours[i], src);
          double degrees = angle * (180/ 3.141592654);
          if (area > 3000){
          std::cout << "X"<< " "<< positionX << "\t" << "Y" << " "<< positionY << "\t" << "Rotation" << " "<< degrees <<"\n"<<"\n";

          OBangle = angle;
        }
    }

cv_mat_out_ = src;

      // =========================================================================
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

// vector<double> ImageProcessor::getposes(){
//   positionX = x_pos;
// 	positionY = y_pos;
// 	angle = angle_pos;
//   //double = returnarr[] = [positionX, positionY, angle];
//   vector<double> returnarr;
//   returnarr[0] = positionX;
//   returnarr[1] = positionY;
//   returnarr[2] = angle;
//
//   return returnarr;
// }


// cv::Point ImageProcessor::getpose(){
//   return x0;
//
// }
