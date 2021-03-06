// Generated by gencpp from file manipulator_groep_1/control_robotFeedback.msg
// DO NOT EDIT!


#ifndef MANIPULATOR_GROEP_1_MESSAGE_CONTROL_ROBOTFEEDBACK_H
#define MANIPULATOR_GROEP_1_MESSAGE_CONTROL_ROBOTFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace manipulator_groep_1
{
template <class ContainerAllocator>
struct control_robotFeedback_
{
  typedef control_robotFeedback_<ContainerAllocator> Type;

  control_robotFeedback_()
    {
    }
  control_robotFeedback_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct control_robotFeedback_

typedef ::manipulator_groep_1::control_robotFeedback_<std::allocator<void> > control_robotFeedback;

typedef boost::shared_ptr< ::manipulator_groep_1::control_robotFeedback > control_robotFeedbackPtr;
typedef boost::shared_ptr< ::manipulator_groep_1::control_robotFeedback const> control_robotFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace manipulator_groep_1

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "manipulator_groep_1/control_robotFeedback";
  }

  static const char* value(const ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#feedback\n"
"\n"
"\n"
;
  }

  static const char* value(const ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct control_robotFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::manipulator_groep_1::control_robotFeedback_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // MANIPULATOR_GROEP_1_MESSAGE_CONTROL_ROBOTFEEDBACK_H
