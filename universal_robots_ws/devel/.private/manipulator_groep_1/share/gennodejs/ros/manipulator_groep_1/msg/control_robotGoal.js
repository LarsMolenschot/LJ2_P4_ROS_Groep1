// Auto-generated. Do not edit!

// (in-package manipulator_groep_1.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class control_robotGoal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.lineairpose = null;
      this.position = null;
      this.mode = null;
    }
    else {
      if (initObj.hasOwnProperty('lineairpose')) {
        this.lineairpose = initObj.lineairpose
      }
      else {
        this.lineairpose = new geometry_msgs.msg.Pose();
      }
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = new std_msgs.msg.Bool();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type control_robotGoal
    // Serialize message field [lineairpose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.lineairpose, buffer, bufferOffset);
    // Serialize message field [position]
    bufferOffset = std_msgs.msg.String.serialize(obj.position, buffer, bufferOffset);
    // Serialize message field [mode]
    bufferOffset = std_msgs.msg.Bool.serialize(obj.mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type control_robotGoal
    let len;
    let data = new control_robotGoal(null);
    // Deserialize message field [lineairpose]
    data.lineairpose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    // Deserialize message field [position]
    data.position = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [mode]
    data.mode = std_msgs.msg.Bool.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.String.getMessageSize(object.position);
    return length + 57;
  }

  static datatype() {
    // Returns string type for a message object
    return 'manipulator_groep_1/control_robotGoal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e36f01127625ad1eec9d70ff2f265799';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    #goal
    
    geometry_msgs/Pose lineairpose
    
    std_msgs/String position
    
    std_msgs/Bool mode
    
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
    
    ================================================================================
    MSG: std_msgs/Bool
    bool data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new control_robotGoal(null);
    if (msg.lineairpose !== undefined) {
      resolved.lineairpose = geometry_msgs.msg.Pose.Resolve(msg.lineairpose)
    }
    else {
      resolved.lineairpose = new geometry_msgs.msg.Pose()
    }

    if (msg.position !== undefined) {
      resolved.position = std_msgs.msg.String.Resolve(msg.position)
    }
    else {
      resolved.position = new std_msgs.msg.String()
    }

    if (msg.mode !== undefined) {
      resolved.mode = std_msgs.msg.Bool.Resolve(msg.mode)
    }
    else {
      resolved.mode = new std_msgs.msg.Bool()
    }

    return resolved;
    }
};

module.exports = control_robotGoal;