import streamlit as st
import cv2
import numpy as np
from keras.models import load_model
from playsound import playsound

st.title("Person Not Wearing Mask Alert App")

model = load_model("Mask_Nomask.h5")
haarcascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

results = {0:"Mask Found",1:"Mask Not Found"}
box_color = {1:(0,255,255), 0:(0,255,0)}
box_size = 4

vid = cv2.VideoCapture(0)
status = st.radio("Camera Status",("OFF","ON"),key = "1")

while status== "ON":
    frame = vid.read()[1]
    frame = cv2.flip(frame,1,1)

    new_size = cv2.resize(frame,(frame.shape[1]//box_size,frame.shape[0]//box_size))
    faces = haarcascade.detectMultiScale(new_size)
    for f in faces:
        (x, y, w, h) = [v * box_size for v in f]
        face_img = frame[y:y+h, x:x+w]
        new_size = cv2.resize(face_img,(200,200))
        normalized = new_size/255.0
        reshaped = np.reshape(normalized,(1,200,200,3))
        reshaped = np.vstack([reshaped])
        result = model.predict(reshaped)

        label = np.argmax(result, axis = 1)[0]

        cv2.rectangle(frame,(x,y),(x+w, y+h), box_color[label], 2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),box_color[label], -1)
        cv2.putText(frame, results[label], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX ,0.8,(255,0,0),2)
        if label == 1:
            cv2.putText(frame, "Please wear a Mask", (x-20, y+h+30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
            playsound("Resources/voice_alert.mp3")

    cv2.imshow('Video Streaming',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        st.write("Camera Stopped")
        break
vid.release()
cv2.destroyAllWindows()