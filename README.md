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
