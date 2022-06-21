execute_process(COMMAND "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/rosserial_arduino/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/rosserial_arduino/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
