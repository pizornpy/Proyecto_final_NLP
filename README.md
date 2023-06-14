<<<<<<< HEAD
# Proyecto Final NLP

## Objetivo:
·Hacer un sistema de recomendación de libros que permita al usuario seleccionar sus intereses, su background intelectual y el nivel de dificultad que desea. Además, así tengo la oportunidad de trabajar con redes neuronales convolucionales (CNN) y utilizar varias técnicas de procesamiento de lenguaje natural. También practicaré con Streamlit para crear una interfaz gráfica que pueda usar el usuario.

## Problemas: 

### ·¿Cómo etiquetar los libros? 
Vamos a etiquetarlos según escuelas y a usar el conocimiento propio para elegir diseñar las recomendaciones más adecuadas, pero sigue quedando el cómo. Vamos a utilizar un CSV de Kaggle con algunos textos etiquetados y una red neuronal construida con Keras para que clasifique automáticamente. Este es el dataframe resultante del CSV etiquetado:

![]("C:\Users\Juan\Desktop\Proyecto_final_NLP\img\df_og.png")



### ·¿De dónde sacar los libros?
Ya tenemos la información de referencia con la que va a aprender el modelo, pero necesitamos el qué clasificar. Vamos a scrapear los libros de Proyect Gutenberg, ahí los podemos encontrar de libre acceso, además también hemos sacado y trasteado con el escrapeo de Internet Archive y también he utilizado algún texto al que le apliqué técnicas de Optical Character Recognition, (OCR)(https://es.wikipedia.org/wiki/Reconocimiento_%C3%B3ptico_de_caracteres), para un proyecto previo. Como suele pasar, por falta de tiempo no hemos utilizado todo lo que hemos encontrado. 

Otro problema ha sido cómo tratar los libros, la red fue entrenada con textos de unos 200 carácteres, los libros tienen unos 300.000 de media. En principio iba a utilizar algún modelo tipo BERT(https://huggingface.co/docs/transformers/model_doc/bert) de Hugginface, pero eran textos demasiado largos. Luego pensé dividir y resumir con este modelo varias veces cada libro, es decir, partirlo en fragmentos que pudiese resumir el modelo (1024 caracteres), resumir cada uno de ellos, juntarlos, volver a hacer las divisiones y volver a resumir,etc. Este enfoque requería de una capacidad de computación que simple y llanamente no tengo. 

En su lugar hice una bag of words, es decir, guardar todas las palabras que aparecen en el texto y cómo de frecuentes son para seleccionar las palabras más importantes. Antes de eso tenía que quitar las palabras que no aportan significado y que sin embargo son las que más aparecen. Cosas como preposiciones, artículos, cuantificadores y demás no tienen significado o lo tienen en tanto que modifiquen a un sustantivo. Para ello utilicé NLTK, otra librería de Python, que permite quitar las stopwords, estas palabras, de forma relativamente sencilla. Ya tenía textos de una longitud parecida a aquello con los que los iba a clasificar. 


### .¿Cómo clasificarlos? 
Tras estudiar Keras y las distintas capas que puede tener una red neuronal para NLP, me decidí por lo siguiente 

![](C:\Users\Juan\Desktop\Proyecto_final_NLP\img\keras_config.png)


### Resumiento e intentándolo hacer accesible:
El modelo secuencial es una pila lineal de capas, donde se pueden agregar capas una tras otra.

La primera capa que se agrega al modelo es una capa de incrustación (Embedding). Esta capa se utiliza para convertir secuencias de palabras en vectores  de longitud fija. 

En segundo lugar se agrega una capa convolucional (Conv1D) con 128 filtros y una ventana de tamaño 5. Esta capa aplica filtros convolucionales a la secuencia de incrustación para extraer características relevantes del texto. 

A continuación agregamos una capa de agrupación global máxima (GlobalMaxPooling1D). Esta capa reduce la dimensión de la salida de la capa convolucional tomando el valor máximo en cada dimensión. Ayuda a reducir el número de parámetros y a capturar las características más importantes de las convoluciones.

Finalmente, la capa densa final es la que se encarga de asignar la problabilidad de que cada cada texto de entrada pertenezca a una clase de salida, tiene un par de ajustes que pretenden evitar el sobreentreno del modelo. Con la intención de evitar el sobreentreno del modelo hemos realizado un ajuste de las clases, pues había algunas que estaban sobre representadas. Simplemente le he dicho al modelo que cada vez que aparezca una clase en la fase de entrenamiento reduzca o aumente el valor que le da a esa aparición.

## Streamlit

Finalmente usamos Streamlit para la interfaz, añadimos un mapa conceptual y una breve explicación a los motores de búsqueda. Tambíen incluimos un mapa interactivo con algunos puntos marcados con el lugar de nacimiento y fecha de nacimiento y muerte de algunos autores, todo con la intención de hacer más sencilla la contexualización. 

![]("C:\Users\Juan\Desktop\Proyecto_final_NLP\img\buscador.png")

![]("C:\Users\Juan\Desktop\Proyecto_final_NLP\img\filtros.png")


![]("C:\Users\Juan\Desktop\Proyecto_final_NLP\img\mapa.png")
=======
# PROYECTO FINAL

Para este proyecto el objetivo era realizar un sistema de recomendación de libros de filosofía basado en el usuario, sus intereses, gustos y nivel de conocimiento del usuario. Igualmente hemos añadido un mapa con una selección de autores y su lugar de nacimiento, además de fecha de nacimiento y de defunción. Además hemos añadido una breve explicación con los campos temáticos de la filosofía y un mapa conceptual. 

Hemos realizado una ETL de Project Gutenberg, The Internet Archive y de un CVS de History of Philosophy con algunos textos etiquetados por escuela. 

A la hora de clasificar los libros hemos entrenado una red neuronal con Keras, que se encuentra en el Jupyter llamado "Pruebas Keras".  En primer lugar, e crea una instancia del modelo secuencial mediante la línea model = Sequential(). El modelo secuencial es una pila lineal de capas, donde se pueden agregar capas una tras otra.

    La primera capa que se agrega al modelo es una capa de incrustación (Embedding). Esta capa se utiliza para convertir secuencias de palabras en vectores densos de longitud fija. El parámetro input_dim se establece en la longitud del índice de palabras del tokenizador más uno, lo que indica el tamaño del vocabulario de entrada. El parámetro output_dim se establece en 100, lo que significa que cada palabra se representará como un vector denso de longitud 100. El parámetro input_length se establece en la longitud máxima de secuencia, que es la longitud máxima de palabras en una frase.

    En segundo lugar se agrega una capa convolucional (Conv1D) con 128 filtros y una ventana de tamaño 5. Esta capa aplica filtros convolucionales a la secuencia de incrustación para extraer características relevantes del texto. La función de activación 'relu' se utiliza para introducir no linealidad en las salidas de las convoluciones.
A continuación agregamos una capa de agrupación global máxima (GlobalMaxPooling1D). Esta capa reduce la dimensión de la salida de la capa convolucional tomando el valor máximo en cada dimensión. Ayuda a reducir el número de parámetros y a capturar las características más importantes de las convoluciones.

Después añadimos una capa densa (Dense) con 64 unidades y una función de activación 'relu'. Esta capa completamente conectada se utiliza para aprender patrones más complejos a partir de las características extraídas anteriormente.
Se agrega una capa de regularización (Dropout) con una tasa de 0.2. El dropout ayuda a prevenir el sobreajuste al desactivar aleatoriamente un porcentaje de las unidades de la capa anterior durante el entrenamiento.
Se agrega una capa de salida (Dense) con num_classes unidades y una función de activación 'softmax'. Esta capa produce la distribución de probabilidad de las clases de salida, donde cada unidad representa la probabilidad de que la entrada pertenezca a una clase específica.
Finalmente el modelo se compila utilizando el optimizador 'adam' y la función de pérdida 'sparse_categorical_crossentropy'. El optimizador Adam es un algoritmo popular de optimización basado en gradiente estocástico. La función de pérdida 'sparse_categorical_crossentropy' se utiliza para problemas de clasificación con múltiples clases.
Además de la función de pérdida, se especifica la métrica de 'accuracy' para evaluar el rendimiento del modelo durante el entrenamiento y la evaluación.

Hemos cometido varios errores a la hora de hacer la red, en primer lugar, no hemos dado cuenta del desbalanceo de clases, por lo que la primera versión de este estaba overfiteado, y hemos tenido que reentrenarlo. 

Para el front hemos utilizado streamlit, pensando en la usabilidad y en introducir a un neófito a la filosofía.
>>>>>>> 3fe2294baa620fa34c4ab020531c3a4c2064c14d
