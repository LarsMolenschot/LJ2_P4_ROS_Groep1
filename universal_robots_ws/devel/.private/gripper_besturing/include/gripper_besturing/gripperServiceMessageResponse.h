// Generated by gencpp from file gripper_besturing/gripperServiceMessageResponse.msg
// DO NOT EDIT!


#ifndef GRIPPER_BESTURING_MESSAGE_GRIPPERSERVICEMESSAGERESPONSE_H
#define GRIPPER_BESTURING_MESSAGE_GRIPPERSERVICEMESSAGERESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace gripper_besturing
{
template <class ContainerAllocator>
struct gripperServiceMessageResponse_
{
  typedef gripperServiceMessageResponse_<ContainerAllocator> Type;

  gripperServiceMessageResponse_()
    : succes(false)
    , found_object(false)
    , error_nummer(0)
    , error_tekst()  {
    }
  gripperServiceMessageResponse_(const ContainerAllocator& _alloc)
    : succes(false)
    , found_object(false)
    , error_nummer(0)
    , error_tekst(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _succes_type;
  _succes_type succes;

   typedef uint8_t _found_object_type;
  _found_object_type found_object;

   typedef int64_t _error_nummer_type;
  _error_nummer_type error_nummer;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _error_tekst_type;
  _error_tekst_type error_tekst;





  typedef boost::shared_ptr< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> const> ConstPtr;

}; // struct gripperServiceMessageResponse_

typedef ::gripper_besturing::gripperServiceMessageResponse_<std::allocator<void> > gripperServiceMessageResponse;

typedef boost::shared_ptr< ::gripper_besturing::gripperServiceMessageResponse > gripperServiceMessageResponsePtr;
typedef boost::shared_ptr< ::gripper_besturing::gripperServiceMessageResponse const> gripperServiceMessageResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator1> & lhs, const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator2> & rhs)
{
  return lhs.succes == rhs.succes &&
    lhs.found_object == rhs.found_object &&
    lhs.error_nummer == rhs.error_nummer &&
    lhs.error_tekst == rhs.error_tekst;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator1> & lhs, const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace gripper_besturing

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ef8c5718b3a04b760dd07273c62bce7f";
  }

  static const char* value(const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xef8c5718b3a04b76ULL;
  static const uint64_t static_value2 = 0x0dd07273c62bce7fULL;
};

template<class ContainerAllocator>
struct DataType< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "gripper_besturing/gripperServiceMessageResponse";
  }

  static const char* value(const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool succes\n"
"bool found_object\n"
"int64 error_nummer\n"
"string error_tekst\n"
"\n"
;
  }

  static const char* value(const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.succes);
      stream.next(m.found_object);
      stream.next(m.error_nummer);
      stream.next(m.error_tekst);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct gripperServiceMessageResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::gripper_besturing::gripperServiceMessageResponse_<ContainerAllocator>& v)
  {
    s << indent << "succes: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.succes);
    s << indent << "found_object: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.found_object);
    s << indent << "error_nummer: ";
    Printer<int64_t>::stream(s, indent + "  ", v.error_nummer);
    s << indent << "error_tekst: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.error_tekst);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRIPPER_BESTURING_MESSAGE_GRIPPERSERVICEMESSAGERESPONSE_H