# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import uploader_pb2 as uploader__pb2


class UploaderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.uploadFile = channel.stream_unary(
                '/UploaderPkg.UploaderService/uploadFile',
                request_serializer=uploader__pb2.FileUploadRequest.SerializeToString,
                response_deserializer=uploader__pb2.FileUploadResponse.FromString,
                )


class UploaderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def uploadFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UploaderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'uploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.uploadFile,
                    request_deserializer=uploader__pb2.FileUploadRequest.FromString,
                    response_serializer=uploader__pb2.FileUploadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UploaderPkg.UploaderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UploaderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def uploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/UploaderPkg.UploaderService/uploadFile',
            uploader__pb2.FileUploadRequest.SerializeToString,
            uploader__pb2.FileUploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
