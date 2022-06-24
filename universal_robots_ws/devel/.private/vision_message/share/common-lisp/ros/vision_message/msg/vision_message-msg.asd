
(cl:in-package :asdf)

(defsystem "vision_message-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "vision_msg" :depends-on ("_package_vision_msg"))
    (:file "_package_vision_msg" :depends-on ("_package"))
  ))