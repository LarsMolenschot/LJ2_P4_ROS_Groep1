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
  :slots (_programstate _programtype _stop _noodstop _stopreset ))

(defmethod hmi::HMI_state
  (:init
   (&key
    ((:programstate __programstate) "")
    ((:programtype __programtype) "")
    ((:stop __stop) nil)
    ((:noodstop __noodstop) nil)
    ((:stopreset __stopreset) nil)
    )
   (send-super :init)
   (setq _programstate (string __programstate))
   (setq _programtype (string __programtype))
   (setq _stop __stop)
   (setq _noodstop __noodstop)
   (setq _stopreset __stopreset)
   self)
  (:programstate
   (&optional __programstate)
   (if __programstate (setq _programstate __programstate)) _programstate)
  (:programtype
   (&optional __programtype)
   (if __programtype (setq _programtype __programtype)) _programtype)
  (:stop
   (&optional __stop)
   (if __stop (setq _stop __stop)) _stop)
  (:noodstop
   (&optional __noodstop)
   (if __noodstop (setq _noodstop __noodstop)) _noodstop)
  (:stopreset
   (&optional __stopreset)
   (if __stopreset (setq _stopreset __stopreset)) _stopreset)
  (:serialization-length
   ()
   (+
    ;; string _programstate
    4 (length _programstate)
    ;; string _programtype
    4 (length _programtype)
    ;; bool _stop
    1
    ;; bool _noodstop
    1
    ;; bool _stopreset
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
     ;; bool _stop
       (if _stop (write-byte -1 s) (write-byte 0 s))
     ;; bool _noodstop
       (if _noodstop (write-byte -1 s) (write-byte 0 s))
     ;; bool _stopreset
       (if _stopreset (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _programstate
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _programstate (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _programtype
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _programtype (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _stop
     (setq _stop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _noodstop
     (setq _noodstop (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _stopreset
     (setq _stopreset (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get hmi::HMI_state :md5sum-) "12d2ece259040b0ded5a9b3526331ec2")
(setf (get hmi::HMI_state :datatype-) "hmi/HMI_state")
(setf (get hmi::HMI_state :definition-)
      "string programstate
string programtype
bool stop
bool noodstop
bool stopreset

")



(provide :hmi/HMI_state "12d2ece259040b0ded5a9b3526331ec2")


