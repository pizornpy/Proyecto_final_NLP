import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import re

img = Image.open(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\lechuza3.png")
#data = pd.read_csv(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\phil_nlp.csv")
st.image(img, width=100)
st.write('# place_holder')

#Background intelectual
opciones_a = ['STEM', 'Economics/Bussiness', 'History', 'Literature', 'Philosophy' ,'Other/Surprise me']
selected_option1 = st.selectbox('What is your background?', opciones_a)

#Ramas de la filosofía
opciones_b = ['Science', 'Ethic', 'History of Philosophy', 'Metaphysics', 'Politics','Aesthetics']
selected_option2 = st.selectbox('What are you interested in?', opciones_b)


#Dificultad
opciones_c = ['Not much', 'I have some experience', 'I have read a lot']
selected_option3 = st.selectbox("How accustomed are you to reading Philosophy?", opciones_c)


respuestas = {"preg1":selected_option1, "preg2":selected_option2, "preg3":selected_option3 }