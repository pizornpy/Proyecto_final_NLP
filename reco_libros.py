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
data = pd.read_csv(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\datos_final_final.csv")
st.image(img, width=100)
st.header('place_holder')
cop = data[["title","author","school","dif"]]

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
    if respuestas["preg1"] == "STEM":
        filt = data[data["school"].isin(["analytic", "phenomenology", "rationalism", "empiricism", "plato", "aristotle"])]

    elif respuestas["preg1"] == 'Economics/Bussiness':
        filt = data[data["school"].isin(["capitalism", "Ethics", "empiricism", "communism", "plato", "aristotle"])]

    elif respuestas["preg1"] == "Literature":
        filt = data[data["school"].isin(["continental", "communism", "plato", "aristotle", "german_idealism"])]

    elif respuestas["preg1"] == "History":
        filt = data[data["school"].isin(["german_idealism", "phenomenology","continental","capitalism", "communism", "plato", "aristotle"])]

    elif respuestas["preg1"] == "Sociology":
        filt = data[data["school"].isin(["german_idealism", "capitalism", "communism", "plato", "aristotle","continental"])]

    elif respuestas["preg1"] == "Other/Surprise me":
        filt = data  # Sin filtros

    #intereses

    
    if respuestas["preg2"] == "Science":
        filt = filt[filt['title'].str.contains("science|math|logic|physics|geometry|knowledge", case=False)]

    elif respuestas["preg2"] == "Ethics":
            filt = filt[filt['title'].str.contains("biology|ethics|ethic|practical", case=False)]
    
    elif respuestas["preg2"] == "History of Philosophy":
            filt = filt[filt['title'].str.contains("greek|greeks|history", case=False)]
    
    elif respuestas["preg2"] == "Metaphysics":
            filt = filt[filt['title'].str.contains("reason|metaphysics|spirit|phenomenology|being|time|reality", case=False)]
    
    elif respuestas["preg2"] == "Politics":
            filt = filt[filt['title'].str.contains("goverment|right|kapital|treatise|lenin|", case=False)]

    elif respuestas["preg2"] == "Philosophy of Art":
         filt = filt[filt["title"].str.contains("aesthic|art|nietzsche|greek|literature")]
    
    #dificultad

    if respuestas["preg3"] == "Not much": 
        filt = filt[filt['dif']<=29.0]
    
    elif respuestas["preg3"] == 'I have some experience': 
        filt = filt[(filt['dif']>29.0) & (filt['dif']<47.0)]
    
    elif respuestas["preg3"] == 'I have read a lot':
        pass
    
    return filt

if st.button("Show me what you got!"):
    # Call the reco function with the appropriate respuestas dictionary
    filtered_data = reco(respuestas)

    # Display the filtered DataFrame
    st.dataframe(filtered_data)

#por si quiere buscar directamente 
st.subheader("You can also search directly")


titulo = st.text_input('Enter a book title')
autor = st.text_input('Enter an author name')
school_options = [''] + list(cop['school'].unique())
school = st.selectbox('Select a school of thought', school_options)


if st.button('Filter'):
    if titulo.strip() == "" and autor.strip() == "" and school == "":
        st.warning("Please enter search criteria.")
    else:
        df_filt = cop[
            (cop['title'].str.contains(titulo, case=False) if titulo.strip() != "" else True) &
            (cop['author'].str.contains(autor, case=False) if autor.strip() != "" else True) &
            (cop['school'] == school if school != "" else True)]

        if df_filt.empty:
            st.warning("No results found.")
        else:
            st.write(df_filt)