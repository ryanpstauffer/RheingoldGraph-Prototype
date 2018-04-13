# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import rheingoldgraph.protobuf.music_pb2 as music__pb2
import rheingoldgraph.protobuf.rheingoldgraph_pb2 as rheingoldgraph__pb2


class RheingoldGraphStub(object):
  """RheingoldGraph service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSummary = channel.unary_unary(
        '/rheingoldgraph.RheingoldGraph/GetSummary',
        request_serializer=rheingoldgraph__pb2.SummaryRequest.SerializeToString,
        response_deserializer=rheingoldgraph__pb2.GraphSummary.FromString,
        )
    self.GetLine = channel.unary_stream(
        '/rheingoldgraph.RheingoldGraph/GetLine',
        request_serializer=rheingoldgraph__pb2.LineRequest.SerializeToString,
        response_deserializer=music__pb2.Note.FromString,
        )
    self.DropLine = channel.unary_unary(
        '/rheingoldgraph.RheingoldGraph/DropLine',
        request_serializer=rheingoldgraph__pb2.LineRequest.SerializeToString,
        response_deserializer=rheingoldgraph__pb2.DropResponse.FromString,
        )
    self.AddLinesFromXML = channel.unary_unary(
        '/rheingoldgraph.RheingoldGraph/AddLinesFromXML',
        request_serializer=rheingoldgraph__pb2.XMLRequest.SerializeToString,
        response_deserializer=rheingoldgraph__pb2.AddResponse.FromString,
        )
    self.SearchLines = channel.unary_stream(
        '/rheingoldgraph.RheingoldGraph/SearchLines',
        request_serializer=rheingoldgraph__pb2.HeaderMetadata.SerializeToString,
        response_deserializer=rheingoldgraph__pb2.Line.FromString,
        )


class RheingoldGraphServicer(object):
  """RheingoldGraph service definition.
  """

  def GetSummary(self, request, context):
    """Get a summary of musical information stored in our graph.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLine(self, request, context):
    """Get a sequence of ProtoBuf Notes from a Line 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropLine(self, request, context):
    """Remove a line and all associated musical content
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLinesFromXML(self, request, context):
    """Add lines in the graph from an XML file
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchLines(self, request, context):
    """Search lines in the graph by Header Metadata
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RheingoldGraphServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSummary': grpc.unary_unary_rpc_method_handler(
          servicer.GetSummary,
          request_deserializer=rheingoldgraph__pb2.SummaryRequest.FromString,
          response_serializer=rheingoldgraph__pb2.GraphSummary.SerializeToString,
      ),
      'GetLine': grpc.unary_stream_rpc_method_handler(
          servicer.GetLine,
          request_deserializer=rheingoldgraph__pb2.LineRequest.FromString,
          response_serializer=music__pb2.Note.SerializeToString,
      ),
      'DropLine': grpc.unary_unary_rpc_method_handler(
          servicer.DropLine,
          request_deserializer=rheingoldgraph__pb2.LineRequest.FromString,
          response_serializer=rheingoldgraph__pb2.DropResponse.SerializeToString,
      ),
      'AddLinesFromXML': grpc.unary_unary_rpc_method_handler(
          servicer.AddLinesFromXML,
          request_deserializer=rheingoldgraph__pb2.XMLRequest.FromString,
          response_serializer=rheingoldgraph__pb2.AddResponse.SerializeToString,
      ),
      'SearchLines': grpc.unary_stream_rpc_method_handler(
          servicer.SearchLines,
          request_deserializer=rheingoldgraph__pb2.HeaderMetadata.FromString,
          response_serializer=rheingoldgraph__pb2.Line.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rheingoldgraph.RheingoldGraph', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
