#ifndef COLOR_DETECTOR_H
#define COLOR_DETECTOR_H
//#include <mainwindow.h>


 
class color_detector
{
public:
    color_detector(cv::Mat g){
    _g=g;
}
cv::Mat returnimage();

private:
cv::Mat _g{};
};

#endif // COLOR_DETECTOR_H
