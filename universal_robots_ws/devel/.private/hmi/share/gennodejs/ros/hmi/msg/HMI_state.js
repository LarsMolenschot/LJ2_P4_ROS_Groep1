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
      this.stop = null;
      this.noodstop = null;
      this.stopreset = null;
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
      if (initObj.hasOwnProperty('stop')) {
        this.stop = initObj.stop
      }
      else {
        this.stop = false;
      }
      if (initObj.hasOwnProperty('noodstop')) {
        this.noodstop = initObj.noodstop
      }
      else {
        this.noodstop = false;
      }
      if (initObj.hasOwnProperty('stopreset')) {
        this.stopreset = initObj.stopreset
      }
      else {
        this.stopreset = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HMI_state
    // Serialize message field [programstate]
    bufferOffset = _serializer.string(obj.programstate, buffer, bufferOffset);
    // Serialize message field [programtype]
    bufferOffset = _serializer.string(obj.programtype, buffer, bufferOffset);
    // Serialize message field [stop]
    bufferOffset = _serializer.bool(obj.stop, buffer, bufferOffset);
    // Serialize message field [noodstop]
    bufferOffset = _serializer.bool(obj.noodstop, buffer, bufferOffset);
    // Serialize message field [stopreset]
    bufferOffset = _serializer.bool(obj.stopreset, buffer, bufferOffset);
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
    // Deserialize message field [stop]
    data.stop = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [noodstop]
    data.noodstop = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [stopreset]
    data.stopreset = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.programstate.length;
    length += object.programtype.length;
    return length + 11;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hmi/HMI_state';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '12d2ece259040b0ded5a9b3526331ec2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string programstate
    string programtype
    bool stop
    bool noodstop
    bool stopreset
    
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

    if (msg.stop !== undefined) {
      resolved.stop = msg.stop;
    }
    else {
      resolved.stop = false
    }

    if (msg.noodstop !== undefined) {
      resolved.noodstop = msg.noodstop;
    }
    else {
      resolved.noodstop = false
    }

    if (msg.stopreset !== undefined) {
      resolved.stopreset = msg.stopreset;
    }
    else {
      resolved.stopreset = false
    }

    return resolved;
    }
};

module.exports = HMI_state;
