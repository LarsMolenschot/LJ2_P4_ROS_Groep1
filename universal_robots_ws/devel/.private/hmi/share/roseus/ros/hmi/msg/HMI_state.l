;; Auto-generated. Do not edit!


(when (boundp 'hmi::HMI_state)
  (if (not (find-package "HMI"))
    (make-package "HMI"))
  (shadow 'HMI_state (find-package "HMI")))
(unless (find-package "HMI::HMI_STATE")
  (make-package "HMI::HMI_STATE"))

(in-package "ROS")
;;//! \htmlinclude HMI_state.msg.html


(defclass hmi::HMI_state
  :super ros::object
  :slots (_programstate _programtype _buttontype ))

(defmethod hmi::HMI_state
  (:init
   (&key
    ((:programstate __programstate) "")
    ((:programtype __programtype) "")
    ((:buttontype __buttontype) 0)
    )
   (send-super :init)
   (setq _programstate (string __programstate))
   (setq _programtype (string __programtype))
   (setq _buttontype (round __buttontype))
   self)
  (:programstate
   (&optional __programstate)
   (if __programstate (setq _programstate __programstate)) _programstate)
  (:programtype
   (&optional __programtype)
   (if __programtype (setq _programtype __programtype)) _programtype)
  (:buttontype
   (&optional __buttontype)
   (if __buttontype (setq _buttontype __buttontype)) _buttontype)
  (:serialization-length
   ()
   (+
    ;; string _programstate
    4 (length _programstate)
    ;; string _programtype
    4 (length _programtype)
    ;; uint8 _buttontype
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _programstate
       (write-long (length _programstate) s) (princ _programstate s)
     ;; string _programtype
       (write-long (length _programtype) s) (princ _programtype s)
     ;; uint8 _buttontype
       (write-byte _buttontype s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _programstate
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _programstate (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _programtype
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _programtype (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _buttontype
     (setq _buttontype (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get hmi::HMI_state :md5sum-) "d05be62867557efe2359be0b2c4cb496")
(setf (get hmi::HMI_state :datatype-) "hmi/HMI_state")
(setf (get hmi::HMI_state :definition-)
      "string programstate
string programtype
uint8 buttontype

")



(provide :hmi/HMI_state "d05be62867557efe2359be0b2c4cb496")


