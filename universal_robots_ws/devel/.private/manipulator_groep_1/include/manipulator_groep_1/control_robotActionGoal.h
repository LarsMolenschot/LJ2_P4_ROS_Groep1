// Generated by gencpp from file manipulator_groep_1/control_robotActionGoal.msg
// DO NOT EDIT!


#ifndef MANIPULATOR_GROEP_1_MESSAGE_CONTROL_ROBOTACTIONGOAL_H
#define MANIPULATOR_GROEP_1_MESSAGE_CONTROL_ROBOTACTIONGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <actionlib_msgs/GoalID.h>
#include <manipulator_groep_1/control_robotGoal.h>

namespace manipulator_groep_1
{
template <class ContainerAllocator>
struct control_robotActionGoal_
{
  typedef control_robotActionGoal_<ContainerAllocator> Type;

  control_robotActionGoal_()
    : header()
    , goal_id()
    , goal()  {
    }
  control_robotActionGoal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , goal_id(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
  _goal_id_type goal_id;

   typedef  ::manipulator_groep_1::control_robotGoal_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct control_robotActionGoal_

typedef ::manipulator_groep_1::control_robotActionGoal_<std::allocator<void> > control_robotActionGoal;

typedef boost::shared_ptr< ::manipulator_groep_1::control_robotActionGoal > control_robotActionGoalPtr;
typedef boost::shared_ptr< ::manipulator_groep_1::control_robotActionGoal const> control_robotActionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator1> & lhs, const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.goal_id == rhs.goal_id &&
    lhs.goal == rhs.goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator1> & lhs, const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace manipulator_groep_1

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6ad9893a5777d22ec6e93159fbef03b1";
  }

  static const char* value(const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6ad9893a5777d22eULL;
  static const uint64_t static_value2 = 0xc6e93159fbef03b1ULL;
};

template<class ContainerAllocator>
struct DataType< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "manipulator_groep_1/control_robotActionGoal";
  }

  static const char* value(const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"control_robotGoal goal\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: manipulator_groep_1/control_robotGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#goal\n"
"\n"
"geometry_msgs/Pose lineairpose\n"
"\n"
"std_msgs/String position\n"
"\n"
"std_msgs/Bool mode\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/String\n"
"string data\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Bool\n"
"bool data\n"
;
  }

  static const char* value(const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.goal_id);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct control_robotActionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::manipulator_groep_1::control_robotActionGoal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
    s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::manipulator_groep_1::control_robotGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MANIPULATOR_GROEP_1_MESSAGE_CONTROL_ROBOTACTIONGOAL_H
