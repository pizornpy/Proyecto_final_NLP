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
#df = pd.read_csv(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\phil_nlp.csv")
st.image(img, width=100)
st.write('# place_holder')

#Background intelectual
opciones_a = ['STEM', 'Economics/Bussiness', 'History', 'Literature', 'Philosophy','Sociology','Other/Surprise me']
selected_option1 = st.selectbox('What is your background?', opciones_a)

#Ramas de la filosofía
opciones_b = ['Science', 'Ethics', 'History of Philosophy', 'Metaphysics', 'Politics', 'Philosophy of Art']
selected_option2 = st.selectbox('What are you interested in?', opciones_b)


#Dificultad
opciones_c = ['Not much', 'I have some experience', 'I have read a lot']
selected_option3 = st.selectbox("How accustomed are you to reading Philosophy?", opciones_c)


respuestas = {"preg1":selected_option1, "preg2":selected_option2, "preg3":selected_option3}

if respuestas[preg1] == "STEM":
    rec =data[data["school"] == ["analytic", "phenomenology","rationalism","empiricism"]]
elif respuestas[preg1] =='Economics/Bussiness':
    rec = data[data["school"] == ["capitalism", "Ethics","empiricism"]]
elif respuestas[preg1] == "Literature":
    rec = data[data["school"]] == ["Continental"]:
elif respuestas[preg1] == "Philosophy":
    rec = data[data["school"] == []]
elif respuestas[preg1] == "History":
    rec = data[data["school"] == ["german_idealism","phenomenology","capitalism","communism"]]
elif respuestas[preg1] == "Other/Surprise me":
    pass








