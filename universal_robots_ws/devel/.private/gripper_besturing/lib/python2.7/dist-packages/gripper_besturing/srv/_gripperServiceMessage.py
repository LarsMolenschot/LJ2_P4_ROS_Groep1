# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gripper_besturing/gripperServiceMessageRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class gripperServiceMessageRequest(genpy.Message):
  _md5sum = "16ddae6f8940a74cb7096922bee88c8e"
  _type = "gripper_besturing/gripperServiceMessageRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string open_of_dicht_gripper
int64 gripper_opstarten
"""
  __slots__ = ['open_of_dicht_gripper','gripper_opstarten']
  _slot_types = ['string','int64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       open_of_dicht_gripper,gripper_opstarten

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(gripperServiceMessageRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.open_of_dicht_gripper is None:
        self.open_of_dicht_gripper = ''
      if self.gripper_opstarten is None:
        self.gripper_opstarten = 0
    else:
      self.open_of_dicht_gripper = ''
      self.gripper_opstarten = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.open_of_dicht_gripper
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper_opstarten
      buff.write(_get_struct_q().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.open_of_dicht_gripper = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.open_of_dicht_gripper = str[start:end]
      start = end
      end += 8
      (self.gripper_opstarten,) = _get_struct_q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.open_of_dicht_gripper
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.gripper_opstarten
      buff.write(_get_struct_q().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.open_of_dicht_gripper = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.open_of_dicht_gripper = str[start:end]
      start = end
      end += 8
      (self.gripper_opstarten,) = _get_struct_q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_q = None
def _get_struct_q():
    global _struct_q
    if _struct_q is None:
        _struct_q = struct.Struct("<q")
    return _struct_q
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gripper_besturing/gripperServiceMessageResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class gripperServiceMessageResponse(genpy.Message):
  _md5sum = "ef8c5718b3a04b760dd07273c62bce7f"
  _type = "gripper_besturing/gripperServiceMessageResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool succes
bool found_object
int64 error_nummer
string error_tekst

"""
  __slots__ = ['succes','found_object','error_nummer','error_tekst']
  _slot_types = ['bool','bool','int64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       succes,found_object,error_nummer,error_tekst

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(gripperServiceMessageResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.succes is None:
        self.succes = False
      if self.found_object is None:
        self.found_object = False
      if self.error_nummer is None:
        self.error_nummer = 0
      if self.error_tekst is None:
        self.error_tekst = ''
    else:
      self.succes = False
      self.found_object = False
      self.error_nummer = 0
      self.error_tekst = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2Bq().pack(_x.succes, _x.found_object, _x.error_nummer))
      _x = self.error_tekst
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 10
      (_x.succes, _x.found_object, _x.error_nummer,) = _get_struct_2Bq().unpack(str[start:end])
      self.succes = bool(self.succes)
      self.found_object = bool(self.found_object)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.error_tekst = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.error_tekst = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2Bq().pack(_x.succes, _x.found_object, _x.error_nummer))
      _x = self.error_tekst
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 10
      (_x.succes, _x.found_object, _x.error_nummer,) = _get_struct_2Bq().unpack(str[start:end])
      self.succes = bool(self.succes)
      self.found_object = bool(self.found_object)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.error_tekst = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.error_tekst = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2Bq = None
def _get_struct_2Bq():
    global _struct_2Bq
    if _struct_2Bq is None:
        _struct_2Bq = struct.Struct("<2Bq")
    return _struct_2Bq
class gripperServiceMessage(object):
  _type          = 'gripper_besturing/gripperServiceMessage'
  _md5sum = 'c9aa0baea7a9c0e9e50fcc3986fdf213'
  _request_class  = gripperServiceMessageRequest
  _response_class = gripperServiceMessageResponse