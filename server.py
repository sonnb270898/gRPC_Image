import grpc_img_pb2_grpc
import grpc_img_pb2
import grpc
from concurrent import futures
import logging
import cv2

class testImageServicer(grpc_img_pb2_grpc.testImageServicer):
    def __init__(self):
        pass
    
    def convert_img_to_bytes(self,request,context):
        # image = cv2.imread(request.img)
        # print('====================')
        # is_success, im_buf_arr = cv2.imencode(".jpg", image)
        # byte_im = im_buf_arr.tobytes()
        # return request.img
        pass

    def SendImage(self, request, context):
        print(request)
        return grpc_img_pb2.ImageReply(image=request.img)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_img_pb2_grpc.add_testImageServicer_to_server(
        testImageServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()