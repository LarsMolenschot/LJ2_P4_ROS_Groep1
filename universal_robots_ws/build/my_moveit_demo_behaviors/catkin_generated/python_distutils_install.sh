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

echo_and_run cd "/home/student/universal_robots_ws/src/my_moveit_demo/my_moveit_demo_flexbe_behaviors/my_demo_behaviors"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/student/universal_robots_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/student/universal_robots_ws/install/lib/python2.7/dist-packages:/home/student/universal_robots_ws/build/my_moveit_demo_behaviors/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/student/universal_robots_ws/build/my_moveit_demo_behaviors" \
    "/usr/bin/python2" \
    "/home/student/universal_robots_ws/src/my_moveit_demo/my_moveit_demo_flexbe_behaviors/my_demo_behaviors/setup.py" \
     \
    build --build-base "/home/student/universal_robots_ws/build/my_moveit_demo_behaviors" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/student/universal_robots_ws/install" --install-scripts="/home/student/universal_robots_ws/install/bin"
