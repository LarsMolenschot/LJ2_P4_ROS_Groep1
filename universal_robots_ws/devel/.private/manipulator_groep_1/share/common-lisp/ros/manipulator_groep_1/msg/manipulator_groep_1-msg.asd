
(cl:in-package :asdf)

(defsystem "manipulator_groep_1-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "control_robotAction" :depends-on ("_package_control_robotAction"))
    (:file "_package_control_robotAction" :depends-on ("_package"))
    (:file "control_robotActionFeedback" :depends-on ("_package_control_robotActionFeedback"))
    (:file "_package_control_robotActionFeedback" :depends-on ("_package"))
    (:file "control_robotActionGoal" :depends-on ("_package_control_robotActionGoal"))
    (:file "_package_control_robotActionGoal" :depends-on ("_package"))
    (:file "control_robotActionResult" :depends-on ("_package_control_robotActionResult"))
    (:file "_package_control_robotActionResult" :depends-on ("_package"))
    (:file "control_robotFeedback" :depends-on ("_package_control_robotFeedback"))
    (:file "_package_control_robotFeedback" :depends-on ("_package"))
    (:file "control_robotGoal" :depends-on ("_package_control_robotGoal"))
    (:file "_package_control_robotGoal" :depends-on ("_package"))
    (:file "control_robotResult" :depends-on ("_package_control_robotResult"))
    (:file "_package_control_robotResult" :depends-on ("_package"))
  ))