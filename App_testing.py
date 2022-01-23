import streamlit as st
import cv2
import numpy as np

#st.camera_input("Test")
camera = st.camera_input("Test")
while camera:
    bytes_data = camera.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8),cv2.IMREAD_COLOR)
    cv2_img
# img_file_buffer = st.camera_input("Take a picture")
#
# if img_file_buffer is not None:
#     # To read image file buffer with OpenCV:
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#
#     # Check the type of cv2_img:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(cv2_img))
#
#     # Check the shape of cv2_img:
#     # Should output shape: (height, width, channels)
#     st.write(cv2_img.shape)

















# def main():
#     st.title("No Mask Alert App")
#     vid = cv2.VideoCapture(0)
#     # status = st.button("Start Camera",disabled = True)
#     # if status:
#     #     st.button("Now")
#     # st.write(status)
#
#
#     #picture = st.camera_input("Take a picture")
#
#     # if picture:
#     #     st.image(picture)
#     # while status == 'ON':
#     #     ret, frame = vid.read()
#     #     cv2.imshow('frame',frame)
#     #     # the 'q' button is set as the
#     #     # quitting button you may use any
#     #     # desired button of your choice
#     #     if cv2.waitKey(1) & 0xFF == ord('q'):
#     #         st.write("Camera Stopped")
#     #         break
#     # vid.release()
#     # cv2.destroyAllWindows()
#
#
# if __name__ == '__main__':
#     main()