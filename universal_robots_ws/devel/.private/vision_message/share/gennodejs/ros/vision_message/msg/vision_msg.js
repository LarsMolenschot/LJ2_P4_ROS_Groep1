// Auto-generated. Do not edit!

// (in-package vision_message.msg)


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

class vision_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.vision_positie = null;
      this.object_naam = null;
    }
    else {
      if (initObj.hasOwnProperty('vision_positie')) {
        this.vision_positie = initObj.vision_positie
      }
      else {
        this.vision_positie = new geometry_msgs.msg.Pose();
      }
      if (initObj.hasOwnProperty('object_naam')) {
        this.object_naam = initObj.object_naam
      }
      else {
        this.object_naam = new std_msgs.msg.String();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vision_msg
    // Serialize message field [vision_positie]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.vision_positie, buffer, bufferOffset);
    // Serialize message field [object_naam]
    bufferOffset = std_msgs.msg.String.serialize(obj.object_naam, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vision_msg
    let len;
    let data = new vision_msg(null);
    // Deserialize message field [vision_positie]
    data.vision_positie = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    // Deserialize message field [object_naam]
    data.object_naam = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.String.getMessageSize(object.object_naam);
    return length + 56;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vision_message/vision_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '52237def187f2c19b70d40056e5fd89f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Pose vision_positie
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vision_msg(null);
    if (msg.vision_positie !== undefined) {
      resolved.vision_positie = geometry_msgs.msg.Pose.Resolve(msg.vision_positie)
    }
    else {
      resolved.vision_positie = new geometry_msgs.msg.Pose()
    }

    if (msg.object_naam !== undefined) {
      resolved.object_naam = std_msgs.msg.String.Resolve(msg.object_naam)
    }
    else {
      resolved.object_naam = new std_msgs.msg.String()
    }

    return resolved;
    }
};

module.exports = vision_msg;
