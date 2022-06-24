; Auto-generated. Do not edit!


(cl:in-package vision_message-msg)


;//! \htmlinclude vision_msg.msg.html

(cl:defclass <vision_msg> (roslisp-msg-protocol:ros-message)
  ((vision_positie
    :reader vision_positie
    :initarg :vision_positie
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (object_naam
    :reader object_naam
    :initarg :object_naam
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String)))
)

(cl:defclass vision_msg (<vision_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vision_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vision_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision_message-msg:<vision_msg> is deprecated: use vision_message-msg:vision_msg instead.")))

(cl:ensure-generic-function 'vision_positie-val :lambda-list '(m))
(cl:defmethod vision_positie-val ((m <vision_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_message-msg:vision_positie-val is deprecated.  Use vision_message-msg:vision_positie instead.")
  (vision_positie m))

(cl:ensure-generic-function 'object_naam-val :lambda-list '(m))
(cl:defmethod object_naam-val ((m <vision_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_message-msg:object_naam-val is deprecated.  Use vision_message-msg:object_naam instead.")
  (object_naam m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vision_msg>) ostream)
  "Serializes a message object of type '<vision_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vision_positie) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'object_naam) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vision_msg>) istream)
  "Deserializes a message object of type '<vision_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vision_positie) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'object_naam) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vision_msg>)))
  "Returns string type for a message object of type '<vision_msg>"
  "vision_message/vision_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vision_msg)))
  "Returns string type for a message object of type 'vision_msg"
  "vision_message/vision_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vision_msg>)))
  "Returns md5sum for a message object of type '<vision_msg>"
  "52237def187f2c19b70d40056e5fd89f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vision_msg)))
  "Returns md5sum for a message object of type 'vision_msg"
  "52237def187f2c19b70d40056e5fd89f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vision_msg>)))
  "Returns full string definition for message of type '<vision_msg>"
  (cl:format cl:nil "geometry_msgs/Pose vision_positie~%std_msgs/String object_naam~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vision_msg)))
  "Returns full string definition for message of type 'vision_msg"
  (cl:format cl:nil "geometry_msgs/Pose vision_positie~%std_msgs/String object_naam~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vision_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vision_positie))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'object_naam))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vision_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'vision_msg
    (cl:cons ':vision_positie (vision_positie msg))
    (cl:cons ':object_naam (object_naam msg))
))
