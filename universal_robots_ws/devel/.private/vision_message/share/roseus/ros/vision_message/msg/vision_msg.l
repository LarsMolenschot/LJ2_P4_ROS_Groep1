;; Auto-generated. Do not edit!


(when (boundp 'vision_message::vision_msg)
  (if (not (find-package "VISION_MESSAGE"))
    (make-package "VISION_MESSAGE"))
  (shadow 'vision_msg (find-package "VISION_MESSAGE")))
(unless (find-package "VISION_MESSAGE::VISION_MSG")
  (make-package "VISION_MESSAGE::VISION_MSG"))

(in-package "ROS")
;;//! \htmlinclude vision_msg.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass vision_message::vision_msg
  :super ros::object
  :slots (_vision_positie _object_naam ))

(defmethod vision_message::vision_msg
  (:init
   (&key
    ((:vision_positie __vision_positie) (instance geometry_msgs::Pose :init))
    ((:object_naam __object_naam) (instance std_msgs::String :init))
    )
   (send-super :init)
   (setq _vision_positie __vision_positie)
   (setq _object_naam __object_naam)
   self)
  (:vision_positie
   (&rest __vision_positie)
   (if (keywordp (car __vision_positie))
       (send* _vision_positie __vision_positie)
     (progn
       (if __vision_positie (setq _vision_positie (car __vision_positie)))
       _vision_positie)))
  (:object_naam
   (&rest __object_naam)
   (if (keywordp (car __object_naam))
       (send* _object_naam __object_naam)
     (progn
       (if __object_naam (setq _object_naam (car __object_naam)))
       _object_naam)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose _vision_positie
    (send _vision_positie :serialization-length)
    ;; std_msgs/String _object_naam
    (send _object_naam :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose _vision_positie
       (send _vision_positie :serialize s)
     ;; std_msgs/String _object_naam
       (send _object_naam :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose _vision_positie
     (send _vision_positie :deserialize buf ptr-) (incf ptr- (send _vision_positie :serialization-length))
   ;; std_msgs/String _object_naam
     (send _object_naam :deserialize buf ptr-) (incf ptr- (send _object_naam :serialization-length))
   ;;
   self)
  )

(setf (get vision_message::vision_msg :md5sum-) "52237def187f2c19b70d40056e5fd89f")
(setf (get vision_message::vision_msg :datatype-) "vision_message/vision_msg")
(setf (get vision_message::vision_msg :definition-)
      "geometry_msgs/Pose vision_positie
std_msgs/String object_naam

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: std_msgs/String
string data

")



(provide :vision_message/vision_msg "52237def187f2c19b70d40056e5fd89f")


