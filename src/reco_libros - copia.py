import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import re
import plotly.graph_objects as go
import networkx as nx

img = Image.open(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\lechuza3.png")
data = pd.read_csv(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\datos_final_final.csv")
st.image(img, width=100)
st.title('Philoapp')
cop = data[["title","author","school","dif"]]

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import io
import plotly.express as px

@st.cache_data  # Cache the image generation function
def generate_graph_image():
    # Create the graph
    G = nx.Graph()

    # Define the philosophical genres and their relationships
    generos = ['Metaphysics', 'History of Philosophy', 'Politics', 'Philosophy of Science', 'Philosophy of Art', 'Ethics']
    relaciones = [(0, 1), (0, 2), (1, 4), (0, 5), (5, 2), (0, 3), (2, 3)]
    
    # Add the nodes to the graph except 'History of Philosophy'
    for genero in generos:
        if genero != 'History of Philosophy':
            G.add_node(genero)

    # Add the relationships to the graph excluding those involving 'History of Philosophy'
    for relacion in relaciones:
        if generos[relacion[0]] != 'History of Philosophy' and generos[relacion[1]] != 'History of Philosophy':
            G.add_edge(generos[relacion[0]], generos[relacion[1]])

    G.add_edge('Philosophy of Art', 'Ethics')
    pos = nx.spring_layout(G, seed=42)  # Use a seed to ensure consistent layout on each execution
    pos = {node: (x, y-0.1) for node, (x, y) in pos.items()}  # Slightly shift the nodes downward

    # Configure the graph layout
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_size=10, node_size=1000)

    # Configure the title and axes
    plt.title('A thematic map of philosophy')
    plt.axis('off')
    fig = plt.gcf()
    fig.set_size_inches(10, 6)  # Adjust the width and height as needed
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.tight_layout()
    
    return buffer

# Display the image in Streamlit
buffer = generate_graph_image()

met ='''
Metaphysics: Metaphysics is a branch of philosophy that explores fundamental questions about the nature of reality. It delves into the nature of existence, identity, time, space, causality, and the relationship between mind and matter. Metaphysics examines concepts such as substance, being, essence, and the ultimate nature of things. It seeks to understand the fundamental principles and structures that underlie the physical world and our experiences within it. 
'''
hist = '''
History of Philosophy: The history of philosophy is the study of philosophical ideas and thinkers throughout time. It traces the development of philosophical thought from ancient civilizations to the present day. This field examines various philosophical movements, such as ancient Greek philosophy, medieval philosophy, Renaissance philosophy, Enlightenment philosophy, and modern and contemporary philosophy. The history of philosophy provides insights into how ideas have evolved, influenced one another, and shaped the course of intellectual history.'
'''
pol ='''
Politics: Politics is the branch of philosophy concerned with the study of governance, power, and the organization of human societies. It explores questions about the nature of political authority, the origins of political systems, the distribution of power, the ethics of political action, and the ideal forms of government. Political philosophy also examines concepts such as justice, rights, liberty, equality, democracy, and the role of individuals and communities in shaping the social and political order.'
'''
sci = '''
hilosophy of Science: The philosophy of science investigates the nature, methods, and limits of scientific knowledge. It examines the underlying assumptions, principles, and methodologies employed in scientific inquiry. Philosophers of science explore concepts such as the scientific method, causality, explanation, confirmation, induction, and the nature of scientific theories. They also delve into the relationship between science and other areas of human knowledge, such as metaphysics, epistemology, and ethics.'
'''

art='''
Philosophy of Art: The philosophy of art explores questions concerning the nature, meaning, and value of art. It examines the aesthetic experience, artistic creation, interpretation, and the criteria for assessing artistic quality. Philosophers of art explore concepts such as beauty, expression, representation, creativity, and the relationship between art and truth. They also explore the cultural, historical, and social dimensions of art and its role in human life and society.
'''
eth='''
Ethics: Ethics is the branch of philosophy concerned with moral principles, values, and the study of what is right and wrong. It examines questions about how individuals should act, what constitutes a good life, and the foundations of moral judgments. Ethical theories provide frameworks for evaluating human behavior and making ethical choices. They explore concepts such as consequentialism, deontology, virtue ethics, and ethical relativism. Ethics also investigates topics like moral responsibility, justice, moral reasoning, and the relationship between ethics and other branches of philosophy.
'''

if st.button('Where to start?'):
    st.header("Topics")
    st.subheader("Metaphysics")
    st.write(met)
    st.subheader("History of Philosophy")
    st.write(hist)
    st.subheader("Political Philosophy")
    st.write(pol)    
    st.subheader("Philosophy of Science")
    st.write(sci)
    st.subheader("Philosophy of Art")
    st.write(art)
    st.subheader("Ethics")
    st.write(eth)
    st.image(buffer)


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
        filt = data[data["school"].isin(["continental", "communism", "plato", "aristotle", "german_idealism", "phenomenology", "analytic"])]

    elif respuestas["preg1"] == "History":
        filt = data[data["school"].isin(["german_idealism", "phenomenology","continental","capitalism", "communism", "plato", "aristotle"])]

    elif respuestas["preg1"] == "Sociology":
        filt = data[data["school"].isin(["german_idealism", "capitalism", "communism", "plato", "aristotle","continental"])]

    elif respuestas["preg1"] == "Other/Surprise me":
        filt = data  # Sin filtros

    #intereses

    
    if respuestas["preg2"] == "Science":
        filt = filt[filt['title'].str.contains("science|math|mathematics|logic|physics|geometry|knowledge", case=False)]

    elif respuestas["preg2"] == "Ethics":
            filt = filt[filt['title'].str.contains("biology|ethics|ethic|practical", case=False)]
    
    elif respuestas["preg2"] == "History of Philosophy":
            filt = filt[filt['title'].str.contains("greek|greeks|history", case=False)]
    
    elif respuestas["preg2"] == "Metaphysics":
            filt = filt[filt['title'].str.contains("reason|metaphysics|spirit|phenomenology|being|time|reality", case=False)]
    
    elif respuestas["preg2"] == "Politics":
            filt = filt[filt['title'].str.contains("goverment|right|kapital|treatise|lenin|nations", case=False)]

    elif respuestas["preg2"] == "Philosophy of Art":
         filt = filt[filt["title"].str.contains("aesthic|art|nietzsche|greek|literature"|filt["sentence_lo"].str.contains, case=False)]
    
    #dificultad

    if respuestas["preg3"] == "Not much": 
        filt = filt[filt['dif']<=29.0]
    
    elif respuestas["preg3"] == 'I have some experience': 
        filt = filt[(filt['dif']<=47.0)]
    
    elif respuestas["preg3"] == 'I have read a lot':
        pass #los filtros están así porque no está de más revisitar autores "sencillos" aunque se sepa mucho
    
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



dat = pd.DataFrame({"lat":[51.24083,50.08087,46.58022,48.6616,44.47588,40.7251,52.39057,48.77585,51.364344,52.37022,46.97354,48.85661,38.96375,52.20534,51.50735,37.98392,40.59167,33.76009,51.3397,43.61077,49.74999,
                           51.25621,51.81165,41.90278,55.95325,48.20817,37.88818,49,51.15211,56],
                    "lon":[12.11611,10.56645,0.34038,9.11564,-73.21207,-73.2453,13.06447,9.18293,-2.7652,4.89517,0.69867,2.35222,35.24332,0.12182,-0.12776,23.72936,23.79472,-0.12844,12.37307,3.87672,6.63714,
                           7.15076,-2.7163,12.49637,-3.18827,16.37382,-4.77938,2.4,14.13617,-3.19],
                    "name":["Nietzsche|1884-1900|","Kant|1724-1804|","Foucault|1926-1984|","Heidegger|1889-1976|","Dewey|1859-1952|","Kripke|1940-2022|","Ernst Haeckel|1834-1919|","Hegel|1770-1831|","Locke|1632-1704|",
                    "Spinoza|1632-1677|","Descartes|1596-1650|","Voltaire|1694-1778|","Epictetus|55-135|","Keynes|1883-1946|","Mill|1806-1873|","Plato|427-347 a.C|","Aristotle|384-322 a.C|","Derrida|1930-2004|",
                    "Leibniz|1646-1716|","Comte|1798-1857|", "Marx|1818-1883|","Engels|1820-1895|","Russel|1872-1970|","Boethius|480-524|","Hume|1711-1776|","Popper|1902-1994|","Averroes|1126-1198|","Malebranche|1638-1715|","Fichte|1762-1814|","Smith|1723-1790|"]})


# Mapa
import plotly.express as px
if st.button('Show map'):
    fig = px.scatter_mapbox(dat, lat="lat", lon="lon",
    hover_name='name', zoom=3)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)