// Auto-generated. Do not edit!

// (in-package hmi.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class HMI_state {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.programstate = null;
      this.programtype = null;
      this.buttontype = null;
    }
    else {
      if (initObj.hasOwnProperty('programstate')) {
        this.programstate = initObj.programstate
      }
      else {
        this.programstate = '';
      }
      if (initObj.hasOwnProperty('programtype')) {
        this.programtype = initObj.programtype
      }
      else {
        this.programtype = '';
      }
      if (initObj.hasOwnProperty('buttontype')) {
        this.buttontype = initObj.buttontype
      }
      else {
        this.buttontype = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HMI_state
    // Serialize message field [programstate]
    bufferOffset = _serializer.string(obj.programstate, buffer, bufferOffset);
    // Serialize message field [programtype]
    bufferOffset = _serializer.string(obj.programtype, buffer, bufferOffset);
    // Serialize message field [buttontype]
    bufferOffset = _serializer.uint8(obj.buttontype, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HMI_state
    let len;
    let data = new HMI_state(null);
    // Deserialize message field [programstate]
    data.programstate = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [programtype]
    data.programtype = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [buttontype]
    data.buttontype = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.programstate.length;
    length += object.programtype.length;
    return length + 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hmi/HMI_state';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd05be62867557efe2359be0b2c4cb496';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string programstate
    string programtype
    uint8 buttontype
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HMI_state(null);
    if (msg.programstate !== undefined) {
      resolved.programstate = msg.programstate;
    }
    else {
      resolved.programstate = ''
    }

    if (msg.programtype !== undefined) {
      resolved.programtype = msg.programtype;
    }
    else {
      resolved.programtype = ''
    }

    if (msg.buttontype !== undefined) {
      resolved.buttontype = msg.buttontype;
    }
    else {
      resolved.buttontype = 0
    }

    return resolved;
    }
};

module.exports = HMI_state;
