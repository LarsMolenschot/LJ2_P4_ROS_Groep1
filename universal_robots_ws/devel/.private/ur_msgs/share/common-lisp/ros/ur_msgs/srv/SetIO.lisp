; Auto-generated. Do not edit!


(cl:in-package ur_msgs-srv)


;//! \htmlinclude SetIO-request.msg.html

(cl:defclass <SetIO-request> (roslisp-msg-protocol:ros-message)
  ((fun
    :reader fun
    :initarg :fun
    :type cl:fixnum
    :initform 0)
   (pin
    :reader pin
    :initarg :pin
    :type cl:fixnum
    :initform 0)
   (state
    :reader state
    :initarg :state
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetIO-request (<SetIO-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetIO-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetIO-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<SetIO-request> is deprecated: use ur_msgs-srv:SetIO-request instead.")))

(cl:ensure-generic-function 'fun-val :lambda-list '(m))
(cl:defmethod fun-val ((m <SetIO-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:fun-val is deprecated.  Use ur_msgs-srv:fun instead.")
  (fun m))

(cl:ensure-generic-function 'pin-val :lambda-list '(m))
(cl:defmethod pin-val ((m <SetIO-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:pin-val is deprecated.  Use ur_msgs-srv:pin instead.")
  (pin m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <SetIO-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:state-val is deprecated.  Use ur_msgs-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<SetIO-request>)))
    "Constants for message type '<SetIO-request>"
  '((:PIN_AOUT0 . 0)
    (:PIN_AOUT1 . 1)
    (:PIN_DOUT0 . 0)
    (:PIN_DOUT1 . 1)
    (:PIN_DOUT2 . 2)
    (:PIN_DOUT3 . 3)
    (:PIN_DOUT4 . 4)
    (:PIN_DOUT5 . 5)
    (:PIN_DOUT6 . 6)
    (:PIN_DOUT7 . 7)
    (:PIN_CONF_OUT0 . 8)
    (:PIN_CONF_OUT1 . 9)
    (:PIN_CONF_OUT2 . 10)
    (:PIN_CONF_OUT3 . 11)
    (:PIN_CONF_OUT4 . 12)
    (:PIN_CONF_OUT5 . 13)
    (:PIN_CONF_OUT6 . 14)
    (:PIN_CONF_OUT7 . 15)
    (:PIN_TOOL_DOUT0 . 16)
    (:PIN_TOOL_DOUT1 . 17)
    (:FUN_SET_DIGITAL_OUT . 1)
    (:FUN_SET_FLAG . 2)
    (:FUN_SET_ANALOG_OUT . 3)
    (:FUN_SET_TOOL_VOLTAGE . 4)
    (:STATE_OFF . 0)
    (:STATE_ON . 1)
    (:STATE_TOOL_VOLTAGE_0V . 0)
    (:STATE_TOOL_VOLTAGE_12V . 12)
    (:STATE_TOOL_VOLTAGE_24V . 24))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'SetIO-request)))
    "Constants for message type 'SetIO-request"
  '((:PIN_AOUT0 . 0)
    (:PIN_AOUT1 . 1)
    (:PIN_DOUT0 . 0)
    (:PIN_DOUT1 . 1)
    (:PIN_DOUT2 . 2)
    (:PIN_DOUT3 . 3)
    (:PIN_DOUT4 . 4)
    (:PIN_DOUT5 . 5)
    (:PIN_DOUT6 . 6)
    (:PIN_DOUT7 . 7)
    (:PIN_CONF_OUT0 . 8)
    (:PIN_CONF_OUT1 . 9)
    (:PIN_CONF_OUT2 . 10)
    (:PIN_CONF_OUT3 . 11)
    (:PIN_CONF_OUT4 . 12)
    (:PIN_CONF_OUT5 . 13)
    (:PIN_CONF_OUT6 . 14)
    (:PIN_CONF_OUT7 . 15)
    (:PIN_TOOL_DOUT0 . 16)
    (:PIN_TOOL_DOUT1 . 17)
    (:FUN_SET_DIGITAL_OUT . 1)
    (:FUN_SET_FLAG . 2)
    (:FUN_SET_ANALOG_OUT . 3)
    (:FUN_SET_TOOL_VOLTAGE . 4)
    (:STATE_OFF . 0)
    (:STATE_ON . 1)
    (:STATE_TOOL_VOLTAGE_0V . 0)
    (:STATE_TOOL_VOLTAGE_12V . 12)
    (:STATE_TOOL_VOLTAGE_24V . 24))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetIO-request>) ostream)
  "Serializes a message object of type '<SetIO-request>"
  (cl:let* ((signed (cl:slot-value msg 'fun)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'pin)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetIO-request>) istream)
  "Deserializes a message object of type '<SetIO-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fun) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pin) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'state) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetIO-request>)))
  "Returns string type for a service object of type '<SetIO-request>"
  "ur_msgs/SetIORequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetIO-request)))
  "Returns string type for a service object of type 'SetIO-request"
  "ur_msgs/SetIORequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetIO-request>)))
  "Returns md5sum for a message object of type '<SetIO-request>"
  "f539fc0b1a42859fb186a5aaba22d4b0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetIO-request)))
  "Returns md5sum for a message object of type 'SetIO-request"
  "f539fc0b1a42859fb186a5aaba22d4b0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetIO-request>)))
  "Returns full string definition for message of type '<SetIO-request>"
  (cl:format cl:nil "# Service allows setting digital (DIO) and analog (AIO) IO, as well as flags~%# and configuring tool voltage.~%#~%# This service has three request fields (see below).~%#~%# When setting DIO or AIO pins to new values:~%#~%#  fun    The function to perform~%#  pin    Numeric ID of the pin to set, see constants definition below~%#  state  Desired pin state (signal level for analog or STATE_(ON|OFF) for DIO and flags)~%#~%# When configuring tool voltage:~%#~%#  fun    Set to FUN_SET_TOOL_VOLTAGE~%#  pin    Ignored~%#  state  Desired tool voltage (use STATE_TOOL_VOLTAGE constants)~%~%# constants~%# pin mapping~%# analog out~%int8 PIN_AOUT0 = 0~%int8 PIN_AOUT1 = 1~%~%# digital out~%int8 PIN_DOUT0 = 0~%int8 PIN_DOUT1 = 1~%int8 PIN_DOUT2 = 2~%int8 PIN_DOUT3 = 3~%int8 PIN_DOUT4 = 4~%int8 PIN_DOUT5 = 5~%int8 PIN_DOUT6 = 6~%int8 PIN_DOUT7 = 7~%~%# configurable out~%int8 PIN_CONF_OUT0 = 8~%int8 PIN_CONF_OUT1 = 9~%int8 PIN_CONF_OUT2 = 10~%int8 PIN_CONF_OUT3 = 11~%int8 PIN_CONF_OUT4 = 12~%int8 PIN_CONF_OUT5 = 13~%int8 PIN_CONF_OUT6 = 14~%int8 PIN_CONF_OUT7 = 15~%~%# digital tool output~%int8 PIN_TOOL_DOUT0 = 16~%int8 PIN_TOOL_DOUT1 = 17~%~%# valid function values~%#~%# Note: 'fun' is short for 'function' (ie: the function the service should perform).~%int8 FUN_SET_DIGITAL_OUT = 1~%int8 FUN_SET_FLAG = 2~%int8 FUN_SET_ANALOG_OUT = 3~%int8 FUN_SET_TOOL_VOLTAGE = 4~%~%# valid values for 'state' when setting digital IO or flags~%int8 STATE_OFF = 0~%int8 STATE_ON = 1~%~%# valid 'state' values when setting tool voltage~%int8 STATE_TOOL_VOLTAGE_0V = 0~%int8 STATE_TOOL_VOLTAGE_12V = 12~%int8 STATE_TOOL_VOLTAGE_24V = 24~%~%# request fields~%int8 fun~%int8 pin~%float32 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetIO-request)))
  "Returns full string definition for message of type 'SetIO-request"
  (cl:format cl:nil "# Service allows setting digital (DIO) and analog (AIO) IO, as well as flags~%# and configuring tool voltage.~%#~%# This service has three request fields (see below).~%#~%# When setting DIO or AIO pins to new values:~%#~%#  fun    The function to perform~%#  pin    Numeric ID of the pin to set, see constants definition below~%#  state  Desired pin state (signal level for analog or STATE_(ON|OFF) for DIO and flags)~%#~%# When configuring tool voltage:~%#~%#  fun    Set to FUN_SET_TOOL_VOLTAGE~%#  pin    Ignored~%#  state  Desired tool voltage (use STATE_TOOL_VOLTAGE constants)~%~%# constants~%# pin mapping~%# analog out~%int8 PIN_AOUT0 = 0~%int8 PIN_AOUT1 = 1~%~%# digital out~%int8 PIN_DOUT0 = 0~%int8 PIN_DOUT1 = 1~%int8 PIN_DOUT2 = 2~%int8 PIN_DOUT3 = 3~%int8 PIN_DOUT4 = 4~%int8 PIN_DOUT5 = 5~%int8 PIN_DOUT6 = 6~%int8 PIN_DOUT7 = 7~%~%# configurable out~%int8 PIN_CONF_OUT0 = 8~%int8 PIN_CONF_OUT1 = 9~%int8 PIN_CONF_OUT2 = 10~%int8 PIN_CONF_OUT3 = 11~%int8 PIN_CONF_OUT4 = 12~%int8 PIN_CONF_OUT5 = 13~%int8 PIN_CONF_OUT6 = 14~%int8 PIN_CONF_OUT7 = 15~%~%# digital tool output~%int8 PIN_TOOL_DOUT0 = 16~%int8 PIN_TOOL_DOUT1 = 17~%~%# valid function values~%#~%# Note: 'fun' is short for 'function' (ie: the function the service should perform).~%int8 FUN_SET_DIGITAL_OUT = 1~%int8 FUN_SET_FLAG = 2~%int8 FUN_SET_ANALOG_OUT = 3~%int8 FUN_SET_TOOL_VOLTAGE = 4~%~%# valid values for 'state' when setting digital IO or flags~%int8 STATE_OFF = 0~%int8 STATE_ON = 1~%~%# valid 'state' values when setting tool voltage~%int8 STATE_TOOL_VOLTAGE_0V = 0~%int8 STATE_TOOL_VOLTAGE_12V = 12~%int8 STATE_TOOL_VOLTAGE_24V = 24~%~%# request fields~%int8 fun~%int8 pin~%float32 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetIO-request>))
  (cl:+ 0
     1
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetIO-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetIO-request
    (cl:cons ':fun (fun msg))
    (cl:cons ':pin (pin msg))
    (cl:cons ':state (state msg))
))
;//! \htmlinclude SetIO-response.msg.html

(cl:defclass <SetIO-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetIO-response (<SetIO-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetIO-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetIO-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<SetIO-response> is deprecated: use ur_msgs-srv:SetIO-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetIO-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:success-val is deprecated.  Use ur_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetIO-response>) ostream)
  "Serializes a message object of type '<SetIO-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetIO-response>) istream)
  "Deserializes a message object of type '<SetIO-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetIO-response>)))
  "Returns string type for a service object of type '<SetIO-response>"
  "ur_msgs/SetIOResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetIO-response)))
  "Returns string type for a service object of type 'SetIO-response"
  "ur_msgs/SetIOResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetIO-response>)))
  "Returns md5sum for a message object of type '<SetIO-response>"
  "f539fc0b1a42859fb186a5aaba22d4b0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetIO-response)))
  "Returns md5sum for a message object of type 'SetIO-response"
  "f539fc0b1a42859fb186a5aaba22d4b0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetIO-response>)))
  "Returns full string definition for message of type '<SetIO-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetIO-response)))
  "Returns full string definition for message of type 'SetIO-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetIO-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetIO-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetIO-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetIO)))
  'SetIO-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetIO)))
  'SetIO-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetIO)))
  "Returns string type for a service object of type '<SetIO>"
  "ur_msgs/SetIO")