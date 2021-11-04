# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: widevine_common_encryption.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='widevine_common_encryption.proto',
  package='shaka',
  syntax='proto2',
  serialized_pb=_b('\n widevine_common_encryption.proto\x12\x05shaka\"\xb1\x04\n\x17\x43ommonEncryptionRequest\x12\x12\n\ncontent_id\x18\x01 \x01(\x0c\x12\x0e\n\x06policy\x18\x02 \x01(\t\x12\x34\n\x06tracks\x18\x03 \x03(\x0b\x32$.shaka.CommonEncryptionRequest.Track\x12(\n\tdrm_types\x18\x04 \x03(\x0e\x32\x15.shaka.ModularDrmType\x12!\n\x19\x66irst_crypto_period_index\x18\x08 \x01(\r\x12\x1e\n\x13\x63rypto_period_count\x18\t \x01(\r:\x01\x31\x12\x11\n\tpssh_data\x18\n \x01(\x0c\x12\x10\n\x08\x61sset_id\x18\x0b \x01(\r\x12\x10\n\x08group_id\x18\x0c \x01(\x0c\x12\x1d\n\x15\x63rypto_period_seconds\x18\r \x01(\r\x12J\n\x11protection_scheme\x18\x0e \x01(\x0e\x32/.shaka.CommonEncryptionRequest.ProtectionScheme\x12\"\n\x1a\x65nable_entitlement_license\x18\x10 \x01(\x08\x12\x15\n\rvideo_feature\x18\x13 \x01(\t\x1a\x15\n\x05Track\x12\x0c\n\x04type\x18\x01 \x01(\t\"[\n\x10ProtectionScheme\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x04\x43\x45NC\x10\xe3\xdc\x95\x9b\x06\x12\x0c\n\x04\x43\x42\x43\x31\x10\xb1\xc6\x89\x9b\x06\x12\x0c\n\x04\x43\x45NS\x10\xf3\xdc\x95\x9b\x06\x12\x0c\n\x04\x43\x42\x43S\x10\xf3\xc6\x89\x9b\x06\"\xb8\x07\n\x18\x43ommonEncryptionResponse\x12\x36\n\x06status\x18\x01 \x01(\x0e\x32&.shaka.CommonEncryptionResponse.Status\x12\x30\n\x03\x64rm\x18\x03 \x03(\x0b\x32#.shaka.CommonEncryptionResponse.Drm\x12\x35\n\x06tracks\x18\x04 \x03(\x0b\x32%.shaka.CommonEncryptionResponse.Track\x12\x12\n\ncontent_id\x18\x06 \x01(\x0c\x1a=\n\x03\x44rm\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.shaka.ModularDrmType\x12\x11\n\tsystem_id\x18\x02 \x01(\t\x1a\xe3\x01\n\x05Track\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06key_id\x18\x02 \x01(\x0c\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\n\n\x02iv\x18\x04 \x01(\x0c\x12\x38\n\x04pssh\x18\x05 \x03(\x0b\x32*.shaka.CommonEncryptionResponse.Track.Pssh\x12\x1b\n\x13\x63rypto_period_index\x18\x06 \x01(\r\x1aL\n\x04Pssh\x12\'\n\x08\x64rm_type\x18\x01 \x01(\x0e\x32\x15.shaka.ModularDrmType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\r\n\x05\x62oxes\x18\x03 \x01(\x0c\"\xc1\x03\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x14\n\x10SIGNATURE_FAILED\x10\x01\x12\x16\n\x12\x43ONTENT_ID_MISSING\x10\x02\x12\x12\n\x0ePOLICY_UNKNOWN\x10\x03\x12\x16\n\x12TRACK_TYPE_MISSING\x10\x04\x12\x16\n\x12TRACK_TYPE_UNKNOWN\x10\x05\x12\x15\n\x11MALFORMED_REQUEST\x10\x06\x12\x11\n\rACCESS_DENIED\x10\x07\x12\x12\n\x0eINTERNAL_ERROR\x10\x08\x12\x19\n\x15INVALID_WIDEVINE_PSSH\x10\t\x12\x1f\n\x1bTOO_MANY_CONTENT_SPECIFIERS\x10\n\x12\x13\n\x0f\x41SSET_NOT_FOUND\x10\x0b\x12\x15\n\x11\x41SSET_MISSING_KEY\x10\x0c\x12\x17\n\x13\x43ONTENT_ID_MISMATCH\x10\r\x12\x13\n\x0fKEY_ID_MISMATCH\x10\x0e\x12\x1c\n\x18INVALID_GROUP_TRACK_TYPE\x10\x0f\x12*\n&KEY_ROTATION_WITH_UNSUPPORTED_DRM_TYPE\x10\x10\x12\x1f\n\x1bNO_REQUESTED_CRYPTO_PERIODS\x10\x11\"M\n\x17SignedModularDrmRequest\x12\x0f\n\x07request\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x0e\n\x06signer\x18\x03 \x01(\t\"?\n\x18SignedModularDrmResponse\x12\x10\n\x08response\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c*\x1e\n\x0eModularDrmType\x12\x0c\n\x08WIDEVINE\x10\x00')
)

_MODULARDRMTYPE = _descriptor.EnumDescriptor(
  name='ModularDrmType',
  full_name='shaka.ModularDrmType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WIDEVINE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1706,
  serialized_end=1736,
)
_sym_db.RegisterEnumDescriptor(_MODULARDRMTYPE)

ModularDrmType = enum_type_wrapper.EnumTypeWrapper(_MODULARDRMTYPE)
WIDEVINE = 0


_COMMONENCRYPTIONREQUEST_PROTECTIONSCHEME = _descriptor.EnumDescriptor(
  name='ProtectionScheme',
  full_name='shaka.CommonEncryptionRequest.ProtectionScheme',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CENC', index=1, number=1667591779,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CBC1', index=2, number=1667392305,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CENS', index=3, number=1667591795,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CBCS', index=4, number=1667392371,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=514,
  serialized_end=605,
)
_sym_db.RegisterEnumDescriptor(_COMMONENCRYPTIONREQUEST_PROTECTIONSCHEME)

_COMMONENCRYPTIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='shaka.CommonEncryptionResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGNATURE_FAILED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTENT_ID_MISSING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLICY_UNKNOWN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACK_TYPE_MISSING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACK_TYPE_UNKNOWN', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALFORMED_REQUEST', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_DENIED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_WIDEVINE_PSSH', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_CONTENT_SPECIFIERS', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSET_NOT_FOUND', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSET_MISSING_KEY', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTENT_ID_MISMATCH', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY_ID_MISMATCH', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_GROUP_TRACK_TYPE', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY_ROTATION_WITH_UNSUPPORTED_DRM_TYPE', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_REQUESTED_CRYPTO_PERIODS', index=17, number=17,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1111,
  serialized_end=1560,
)
_sym_db.RegisterEnumDescriptor(_COMMONENCRYPTIONRESPONSE_STATUS)


_COMMONENCRYPTIONREQUEST_TRACK = _descriptor.Descriptor(
  name='Track',
  full_name='shaka.CommonEncryptionRequest.Track',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='shaka.CommonEncryptionRequest.Track.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=491,
  serialized_end=512,
)

_COMMONENCRYPTIONREQUEST = _descriptor.Descriptor(
  name='CommonEncryptionRequest',
  full_name='shaka.CommonEncryptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_id', full_name='shaka.CommonEncryptionRequest.content_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy', full_name='shaka.CommonEncryptionRequest.policy', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracks', full_name='shaka.CommonEncryptionRequest.tracks', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drm_types', full_name='shaka.CommonEncryptionRequest.drm_types', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_crypto_period_index', full_name='shaka.CommonEncryptionRequest.first_crypto_period_index', index=4,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crypto_period_count', full_name='shaka.CommonEncryptionRequest.crypto_period_count', index=5,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pssh_data', full_name='shaka.CommonEncryptionRequest.pssh_data', index=6,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='shaka.CommonEncryptionRequest.asset_id', index=7,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='shaka.CommonEncryptionRequest.group_id', index=8,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crypto_period_seconds', full_name='shaka.CommonEncryptionRequest.crypto_period_seconds', index=9,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protection_scheme', full_name='shaka.CommonEncryptionRequest.protection_scheme', index=10,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable_entitlement_license', full_name='shaka.CommonEncryptionRequest.enable_entitlement_license', index=11,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_feature', full_name='shaka.CommonEncryptionRequest.video_feature', index=12,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COMMONENCRYPTIONREQUEST_TRACK, ],
  enum_types=[
    _COMMONENCRYPTIONREQUEST_PROTECTIONSCHEME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=605,
)


_COMMONENCRYPTIONRESPONSE_DRM = _descriptor.Descriptor(
  name='Drm',
  full_name='shaka.CommonEncryptionResponse.Drm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='shaka.CommonEncryptionResponse.Drm.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_id', full_name='shaka.CommonEncryptionResponse.Drm.system_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=817,
  serialized_end=878,
)

_COMMONENCRYPTIONRESPONSE_TRACK_PSSH = _descriptor.Descriptor(
  name='Pssh',
  full_name='shaka.CommonEncryptionResponse.Track.Pssh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drm_type', full_name='shaka.CommonEncryptionResponse.Track.Pssh.drm_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='shaka.CommonEncryptionResponse.Track.Pssh.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boxes', full_name='shaka.CommonEncryptionResponse.Track.Pssh.boxes', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1032,
  serialized_end=1108,
)

_COMMONENCRYPTIONRESPONSE_TRACK = _descriptor.Descriptor(
  name='Track',
  full_name='shaka.CommonEncryptionResponse.Track',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='shaka.CommonEncryptionResponse.Track.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='shaka.CommonEncryptionResponse.Track.key_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='shaka.CommonEncryptionResponse.Track.key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iv', full_name='shaka.CommonEncryptionResponse.Track.iv', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pssh', full_name='shaka.CommonEncryptionResponse.Track.pssh', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crypto_period_index', full_name='shaka.CommonEncryptionResponse.Track.crypto_period_index', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COMMONENCRYPTIONRESPONSE_TRACK_PSSH, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=1108,
)

_COMMONENCRYPTIONRESPONSE = _descriptor.Descriptor(
  name='CommonEncryptionResponse',
  full_name='shaka.CommonEncryptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='shaka.CommonEncryptionResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drm', full_name='shaka.CommonEncryptionResponse.drm', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracks', full_name='shaka.CommonEncryptionResponse.tracks', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_id', full_name='shaka.CommonEncryptionResponse.content_id', index=3,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COMMONENCRYPTIONRESPONSE_DRM, _COMMONENCRYPTIONRESPONSE_TRACK, ],
  enum_types=[
    _COMMONENCRYPTIONRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=1560,
)


_SIGNEDMODULARDRMREQUEST = _descriptor.Descriptor(
  name='SignedModularDrmRequest',
  full_name='shaka.SignedModularDrmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='shaka.SignedModularDrmRequest.request', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='shaka.SignedModularDrmRequest.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signer', full_name='shaka.SignedModularDrmRequest.signer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1562,
  serialized_end=1639,
)


_SIGNEDMODULARDRMRESPONSE = _descriptor.Descriptor(
  name='SignedModularDrmResponse',
  full_name='shaka.SignedModularDrmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='shaka.SignedModularDrmResponse.response', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='shaka.SignedModularDrmResponse.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1641,
  serialized_end=1704,
)

_COMMONENCRYPTIONREQUEST_TRACK.containing_type = _COMMONENCRYPTIONREQUEST
_COMMONENCRYPTIONREQUEST.fields_by_name['tracks'].message_type = _COMMONENCRYPTIONREQUEST_TRACK
_COMMONENCRYPTIONREQUEST.fields_by_name['drm_types'].enum_type = _MODULARDRMTYPE
_COMMONENCRYPTIONREQUEST.fields_by_name['protection_scheme'].enum_type = _COMMONENCRYPTIONREQUEST_PROTECTIONSCHEME
_COMMONENCRYPTIONREQUEST_PROTECTIONSCHEME.containing_type = _COMMONENCRYPTIONREQUEST
_COMMONENCRYPTIONRESPONSE_DRM.fields_by_name['type'].enum_type = _MODULARDRMTYPE
_COMMONENCRYPTIONRESPONSE_DRM.containing_type = _COMMONENCRYPTIONRESPONSE
_COMMONENCRYPTIONRESPONSE_TRACK_PSSH.fields_by_name['drm_type'].enum_type = _MODULARDRMTYPE
_COMMONENCRYPTIONRESPONSE_TRACK_PSSH.containing_type = _COMMONENCRYPTIONRESPONSE_TRACK
_COMMONENCRYPTIONRESPONSE_TRACK.fields_by_name['pssh'].message_type = _COMMONENCRYPTIONRESPONSE_TRACK_PSSH
_COMMONENCRYPTIONRESPONSE_TRACK.containing_type = _COMMONENCRYPTIONRESPONSE
_COMMONENCRYPTIONRESPONSE.fields_by_name['status'].enum_type = _COMMONENCRYPTIONRESPONSE_STATUS
_COMMONENCRYPTIONRESPONSE.fields_by_name['drm'].message_type = _COMMONENCRYPTIONRESPONSE_DRM
_COMMONENCRYPTIONRESPONSE.fields_by_name['tracks'].message_type = _COMMONENCRYPTIONRESPONSE_TRACK
_COMMONENCRYPTIONRESPONSE_STATUS.containing_type = _COMMONENCRYPTIONRESPONSE
DESCRIPTOR.message_types_by_name['CommonEncryptionRequest'] = _COMMONENCRYPTIONREQUEST
DESCRIPTOR.message_types_by_name['CommonEncryptionResponse'] = _COMMONENCRYPTIONRESPONSE
DESCRIPTOR.message_types_by_name['SignedModularDrmRequest'] = _SIGNEDMODULARDRMREQUEST
DESCRIPTOR.message_types_by_name['SignedModularDrmResponse'] = _SIGNEDMODULARDRMRESPONSE
DESCRIPTOR.enum_types_by_name['ModularDrmType'] = _MODULARDRMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonEncryptionRequest = _reflection.GeneratedProtocolMessageType('CommonEncryptionRequest', (_message.Message,), dict(

  Track = _reflection.GeneratedProtocolMessageType('Track', (_message.Message,), dict(
    DESCRIPTOR = _COMMONENCRYPTIONREQUEST_TRACK,
    __module__ = 'widevine_common_encryption_pb2'
    # @@protoc_insertion_point(class_scope:shaka.CommonEncryptionRequest.Track)
    ))
  ,
  DESCRIPTOR = _COMMONENCRYPTIONREQUEST,
  __module__ = 'widevine_common_encryption_pb2'
  # @@protoc_insertion_point(class_scope:shaka.CommonEncryptionRequest)
  ))
_sym_db.RegisterMessage(CommonEncryptionRequest)
_sym_db.RegisterMessage(CommonEncryptionRequest.Track)

CommonEncryptionResponse = _reflection.GeneratedProtocolMessageType('CommonEncryptionResponse', (_message.Message,), dict(

  Drm = _reflection.GeneratedProtocolMessageType('Drm', (_message.Message,), dict(
    DESCRIPTOR = _COMMONENCRYPTIONRESPONSE_DRM,
    __module__ = 'widevine_common_encryption_pb2'
    # @@protoc_insertion_point(class_scope:shaka.CommonEncryptionResponse.Drm)
    ))
  ,

  Track = _reflection.GeneratedProtocolMessageType('Track', (_message.Message,), dict(

    Pssh = _reflection.GeneratedProtocolMessageType('Pssh', (_message.Message,), dict(
      DESCRIPTOR = _COMMONENCRYPTIONRESPONSE_TRACK_PSSH,
      __module__ = 'widevine_common_encryption_pb2'
      # @@protoc_insertion_point(class_scope:shaka.CommonEncryptionResponse.Track.Pssh)
      ))
    ,
    DESCRIPTOR = _COMMONENCRYPTIONRESPONSE_TRACK,
    __module__ = 'widevine_common_encryption_pb2'
    # @@protoc_insertion_point(class_scope:shaka.CommonEncryptionResponse.Track)
    ))
  ,
  DESCRIPTOR = _COMMONENCRYPTIONRESPONSE,
  __module__ = 'widevine_common_encryption_pb2'
  # @@protoc_insertion_point(class_scope:shaka.CommonEncryptionResponse)
  ))
_sym_db.RegisterMessage(CommonEncryptionResponse)
_sym_db.RegisterMessage(CommonEncryptionResponse.Drm)
_sym_db.RegisterMessage(CommonEncryptionResponse.Track)
_sym_db.RegisterMessage(CommonEncryptionResponse.Track.Pssh)

SignedModularDrmRequest = _reflection.GeneratedProtocolMessageType('SignedModularDrmRequest', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDMODULARDRMREQUEST,
  __module__ = 'widevine_common_encryption_pb2'
  # @@protoc_insertion_point(class_scope:shaka.SignedModularDrmRequest)
  ))
_sym_db.RegisterMessage(SignedModularDrmRequest)

SignedModularDrmResponse = _reflection.GeneratedProtocolMessageType('SignedModularDrmResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDMODULARDRMRESPONSE,
  __module__ = 'widevine_common_encryption_pb2'
  # @@protoc_insertion_point(class_scope:shaka.SignedModularDrmResponse)
  ))
_sym_db.RegisterMessage(SignedModularDrmResponse)


# @@protoc_insertion_point(module_scope)
