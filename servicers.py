# import required libraries & proto defn.
from proto import uploader_pb2_grpc, uploader_pb2
import uuid
import shutil

class UploaderServiceServicer(uploader_pb2_grpc.UploaderServiceServicer):
    ''' this servicer method will read the request from the iterator supplied
        by incoming stream and send back the response as unary
    '''
    def uploadFile(self, request_iterator, context):
        file_info = dict()
        tmp_path = f"{uuid.uuid4()}.tmp"

        with open(tmp_path, "wb+") as binary_file:
            while True:
                try:
                    request = next(request_iterator)
                    if getattr(request, "name"):
                        file_name = getattr(request, "name")
                    else:
                        ##### save to database/storage #####
                        binary_file.write(request.chunk)
                
                except StopIteration:
                    # simulate the response after saving to database
                    shutil.move(tmp_path, file_name)
                    file_info = {
                        "file_id": str(uuid.uuid4())
                    }
                        
                    # send the unary response back
                    return uploader_pb2.FileUploadResponse(**file_info)

        
