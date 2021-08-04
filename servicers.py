# import required libraries & proto defn.
from proto import uploader_pb2_grpc, uploader_pb2
import uuid

class UploaderServiceServicer(uploader_pb2_grpc.UploaderServiceServicer):
    ''' this servicer method will read the request from the iterator supplied
        by incoming stream and send back the response as unary
    '''
    def uploadFile(self, request_iterator, context):
        chunks = []
        file_name = None
        for request in request_iterator:
            if getattr(request, "name") is not None:
                file_name = getattr(request, "name")
            else:
                chunks.append(request.chunk)
        print("************", file_name)
        
        ##### save to database/storage #####
        with open(file_name, "wb") as binary_file:
            for chunk in chunks:
                binary_file.write(chunk)

        # simulate the response after saving to database
        file_info = dict()
        file_info = {
            "file_id": str(uuid.uuid4())
        }

        # send the unary response back
        return uploader_pb2.FileUploadResponse(**file_info)
