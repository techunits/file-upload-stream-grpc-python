# import required libraries & proto defn.
from proto import uploader_pb2_grpc, uploader_pb2
import uuid

class UploaderServiceServicer(uploader_pb2_grpc.UploaderServiceServicer):
    ''' this servicer method will read the request from the iterator supplied
        by incoming stream and send back the response in a stream
    '''
    def uploadFile(self, request_iterator, context):
        for request in request_iterator:
            print(request)
            print("\n\n")

            ##### save to database/storage #####

        # simulate the response after saving to database
        file_info = dict()
        file_info = {
            "file_id": str(uuid.uuid4())
        }

        # stream the response back
        return uploader_pb2.FileUploadResponse(**file_info)
