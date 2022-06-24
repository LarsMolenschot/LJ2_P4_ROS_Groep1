
(cl:in-package :asdf)

(defsystem "hmi-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "HMI_state" :depends-on ("_package_HMI_state"))
    (:file "_package_HMI_state" :depends-on ("_package"))
  ))