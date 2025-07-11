import numpy as np 
import streamlit as st 
import cv2
from keras.models import load_model
import tensorflow as tf 

model=load_model('plant_disease_model.h5')

CLASS_NAMES=['Mango','Lemon','Guava']

st.title("Plant Leaf Disease Detector")
st.markdown("Upload Plant Leaf Image")

plant_image=st.file_uploader("Choose an image..", type="jpg")
submit=st.button("Predict Diseases")

if submit:
    if plant_image is not None: 
        file_byte=np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        opencv_image=cv2.imdecode(file_bytes, 1)
        
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)
        
        opencv_image=cv2.resize(opencv_image, (256,256))
        
        opencv_image.shape=(1,256,256,3)
        
        Y_pred=model.prdict(opencv_image)
        result=CLASS_NAMES[np.argmax(Y_pred)]
        st.title(str("This is" +result.split('-')[0]+"leaf with"+result.split('-')[1]))
        
        
        