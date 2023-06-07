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
data = pd.read_csv(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\df_final.csv")
st.image(img, width=100)
st.write('# place_holder')

#Background intelectual
opciones_a = ['STEM', 'Economics/Bussiness', 'History', 'Literature','Sociology','Other/Surprise me']
selected_option1 = st.selectbox('What is your background?', opciones_a)

#Ramas de la filosofía
opciones_b = ['Science', 'Ethics', 'History of Philosophy', 'Metaphysics', 'Politics', 'Philosophy of Art']
selected_option2 = st.selectbox('What are you interested in?', opciones_b)


#Dificultad
opciones_c = ['Not much', 'I have some experience', 'I have read a lot']
selected_option3 = st.selectbox("How accustomed are you to reading Philosophy?", opciones_c)


respuestas = {"preg1":selected_option1, "preg2":selected_option2, "preg3":selected_option3}
def reco(respuestas):
    #background intelectual
    if respuestas[preg1] == "STEM":
        rec =data[data["school"] == ["analytic", "phenomenology","rationalism","empiricism","plato", "aristotle"]]
    
    elif respuestas[preg1] =='Economics/Bussiness':
        rec = data[data["school"] == ["capitalism", "Ethics","empiricism","communism","plato", "aristotle"]]
    
    elif respuestas[preg1] == "Literature":
        rec = data[data["school"]] == ["Continental", "communism","plato", "aristotle","german_idealism"]
    
    elif respuestas[preg1] == "History":
        rec = data[data["school"] == ["german_idealism","phenomenology","capitalism","communism","plato", "aristotle"]]
    
    elif respuestas[preg1] == "Sociology":
        rec=data[data["school"]==["german_idealism","capitalism","communism","plato", "aristotle"]]    
    
    elif respuestas[preg1] == "Other/Surprise me":
        pass
    
    #intereses

   



#por si quiere buscar directamente 
st.write("#You can also search directly ")
titulo = st.text_input('Enter a book title')
autor = st.text_input('Enter an author name')
school = st.selectbox('Select a school of thought', data['school'].unique())


df_filt = data[
    (data['title'].str.contains(titulo, case=False)) &
    (data['author'].str.contains(autor, case=False)) &
    (data['school'] == school)]


st.write(df_filt)
