import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


image_path = 'innomatics-logo-img.png'  # Replace with your actual PNG image file path

# Display the PNG image
st.image(image_path)

st.header("EMAIL SPAM OR HAM")


rfc=pickle.load(open("bowEmailSpam.pkl",'rb'))
with open("bowCVector.pkl","rb") as f:
    tf = pickle.load(f)

Email = st.text_area("Paste the email here:")


if Email:
   

    data=tf.transform([Email])
    result=rfc.predict(data)[0]

    if st.button('Submit'):
        if result == 'spam':
            st.write("It is a Spam:")
            st.image('spam.jpg')

        else:
            st.write("It is a ham:")
            st.image('safe.jpg')
