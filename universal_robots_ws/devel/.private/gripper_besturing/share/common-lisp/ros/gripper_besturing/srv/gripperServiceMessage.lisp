; Auto-generated. Do not edit!


(cl:in-package gripper_besturing-srv)


;//! \htmlinclude gripperServiceMessage-request.msg.html

(cl:defclass <gripperServiceMessage-request> (roslisp-msg-protocol:ros-message)
  ((open_of_dicht_gripper
    :reader open_of_dicht_gripper
    :initarg :open_of_dicht_gripper
    :type cl:string
    :initform "")
   (gripper_opstarten
    :reader gripper_opstarten
    :initarg :gripper_opstarten
    :type cl:integer
    :initform 0))
)

(cl:defclass gripperServiceMessage-request (<gripperServiceMessage-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gripperServiceMessage-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gripperServiceMessage-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gripper_besturing-srv:<gripperServiceMessage-request> is deprecated: use gripper_besturing-srv:gripperServiceMessage-request instead.")))

(cl:ensure-generic-function 'open_of_dicht_gripper-val :lambda-list '(m))
(cl:defmethod open_of_dicht_gripper-val ((m <gripperServiceMessage-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper_besturing-srv:open_of_dicht_gripper-val is deprecated.  Use gripper_besturing-srv:open_of_dicht_gripper instead.")
  (open_of_dicht_gripper m))

(cl:ensure-generic-function 'gripper_opstarten-val :lambda-list '(m))
(cl:defmethod gripper_opstarten-val ((m <gripperServiceMessage-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper_besturing-srv:gripper_opstarten-val is deprecated.  Use gripper_besturing-srv:gripper_opstarten instead.")
  (gripper_opstarten m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gripperServiceMessage-request>) ostream)
  "Serializes a message object of type '<gripperServiceMessage-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'open_of_dicht_gripper))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'open_of_dicht_gripper))
  (cl:let* ((signed (cl:slot-value msg 'gripper_opstarten)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gripperServiceMessage-request>) istream)
  "Deserializes a message object of type '<gripperServiceMessage-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'open_of_dicht_gripper) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'open_of_dicht_gripper) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gripper_opstarten) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gripperServiceMessage-request>)))
  "Returns string type for a service object of type '<gripperServiceMessage-request>"
  "gripper_besturing/gripperServiceMessageRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gripperServiceMessage-request)))
  "Returns string type for a service object of type 'gripperServiceMessage-request"
  "gripper_besturing/gripperServiceMessageRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gripperServiceMessage-request>)))
  "Returns md5sum for a message object of type '<gripperServiceMessage-request>"
  "c9aa0baea7a9c0e9e50fcc3986fdf213")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gripperServiceMessage-request)))
  "Returns md5sum for a message object of type 'gripperServiceMessage-request"
  "c9aa0baea7a9c0e9e50fcc3986fdf213")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gripperServiceMessage-request>)))
  "Returns full string definition for message of type '<gripperServiceMessage-request>"
  (cl:format cl:nil "string open_of_dicht_gripper~%int64 gripper_opstarten~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gripperServiceMessage-request)))
  "Returns full string definition for message of type 'gripperServiceMessage-request"
  (cl:format cl:nil "string open_of_dicht_gripper~%int64 gripper_opstarten~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gripperServiceMessage-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'open_of_dicht_gripper))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gripperServiceMessage-request>))
  "Converts a ROS message object to a list"
  (cl:list 'gripperServiceMessage-request
    (cl:cons ':open_of_dicht_gripper (open_of_dicht_gripper msg))
    (cl:cons ':gripper_opstarten (gripper_opstarten msg))
))
;//! \htmlinclude gripperServiceMessage-response.msg.html

(cl:defclass <gripperServiceMessage-response> (roslisp-msg-protocol:ros-message)
  ((succes
    :reader succes
    :initarg :succes
    :type cl:boolean
    :initform cl:nil)
   (found_object
    :reader found_object
    :initarg :found_object
    :type cl:boolean
    :initform cl:nil)
   (error_nummer
    :reader error_nummer
    :initarg :error_nummer
    :type cl:integer
    :initform 0)
   (error_tekst
    :reader error_tekst
    :initarg :error_tekst
    :type cl:string
    :initform ""))
)

(cl:defclass gripperServiceMessage-response (<gripperServiceMessage-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gripperServiceMessage-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gripperServiceMessage-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gripper_besturing-srv:<gripperServiceMessage-response> is deprecated: use gripper_besturing-srv:gripperServiceMessage-response instead.")))

(cl:ensure-generic-function 'succes-val :lambda-list '(m))
(cl:defmethod succes-val ((m <gripperServiceMessage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper_besturing-srv:succes-val is deprecated.  Use gripper_besturing-srv:succes instead.")
  (succes m))

(cl:ensure-generic-function 'found_object-val :lambda-list '(m))
(cl:defmethod found_object-val ((m <gripperServiceMessage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper_besturing-srv:found_object-val is deprecated.  Use gripper_besturing-srv:found_object instead.")
  (found_object m))

(cl:ensure-generic-function 'error_nummer-val :lambda-list '(m))
(cl:defmethod error_nummer-val ((m <gripperServiceMessage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper_besturing-srv:error_nummer-val is deprecated.  Use gripper_besturing-srv:error_nummer instead.")
  (error_nummer m))

(cl:ensure-generic-function 'error_tekst-val :lambda-list '(m))
(cl:defmethod error_tekst-val ((m <gripperServiceMessage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper_besturing-srv:error_tekst-val is deprecated.  Use gripper_besturing-srv:error_tekst instead.")
  (error_tekst m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gripperServiceMessage-response>) ostream)
  "Serializes a message object of type '<gripperServiceMessage-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'succes) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'found_object) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'error_nummer)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'error_tekst))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'error_tekst))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gripperServiceMessage-response>) istream)
  "Deserializes a message object of type '<gripperServiceMessage-response>"
    (cl:setf (cl:slot-value msg 'succes) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'found_object) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'error_nummer) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'error_tekst) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'error_tekst) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gripperServiceMessage-response>)))
  "Returns string type for a service object of type '<gripperServiceMessage-response>"
  "gripper_besturing/gripperServiceMessageResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gripperServiceMessage-response)))
  "Returns string type for a service object of type 'gripperServiceMessage-response"
  "gripper_besturing/gripperServiceMessageResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gripperServiceMessage-response>)))
  "Returns md5sum for a message object of type '<gripperServiceMessage-response>"
  "c9aa0baea7a9c0e9e50fcc3986fdf213")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gripperServiceMessage-response)))
  "Returns md5sum for a message object of type 'gripperServiceMessage-response"
  "c9aa0baea7a9c0e9e50fcc3986fdf213")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gripperServiceMessage-response>)))
  "Returns full string definition for message of type '<gripperServiceMessage-response>"
  (cl:format cl:nil "bool succes~%bool found_object~%int64 error_nummer~%string error_tekst~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gripperServiceMessage-response)))
  "Returns full string definition for message of type 'gripperServiceMessage-response"
  (cl:format cl:nil "bool succes~%bool found_object~%int64 error_nummer~%string error_tekst~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gripperServiceMessage-response>))
  (cl:+ 0
     1
     1
     8
     4 (cl:length (cl:slot-value msg 'error_tekst))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gripperServiceMessage-response>))
  "Converts a ROS message object to a list"
  (cl:list 'gripperServiceMessage-response
    (cl:cons ':succes (succes msg))
    (cl:cons ':found_object (found_object msg))
    (cl:cons ':error_nummer (error_nummer msg))
    (cl:cons ':error_tekst (error_tekst msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'gripperServiceMessage)))
  'gripperServiceMessage-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'gripperServiceMessage)))
  'gripperServiceMessage-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gripperServiceMessage)))
  "Returns string type for a service object of type '<gripperServiceMessage>"
  "gripper_besturing/gripperServiceMessage")