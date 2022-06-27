
(cl:in-package :asdf)

(defsystem "gripper_besturing-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "gripperServiceMessage" :depends-on ("_package_gripperServiceMessage"))
    (:file "_package_gripperServiceMessage" :depends-on ("_package"))
  ))