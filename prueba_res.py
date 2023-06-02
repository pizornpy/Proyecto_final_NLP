import pandas as pd 
from transformers import pipeline
from joblib import Parallel, delayed


data = pd.read_csv(r"C:\Users\Juan\Desktop\Proyecto_final_NLP\dataen.csv")
data =data.drop(["Unnamed: 0"], axis=1)

def separar(str, leng):
    return [str[i:i+leng] for i in range(0, len(str), leng)]

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
def resumir(str): 
    lista =separar(str,1024)
    resumenes = Parallel(n_jobs=6)(delayed(summarizer)(l, len(l), len(l)/3, do_sample=False) for l in lista)
    print("La primera parte funciona")
    return resumenes

r = resumir(data.at[0, "work"])

print(r)
for i in r:
    print(type(i))

