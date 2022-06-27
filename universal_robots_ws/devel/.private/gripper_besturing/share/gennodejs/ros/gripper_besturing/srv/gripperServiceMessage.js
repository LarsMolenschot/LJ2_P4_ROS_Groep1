// Auto-generated. Do not edit!

// (in-package gripper_besturing.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class gripperServiceMessageRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.open_of_dicht_gripper = null;
      this.gripper_opstarten = null;
    }
    else {
      if (initObj.hasOwnProperty('open_of_dicht_gripper')) {
        this.open_of_dicht_gripper = initObj.open_of_dicht_gripper
      }
      else {
        this.open_of_dicht_gripper = '';
      }
      if (initObj.hasOwnProperty('gripper_opstarten')) {
        this.gripper_opstarten = initObj.gripper_opstarten
      }
      else {
        this.gripper_opstarten = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type gripperServiceMessageRequest
    // Serialize message field [open_of_dicht_gripper]
    bufferOffset = _serializer.string(obj.open_of_dicht_gripper, buffer, bufferOffset);
    // Serialize message field [gripper_opstarten]
    bufferOffset = _serializer.int64(obj.gripper_opstarten, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type gripperServiceMessageRequest
    let len;
    let data = new gripperServiceMessageRequest(null);
    // Deserialize message field [open_of_dicht_gripper]
    data.open_of_dicht_gripper = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [gripper_opstarten]
    data.gripper_opstarten = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.open_of_dicht_gripper.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'gripper_besturing/gripperServiceMessageRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '16ddae6f8940a74cb7096922bee88c8e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string open_of_dicht_gripper
    int64 gripper_opstarten
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new gripperServiceMessageRequest(null);
    if (msg.open_of_dicht_gripper !== undefined) {
      resolved.open_of_dicht_gripper = msg.open_of_dicht_gripper;
    }
    else {
      resolved.open_of_dicht_gripper = ''
    }

    if (msg.gripper_opstarten !== undefined) {
      resolved.gripper_opstarten = msg.gripper_opstarten;
    }
    else {
      resolved.gripper_opstarten = 0
    }

    return resolved;
    }
};

class gripperServiceMessageResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.succes = null;
      this.found_object = null;
      this.error_nummer = null;
      this.error_tekst = null;
    }
    else {
      if (initObj.hasOwnProperty('succes')) {
        this.succes = initObj.succes
      }
      else {
        this.succes = false;
      }
      if (initObj.hasOwnProperty('found_object')) {
        this.found_object = initObj.found_object
      }
      else {
        this.found_object = false;
      }
      if (initObj.hasOwnProperty('error_nummer')) {
        this.error_nummer = initObj.error_nummer
      }
      else {
        this.error_nummer = 0;
      }
      if (initObj.hasOwnProperty('error_tekst')) {
        this.error_tekst = initObj.error_tekst
      }
      else {
        this.error_tekst = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type gripperServiceMessageResponse
    // Serialize message field [succes]
    bufferOffset = _serializer.bool(obj.succes, buffer, bufferOffset);
    // Serialize message field [found_object]
    bufferOffset = _serializer.bool(obj.found_object, buffer, bufferOffset);
    // Serialize message field [error_nummer]
    bufferOffset = _serializer.int64(obj.error_nummer, buffer, bufferOffset);
    // Serialize message field [error_tekst]
    bufferOffset = _serializer.string(obj.error_tekst, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type gripperServiceMessageResponse
    let len;
    let data = new gripperServiceMessageResponse(null);
    // Deserialize message field [succes]
    data.succes = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [found_object]
    data.found_object = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [error_nummer]
    data.error_nummer = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [error_tekst]
    data.error_tekst = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.error_tekst.length;
    return length + 14;
  }

  static datatype() {
    // Returns string type for a service object
    return 'gripper_besturing/gripperServiceMessageResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ef8c5718b3a04b760dd07273c62bce7f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool succes
    bool found_object
    int64 error_nummer
    string error_tekst
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new gripperServiceMessageResponse(null);
    if (msg.succes !== undefined) {
      resolved.succes = msg.succes;
    }
    else {
      resolved.succes = false
    }

    if (msg.found_object !== undefined) {
      resolved.found_object = msg.found_object;
    }
    else {
      resolved.found_object = false
    }

    if (msg.error_nummer !== undefined) {
      resolved.error_nummer = msg.error_nummer;
    }
    else {
      resolved.error_nummer = 0
    }

    if (msg.error_tekst !== undefined) {
      resolved.error_tekst = msg.error_tekst;
    }
    else {
      resolved.error_tekst = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: gripperServiceMessageRequest,
  Response: gripperServiceMessageResponse,
  md5sum() { return 'c9aa0baea7a9c0e9e50fcc3986fdf213'; },
  datatype() { return 'gripper_besturing/gripperServiceMessage'; }
};
