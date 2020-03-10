import grpc
import grpc_img_pb2_grpc
import grpc_img_pb2
import logging
import PIL.Image as Image
import cv2
import io

def save_image(response):
    print("Image is recieved")
    image = Image.open(io.BytesIO(response.image)).save('test.jpg')

def convert_img_to_bytes():
    image = cv2.imread('ab.jpg')
    is_success, im_buf_arr = cv2.imencode(".jpg", image)
    byte_im = im_buf_arr.tobytes()
    return byte_im

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_img_pb2_grpc.testImageStub(channel)
        response = stub.SendImage(grpc_img_pb2.ImageRequest(img=convert_img_to_bytes()))
    save_image(response)
    



if __name__ == '__main__':
    logging.basicConfig()
    run()