#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/src/my_moveit_demo/my_flexbe_behaviors/my_behavior_flexbe_states"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/lib/python2.7/dist-packages:/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/my_behavior_flexbe_states/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/my_behavior_flexbe_states" \
    "/usr/bin/python2" \
    "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/src/my_moveit_demo/my_flexbe_behaviors/my_behavior_flexbe_states/setup.py" \
     \
    build --build-base "/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/build/my_behavior_flexbe_states" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install" --install-scripts="/home/student/LJ2_P4_ROS_Groep1/universal_robots_ws/install/bin"
