
# Importing Required Libraries

import numpy as np 
import pandas as pd 
import cv2
import tensorflow as tf
from PIL import Image
import streamlit as st


# This module is imported so that we can  
# save the  audio 
from gtts import gTTS 
  
import os 
  


html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Traffic Sign Classifier </h2>
    </div>
    """

#this markdown line allows us to display the front end aspects we have  
# defined in the code 
#By default, any HTML tags found in the body will be escaped and therefore treated as pure text. This behavior may be 
#turned off by setting this argument to True.


st.markdown(html_temp,unsafe_allow_html=True)

#Loads the saved model into cache using streamlit's "@st.cache" feature
@st.cache(allow_output_mutation=True)

def load_model():
    model=tf.keras.models.load_model('model_traffic_sign.h5')
    return model

model=load_model()

# uploading image
uploaded_file=st.file_uploader("Please upload an image",type=["jpg","png"])

from PIL import Image,ImageOps

if uploaded_file is None:
    st.text("")
else:
    
    # opening image 
    image = Image.open(uploaded_file)
    
    # showing image in a html page
    st.image(image,width=250)
    
    #resizing image
    image = image.resize((30,30))
    
    #converting into array
    image = np.asarray(image)
    image=image[:, :, :3]
    
    image = np.array(image).reshape(1,30,30,3).astype(float)
    image=image/255
     
    pred = model.predict_classes(image)

    def getClassName(classNo):
        if classNo == 0:
            return 'Speed Limit 20 km/h'
        elif classNo == 1:
            return 'Speed Limit 30 km/h'
        elif classNo == 2:
            return 'Speed Limit 50 km/h'
        elif classNo == 3:
            return 'Speed Limit 60 km/h'
        elif classNo == 4:
            return 'Speed Limit 70 km/h'
        elif classNo == 5:
            return 'Speed Limit 80 km/h'
        elif classNo == 6:
            return 'End of Speed Limit 80 km/h'
        elif classNo == 7:
            return 'Speed Limit 100 km/h'
        elif classNo == 8:
            return 'Speed Limit 120 km/h'
        elif classNo == 9:
            return 'No passing'
        elif classNo == 10:
            return 'No passing for vechiles over 3.5 metric tons'
        elif classNo == 11:
            return 'Right-of-way at the next intersection'
        elif classNo == 12:
            return 'Priority road'
        elif classNo == 13:
            return 'Yield'
        elif classNo == 14:
            return 'Stop'
        elif classNo == 15:
            return 'No vechiles'
        elif classNo == 16:
            return 'Vechiles over 3.5 metric tons prohibited'
        elif classNo == 17:
            return 'No entry'
        elif classNo == 18:
            return 'General caution'
        elif classNo == 19:
            return 'Dangerous curve to the left'
        elif classNo == 20:
            return 'Dangerous curve to the right'
        elif classNo == 21:
            return 'Double curve'
        elif classNo == 22:
            return 'Bumpy road'
        elif classNo == 23:
            return 'Slippery road'
        elif classNo == 24:
            return 'Road narrows on the right'
        elif classNo == 25:
            return 'Road work'
        elif classNo == 26:
            return 'Traffic signals'
        elif classNo == 27:
            return 'Pedestrians'
        elif classNo == 28:
            return 'Children crossing'
        elif classNo == 29:
            return 'Bicycles crossing'
        elif classNo == 30:
            return 'Beware of ice/snow'
        elif classNo == 31:
            return 'Wild animals crossing'
        elif classNo == 32:
            return 'End of all speed and passing limits'
        elif classNo == 33:
            return 'Turn right ahead'
        elif classNo == 34:
            return 'Turn left ahead'
        elif classNo == 35:
            return 'Ahead only'
        elif classNo == 36:
            return 'Go straight or right'
        elif classNo == 37:
            return 'Go straight or left'
        elif classNo == 38:
            return 'Keep right'
        elif classNo == 39:
            return 'Keep left'
        elif classNo == 40:
            return 'Roundabout mandatory'
        elif classNo == 41:
            return 'End of no passing'
        elif classNo == 42:
            return 'End of no passing by vechiles over 3.5 metric tons'
    st.write("Class is " + str(getClassName(pred[0])))
    
    # The text that we want to convert to audio 
    mytext = 'The image shown belongs to the class of ' + str(getClassName(pred[0]) )
  
    # Language in which we want to convert 
    language = 'en'
  
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 
  
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("class_telling_audio.mp3") 
    audio_file = open('class_telling_audio.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg',start_time=0)
     