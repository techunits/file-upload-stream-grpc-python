# import required libraries & proto defn.
import grpc
from proto import uploader_pb2_grpc, uploader_pb2

# initialize channel to gRPC server
channel = grpc.insecure_channel(target="localhost:50051")

# create service stub
stub = uploader_pb2_grpc.UploaderServiceStub(channel=channel)

# define file upload request object generator which will yield file into chunks
def entry_request_iterator():
    for idx in range(1, 16):
        entry_request = uploader_pb2.FileUploadRequest(name=f"Test {idx}", 
                                                        code=f"T{idx}",
                                                        description=f"Test {idx} description")
        yield entry_request

# iterate through response stream and print to console
for entry_response in stub.createBulkEntries(entry_request_iterator()):
    print(entry_response)
