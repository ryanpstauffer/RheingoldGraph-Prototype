# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rheingoldgraph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import rheingoldgraph.protobuf.music_pb2 as music__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rheingoldgraph.proto',
  package='rheingoldgraph',
  syntax='proto3',
  serialized_pb=_b('\n\x14rheingoldgraph.proto\x12\x0erheingoldgraph\x1a\x0bmusic.proto\"\x1e\n\x0eSummaryRequest\x12\x0c\n\x04line\x18\x01 \x01(\t\"3\n\x0bLineRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0e\x65xcerpt_length\x18\x02 \x01(\x05\"-\n\nXMLRequest\x12\x0b\n\x03xml\x18\x01 \x01(\x0c\x12\x12\n\npiece_name\x18\x02 \x01(\t\"L\n\x0eHeaderMetadata\x12\x14\n\x0c\x63reated_date\x18\x01 \x01(\t\x12\x10\n\x08\x63omposer\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\x05\"z\n\x0cGraphSummary\x12\x16\n\x0etotal_vertices\x18\x01 \x01(\x05\x12\x13\n\x0btotal_edges\x18\x02 \x01(\x05\x12\x11\n\tnum_lines\x18\x03 \x01(\x05\x12*\n\x05lines\x18\x04 \x03(\x0b\x32\x1b.rheingoldgraph.LineSummary\"-\n\x0bLineSummary\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08vertices\x18\x02 \x01(\x05\"-\n\x0c\x44ropResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"A\n\x0b\x41\x64\x64Response\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x13\n\x0bnotes_added\x18\x03 \x01(\x05\"m\n\x04Line\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x05notes\x18\x02 \x03(\x0b\x32\x18.rheingoldgraph.LineNote\x12.\n\x06header\x18\x03 \x01(\x0b\x32\x1e.rheingoldgraph.HeaderMetadata\"5\n\x08LineNote\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x05\x12\x0b\n\x03\x64ot\x18\x03 \x01(\x05\x32\xc4\x03\n\x0eRheingoldGraph\x12L\n\nGetSummary\x12\x1e.rheingoldgraph.SummaryRequest\x1a\x1c.rheingoldgraph.GraphSummary\"\x00\x12\x44\n\x07GetLine\x12\x1b.rheingoldgraph.LineRequest\x1a\x18.tensorflow.magenta.Note\"\x00\x30\x01\x12G\n\x08\x44ropLine\x12\x1b.rheingoldgraph.LineRequest\x1a\x1c.rheingoldgraph.DropResponse\"\x00\x12L\n\x0f\x41\x64\x64LinesFromXML\x12\x1a.rheingoldgraph.XMLRequest\x1a\x1b.rheingoldgraph.AddResponse\"\x00\x12G\n\x0bSearchLines\x12\x1e.rheingoldgraph.HeaderMetadata\x1a\x14.rheingoldgraph.Line\"\x00\x30\x01\x12>\n\x07\x41\x64\x64Line\x12\x14.rheingoldgraph.Line\x1a\x1b.rheingoldgraph.LineSummary\"\x00\x62\x06proto3')
  ,
  dependencies=[music__pb2.DESCRIPTOR,])




_SUMMARYREQUEST = _descriptor.Descriptor(
  name='SummaryRequest',
  full_name='rheingoldgraph.SummaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line', full_name='rheingoldgraph.SummaryRequest.line', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=83,
)


_LINEREQUEST = _descriptor.Descriptor(
  name='LineRequest',
  full_name='rheingoldgraph.LineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rheingoldgraph.LineRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='excerpt_length', full_name='rheingoldgraph.LineRequest.excerpt_length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=136,
)


_XMLREQUEST = _descriptor.Descriptor(
  name='XMLRequest',
  full_name='rheingoldgraph.XMLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xml', full_name='rheingoldgraph.XMLRequest.xml', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='piece_name', full_name='rheingoldgraph.XMLRequest.piece_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=183,
)


_HEADERMETADATA = _descriptor.Descriptor(
  name='HeaderMetadata',
  full_name='rheingoldgraph.HeaderMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_date', full_name='rheingoldgraph.HeaderMetadata.created_date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='composer', full_name='rheingoldgraph.HeaderMetadata.composer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='rheingoldgraph.HeaderMetadata.session_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=261,
)


_GRAPHSUMMARY = _descriptor.Descriptor(
  name='GraphSummary',
  full_name='rheingoldgraph.GraphSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_vertices', full_name='rheingoldgraph.GraphSummary.total_vertices', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_edges', full_name='rheingoldgraph.GraphSummary.total_edges', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_lines', full_name='rheingoldgraph.GraphSummary.num_lines', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lines', full_name='rheingoldgraph.GraphSummary.lines', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=385,
)


_LINESUMMARY = _descriptor.Descriptor(
  name='LineSummary',
  full_name='rheingoldgraph.LineSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rheingoldgraph.LineSummary.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='rheingoldgraph.LineSummary.vertices', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=432,
)


_DROPRESPONSE = _descriptor.Descriptor(
  name='DropResponse',
  full_name='rheingoldgraph.DropResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rheingoldgraph.DropResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='rheingoldgraph.DropResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=479,
)


_ADDRESPONSE = _descriptor.Descriptor(
  name='AddResponse',
  full_name='rheingoldgraph.AddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rheingoldgraph.AddResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='rheingoldgraph.AddResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes_added', full_name='rheingoldgraph.AddResponse.notes_added', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=546,
)


_LINE = _descriptor.Descriptor(
  name='Line',
  full_name='rheingoldgraph.Line',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rheingoldgraph.Line.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='rheingoldgraph.Line.notes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='rheingoldgraph.Line.header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=657,
)


_LINENOTE = _descriptor.Descriptor(
  name='LineNote',
  full_name='rheingoldgraph.LineNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rheingoldgraph.LineNote.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='rheingoldgraph.LineNote.length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dot', full_name='rheingoldgraph.LineNote.dot', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=712,
)

_GRAPHSUMMARY.fields_by_name['lines'].message_type = _LINESUMMARY
_LINE.fields_by_name['notes'].message_type = _LINENOTE
_LINE.fields_by_name['header'].message_type = _HEADERMETADATA
DESCRIPTOR.message_types_by_name['SummaryRequest'] = _SUMMARYREQUEST
DESCRIPTOR.message_types_by_name['LineRequest'] = _LINEREQUEST
DESCRIPTOR.message_types_by_name['XMLRequest'] = _XMLREQUEST
DESCRIPTOR.message_types_by_name['HeaderMetadata'] = _HEADERMETADATA
DESCRIPTOR.message_types_by_name['GraphSummary'] = _GRAPHSUMMARY
DESCRIPTOR.message_types_by_name['LineSummary'] = _LINESUMMARY
DESCRIPTOR.message_types_by_name['DropResponse'] = _DROPRESPONSE
DESCRIPTOR.message_types_by_name['AddResponse'] = _ADDRESPONSE
DESCRIPTOR.message_types_by_name['Line'] = _LINE
DESCRIPTOR.message_types_by_name['LineNote'] = _LINENOTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SummaryRequest = _reflection.GeneratedProtocolMessageType('SummaryRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUMMARYREQUEST,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.SummaryRequest)
  ))
_sym_db.RegisterMessage(SummaryRequest)

LineRequest = _reflection.GeneratedProtocolMessageType('LineRequest', (_message.Message,), dict(
  DESCRIPTOR = _LINEREQUEST,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.LineRequest)
  ))
_sym_db.RegisterMessage(LineRequest)

XMLRequest = _reflection.GeneratedProtocolMessageType('XMLRequest', (_message.Message,), dict(
  DESCRIPTOR = _XMLREQUEST,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.XMLRequest)
  ))
_sym_db.RegisterMessage(XMLRequest)

HeaderMetadata = _reflection.GeneratedProtocolMessageType('HeaderMetadata', (_message.Message,), dict(
  DESCRIPTOR = _HEADERMETADATA,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.HeaderMetadata)
  ))
_sym_db.RegisterMessage(HeaderMetadata)

GraphSummary = _reflection.GeneratedProtocolMessageType('GraphSummary', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHSUMMARY,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.GraphSummary)
  ))
_sym_db.RegisterMessage(GraphSummary)

LineSummary = _reflection.GeneratedProtocolMessageType('LineSummary', (_message.Message,), dict(
  DESCRIPTOR = _LINESUMMARY,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.LineSummary)
  ))
_sym_db.RegisterMessage(LineSummary)

DropResponse = _reflection.GeneratedProtocolMessageType('DropResponse', (_message.Message,), dict(
  DESCRIPTOR = _DROPRESPONSE,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.DropResponse)
  ))
_sym_db.RegisterMessage(DropResponse)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESPONSE,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.AddResponse)
  ))
_sym_db.RegisterMessage(AddResponse)

Line = _reflection.GeneratedProtocolMessageType('Line', (_message.Message,), dict(
  DESCRIPTOR = _LINE,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.Line)
  ))
_sym_db.RegisterMessage(Line)

LineNote = _reflection.GeneratedProtocolMessageType('LineNote', (_message.Message,), dict(
  DESCRIPTOR = _LINENOTE,
  __module__ = 'rheingoldgraph_pb2'
  # @@protoc_insertion_point(class_scope:rheingoldgraph.LineNote)
  ))
_sym_db.RegisterMessage(LineNote)



_RHEINGOLDGRAPH = _descriptor.ServiceDescriptor(
  name='RheingoldGraph',
  full_name='rheingoldgraph.RheingoldGraph',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=715,
  serialized_end=1167,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSummary',
    full_name='rheingoldgraph.RheingoldGraph.GetSummary',
    index=0,
    containing_service=None,
    input_type=_SUMMARYREQUEST,
    output_type=_GRAPHSUMMARY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLine',
    full_name='rheingoldgraph.RheingoldGraph.GetLine',
    index=1,
    containing_service=None,
    input_type=_LINEREQUEST,
    output_type=music__pb2._NOTE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DropLine',
    full_name='rheingoldgraph.RheingoldGraph.DropLine',
    index=2,
    containing_service=None,
    input_type=_LINEREQUEST,
    output_type=_DROPRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddLinesFromXML',
    full_name='rheingoldgraph.RheingoldGraph.AddLinesFromXML',
    index=3,
    containing_service=None,
    input_type=_XMLREQUEST,
    output_type=_ADDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SearchLines',
    full_name='rheingoldgraph.RheingoldGraph.SearchLines',
    index=4,
    containing_service=None,
    input_type=_HEADERMETADATA,
    output_type=_LINE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddLine',
    full_name='rheingoldgraph.RheingoldGraph.AddLine',
    index=5,
    containing_service=None,
    input_type=_LINE,
    output_type=_LINESUMMARY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RHEINGOLDGRAPH)

DESCRIPTOR.services_by_name['RheingoldGraph'] = _RHEINGOLDGRAPH

# @@protoc_insertion_point(module_scope)
