;; Auto-generated. Do not edit!


(when (boundp 'gripper_besturing::gripperServiceMessage)
  (if (not (find-package "GRIPPER_BESTURING"))
    (make-package "GRIPPER_BESTURING"))
  (shadow 'gripperServiceMessage (find-package "GRIPPER_BESTURING")))
(unless (find-package "GRIPPER_BESTURING::GRIPPERSERVICEMESSAGE")
  (make-package "GRIPPER_BESTURING::GRIPPERSERVICEMESSAGE"))
(unless (find-package "GRIPPER_BESTURING::GRIPPERSERVICEMESSAGEREQUEST")
  (make-package "GRIPPER_BESTURING::GRIPPERSERVICEMESSAGEREQUEST"))
(unless (find-package "GRIPPER_BESTURING::GRIPPERSERVICEMESSAGERESPONSE")
  (make-package "GRIPPER_BESTURING::GRIPPERSERVICEMESSAGERESPONSE"))

(in-package "ROS")





(defclass gripper_besturing::gripperServiceMessageRequest
  :super ros::object
  :slots (_open_of_dicht_gripper _gripper_opstarten ))

(defmethod gripper_besturing::gripperServiceMessageRequest
  (:init
   (&key
    ((:open_of_dicht_gripper __open_of_dicht_gripper) "")
    ((:gripper_opstarten __gripper_opstarten) 0)
    )
   (send-super :init)
   (setq _open_of_dicht_gripper (string __open_of_dicht_gripper))
   (setq _gripper_opstarten (round __gripper_opstarten))
   self)
  (:open_of_dicht_gripper
   (&optional __open_of_dicht_gripper)
   (if __open_of_dicht_gripper (setq _open_of_dicht_gripper __open_of_dicht_gripper)) _open_of_dicht_gripper)
  (:gripper_opstarten
   (&optional __gripper_opstarten)
   (if __gripper_opstarten (setq _gripper_opstarten __gripper_opstarten)) _gripper_opstarten)
  (:serialization-length
   ()
   (+
    ;; string _open_of_dicht_gripper
    4 (length _open_of_dicht_gripper)
    ;; int64 _gripper_opstarten
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _open_of_dicht_gripper
       (write-long (length _open_of_dicht_gripper) s) (princ _open_of_dicht_gripper s)
     ;; int64 _gripper_opstarten
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _gripper_opstarten (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _gripper_opstarten) (= (length (_gripper_opstarten . bv)) 2)) ;; bignum
              (write-long (ash (elt (_gripper_opstarten . bv) 0) 0) s)
              (write-long (ash (elt (_gripper_opstarten . bv) 1) -1) s))
             ((and (class _gripper_opstarten) (= (length (_gripper_opstarten . bv)) 1)) ;; big1
              (write-long (elt (_gripper_opstarten . bv) 0) s)
              (write-long (if (>= _gripper_opstarten 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _gripper_opstarten s)(write-long (if (>= _gripper_opstarten 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _open_of_dicht_gripper
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _open_of_dicht_gripper (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int64 _gripper_opstarten
#+(or :alpha :irix6 :x86_64)
      (setf _gripper_opstarten (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _gripper_opstarten (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass gripper_besturing::gripperServiceMessageResponse
  :super ros::object
  :slots (_succes _found_object _error_nummer _error_tekst ))

(defmethod gripper_besturing::gripperServiceMessageResponse
  (:init
   (&key
    ((:succes __succes) nil)
    ((:found_object __found_object) nil)
    ((:error_nummer __error_nummer) 0)
    ((:error_tekst __error_tekst) "")
    )
   (send-super :init)
   (setq _succes __succes)
   (setq _found_object __found_object)
   (setq _error_nummer (round __error_nummer))
   (setq _error_tekst (string __error_tekst))
   self)
  (:succes
   (&optional __succes)
   (if __succes (setq _succes __succes)) _succes)
  (:found_object
   (&optional __found_object)
   (if __found_object (setq _found_object __found_object)) _found_object)
  (:error_nummer
   (&optional __error_nummer)
   (if __error_nummer (setq _error_nummer __error_nummer)) _error_nummer)
  (:error_tekst
   (&optional __error_tekst)
   (if __error_tekst (setq _error_tekst __error_tekst)) _error_tekst)
  (:serialization-length
   ()
   (+
    ;; bool _succes
    1
    ;; bool _found_object
    1
    ;; int64 _error_nummer
    8
    ;; string _error_tekst
    4 (length _error_tekst)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _succes
       (if _succes (write-byte -1 s) (write-byte 0 s))
     ;; bool _found_object
       (if _found_object (write-byte -1 s) (write-byte 0 s))
     ;; int64 _error_nummer
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _error_nummer (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _error_nummer) (= (length (_error_nummer . bv)) 2)) ;; bignum
              (write-long (ash (elt (_error_nummer . bv) 0) 0) s)
              (write-long (ash (elt (_error_nummer . bv) 1) -1) s))
             ((and (class _error_nummer) (= (length (_error_nummer . bv)) 1)) ;; big1
              (write-long (elt (_error_nummer . bv) 0) s)
              (write-long (if (>= _error_nummer 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _error_nummer s)(write-long (if (>= _error_nummer 0) 0 #xffffffff) s)))
     ;; string _error_tekst
       (write-long (length _error_tekst) s) (princ _error_tekst s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _succes
     (setq _succes (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _found_object
     (setq _found_object (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int64 _error_nummer
#+(or :alpha :irix6 :x86_64)
      (setf _error_nummer (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _error_nummer (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; string _error_tekst
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _error_tekst (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass gripper_besturing::gripperServiceMessage
  :super ros::object
  :slots ())

(setf (get gripper_besturing::gripperServiceMessage :md5sum-) "c9aa0baea7a9c0e9e50fcc3986fdf213")
(setf (get gripper_besturing::gripperServiceMessage :datatype-) "gripper_besturing/gripperServiceMessage")
(setf (get gripper_besturing::gripperServiceMessage :request) gripper_besturing::gripperServiceMessageRequest)
(setf (get gripper_besturing::gripperServiceMessage :response) gripper_besturing::gripperServiceMessageResponse)

(defmethod gripper_besturing::gripperServiceMessageRequest
  (:response () (instance gripper_besturing::gripperServiceMessageResponse :init)))

(setf (get gripper_besturing::gripperServiceMessageRequest :md5sum-) "c9aa0baea7a9c0e9e50fcc3986fdf213")
(setf (get gripper_besturing::gripperServiceMessageRequest :datatype-) "gripper_besturing/gripperServiceMessageRequest")
(setf (get gripper_besturing::gripperServiceMessageRequest :definition-)
      "string open_of_dicht_gripper
int64 gripper_opstarten
---
bool succes
bool found_object
int64 error_nummer
string error_tekst

")

(setf (get gripper_besturing::gripperServiceMessageResponse :md5sum-) "c9aa0baea7a9c0e9e50fcc3986fdf213")
(setf (get gripper_besturing::gripperServiceMessageResponse :datatype-) "gripper_besturing/gripperServiceMessageResponse")
(setf (get gripper_besturing::gripperServiceMessageResponse :definition-)
      "string open_of_dicht_gripper
int64 gripper_opstarten
---
bool succes
bool found_object
int64 error_nummer
string error_tekst

")



(provide :gripper_besturing/gripperServiceMessage "c9aa0baea7a9c0e9e50fcc3986fdf213")


