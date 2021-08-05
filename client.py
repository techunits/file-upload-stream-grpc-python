# import required libraries & proto defn.
import grpc
import os
from proto import uploader_pb2_grpc, uploader_pb2

# initialize channel to gRPC server
channel = grpc.insecure_channel(target="localhost:50051")

# create service stub
stub = uploader_pb2_grpc.UploaderServiceStub(channel=channel)

# define file upload request object generator which will yield file into chunks
def file_request_iterator(file_path, chunk_size=64):
    # yield filename
    yield uploader_pb2.FileUploadRequest(name=os.path.basename(file_path))
    
    # yield file data
    with open(file_path, 'rb') as fp:
        while True:
            data = fp.read(chunk_size)
            if not data:
                break
            yield uploader_pb2.FileUploadRequest(chunk=data)

# stream file upload request and fetch response async
file_path = './resources/sconnector-intro.mp4'
upload_response_future = stub.uploadFile.future(file_request_iterator(file_path=file_path))
upload_response = upload_response_future.result()

print(upload_response)
