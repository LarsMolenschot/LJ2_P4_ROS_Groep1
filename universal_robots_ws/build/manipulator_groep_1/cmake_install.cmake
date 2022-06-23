# Install script for directory: /home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/src/my_universal_robots/manipulator_groep_1

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install" TYPE PROGRAM FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install" TYPE PROGRAM FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/setup.bash;/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install" TYPE FILE FILES
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/setup.bash"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/setup.sh;/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install" TYPE FILE FILES
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/setup.sh"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/setup.zsh;/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install" TYPE FILE FILES
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/setup.zsh"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install" TYPE FILE FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/.rosinstall")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/manipulator_groep_1/action" TYPE FILE FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/src/my_universal_robots/manipulator_groep_1/action/control_robot.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/manipulator_groep_1/msg" TYPE FILE FILES
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/manipulator_groep_1/msg/control_robotAction.msg"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/manipulator_groep_1/msg/control_robotActionGoal.msg"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/manipulator_groep_1/msg/control_robotActionResult.msg"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/manipulator_groep_1/msg/control_robotActionFeedback.msg"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/manipulator_groep_1/msg/control_robotGoal.msg"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/manipulator_groep_1/msg/control_robotResult.msg"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/manipulator_groep_1/msg/control_robotFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/manipulator_groep_1/cmake" TYPE FILE FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/manipulator_groep_1-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/include/manipulator_groep_1")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/roseus/ros/manipulator_groep_1")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/common-lisp/ros/manipulator_groep_1")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/share/gennodejs/ros/manipulator_groep_1")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/lib/python2.7/dist-packages/manipulator_groep_1")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/devel/.private/manipulator_groep_1/lib/python2.7/dist-packages/manipulator_groep_1")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/manipulator_groep_1.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/manipulator_groep_1/cmake" TYPE FILE FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/manipulator_groep_1-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/manipulator_groep_1/cmake" TYPE FILE FILES
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/manipulator_groep_1Config.cmake"
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/catkin_generated/installspace/manipulator_groep_1Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/manipulator_groep_1" TYPE FILE FILES "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/src/my_universal_robots/manipulator_groep_1/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/manipulator_groep_1/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
