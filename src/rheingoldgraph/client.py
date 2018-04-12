"""RheingoldGraph gRPC Client."""

# import asyncio
# import websockets

from __future__ import print_function

import grpc

import rheingoldgraph.protobuf.rheingoldgraph_pb2 as rgpb
import rheingoldgraph.protobuf.rheingoldgraph_pb2_grpc as rgrpc


class RheingoldGraphClient:
    """Remote client of RheingoldGraph."""
    def __init__(self, server_uri):
        channel = grpc.insecure_channel(server_uri) 
        self.stub = rgrpc.RheingoldGraphStub(channel)


    def get_summary(self):
        """Get a summary of the complete graph."""
        # TODO: Allow for subgraph summaries as well 
        summary_request = rgpb.SummaryRequest(line='bach_cello')

        return self.stub.GetSummary(summary_request) 


    def add_lines_from_xml(self, filename, piece_name):
        """Add lines from an XML file."""
        with open(filename, 'rb') as f:
            xml_string = f.read() 
        xml_request = rgpb.XMLRequest(xml=xml_string, piece_name=piece_name)

        return self.stub.AddLinesFromXML(xml_request)


    def get_playable_line(self, line_name): 
        """Get a generator of Notes""" 
        # TODO(ryan): We still have nested generators
        # Try to improve this efficiency
        line_request = rgpb.LineRequest(name=line_name)
        notes = self.stub.GetPlayableLine(line_request)
        for note in notes:
            yield note


    def drop_line(self, line_name):
        """Drop a line."""
        drop_request = rgpb.LineRequest(name=line_name)
        return self.stub.DropLine(drop_request)


if __name__ == '__main__':
    server_uri = 'localhost:50051'
    client = RheingoldGraphClient(server_uri)

