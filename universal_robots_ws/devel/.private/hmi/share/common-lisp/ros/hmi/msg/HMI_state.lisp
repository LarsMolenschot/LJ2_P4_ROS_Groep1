; Auto-generated. Do not edit!


(cl:in-package hmi-msg)


;//! \htmlinclude HMI_state.msg.html

(cl:defclass <HMI_state> (roslisp-msg-protocol:ros-message)
  ((programstate
    :reader programstate
    :initarg :programstate
    :type cl:string
    :initform "")
   (programtype
    :reader programtype
    :initarg :programtype
    :type cl:string
    :initform "")
   (stop
    :reader stop
    :initarg :stop
    :type cl:boolean
    :initform cl:nil)
   (noodstop
    :reader noodstop
    :initarg :noodstop
    :type cl:boolean
    :initform cl:nil)
   (stopreset
    :reader stopreset
    :initarg :stopreset
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass HMI_state (<HMI_state>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HMI_state>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HMI_state)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hmi-msg:<HMI_state> is deprecated: use hmi-msg:HMI_state instead.")))

(cl:ensure-generic-function 'programstate-val :lambda-list '(m))
(cl:defmethod programstate-val ((m <HMI_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hmi-msg:programstate-val is deprecated.  Use hmi-msg:programstate instead.")
  (programstate m))

(cl:ensure-generic-function 'programtype-val :lambda-list '(m))
(cl:defmethod programtype-val ((m <HMI_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hmi-msg:programtype-val is deprecated.  Use hmi-msg:programtype instead.")
  (programtype m))

(cl:ensure-generic-function 'stop-val :lambda-list '(m))
(cl:defmethod stop-val ((m <HMI_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hmi-msg:stop-val is deprecated.  Use hmi-msg:stop instead.")
  (stop m))

(cl:ensure-generic-function 'noodstop-val :lambda-list '(m))
(cl:defmethod noodstop-val ((m <HMI_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hmi-msg:noodstop-val is deprecated.  Use hmi-msg:noodstop instead.")
  (noodstop m))

(cl:ensure-generic-function 'stopreset-val :lambda-list '(m))
(cl:defmethod stopreset-val ((m <HMI_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hmi-msg:stopreset-val is deprecated.  Use hmi-msg:stopreset instead.")
  (stopreset m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HMI_state>) ostream)
  "Serializes a message object of type '<HMI_state>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'programstate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'programstate))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'programtype))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'programtype))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'stop) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'noodstop) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'stopreset) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HMI_state>) istream)
  "Deserializes a message object of type '<HMI_state>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'programstate) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'programstate) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'programtype) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'programtype) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'stop) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'noodstop) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'stopreset) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HMI_state>)))
  "Returns string type for a message object of type '<HMI_state>"
  "hmi/HMI_state")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HMI_state)))
  "Returns string type for a message object of type 'HMI_state"
  "hmi/HMI_state")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HMI_state>)))
  "Returns md5sum for a message object of type '<HMI_state>"
  "12d2ece259040b0ded5a9b3526331ec2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HMI_state)))
  "Returns md5sum for a message object of type 'HMI_state"
  "12d2ece259040b0ded5a9b3526331ec2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HMI_state>)))
  "Returns full string definition for message of type '<HMI_state>"
  (cl:format cl:nil "string programstate~%string programtype~%bool stop~%bool noodstop~%bool stopreset~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HMI_state)))
  "Returns full string definition for message of type 'HMI_state"
  (cl:format cl:nil "string programstate~%string programtype~%bool stop~%bool noodstop~%bool stopreset~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HMI_state>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'programstate))
     4 (cl:length (cl:slot-value msg 'programtype))
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HMI_state>))
  "Converts a ROS message object to a list"
  (cl:list 'HMI_state
    (cl:cons ':programstate (programstate msg))
    (cl:cons ':programtype (programtype msg))
    (cl:cons ':stop (stop msg))
    (cl:cons ':noodstop (noodstop msg))
    (cl:cons ':stopreset (stopreset msg))
))
