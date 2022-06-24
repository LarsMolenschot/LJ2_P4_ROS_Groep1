
"use strict";

let control_robotActionGoal = require('./control_robotActionGoal.js');
let control_robotGoal = require('./control_robotGoal.js');
let control_robotActionResult = require('./control_robotActionResult.js');
let control_robotFeedback = require('./control_robotFeedback.js');
let control_robotResult = require('./control_robotResult.js');
let control_robotActionFeedback = require('./control_robotActionFeedback.js');
let control_robotAction = require('./control_robotAction.js');

module.exports = {
  control_robotActionGoal: control_robotActionGoal,
  control_robotGoal: control_robotGoal,
  control_robotActionResult: control_robotActionResult,
  control_robotFeedback: control_robotFeedback,
  control_robotResult: control_robotResult,
  control_robotActionFeedback: control_robotActionFeedback,
  control_robotAction: control_robotAction,
};
