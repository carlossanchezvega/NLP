import pandas as pd
import string
import nltk


# se leen los ficheros
with open('./Data_Science.txt', 'r') as f:
    data_science = f.read()

with open('./Data.txt', 'r') as f:
    data = f.read()

with open('./Credit_Card.txt', 'r') as f:
    credit_card = f.read()

with open('./Science.txt', 'r') as f:
    science = f.read()


def elimina_signos_puntuacion(text):
    sinPuntuacion = set()
    tokens = nltk.word_tokenize(text)
    for palabra in tokens:
        # "isalpha" lo aplicaremos para eliminar palabras como "'s"
        if palabra not in string.punctuation and  palabra.isalpha():
            sinPuntuacion.add(palabra)
    return sinPuntuacion


def rellena_palabras_presentes (vocabulario_especifico, vocabulario_general):
    # inicializamos el hash a partir del conjunto que se recibe como parámetro (rellenando con 0's su valor)
    columna_diccionario = dict.fromkeys(vocabulario_general, '0')

    # rellenamos con '1' las palabras presentes para cada fichero
    for item in vocabulario_especifico:
        columna_diccionario[item]='1'
    return columna_diccionario


matriz_total={}

# se crean los conjuntos de cada uno de los ficheros
set_data_science = elimina_signos_puntuacion(data_science)
set_data = elimina_signos_puntuacion(data)
set_credit_card = elimina_signos_puntuacion(credit_card)
set_science = elimina_signos_puntuacion(science)
vocabulario  = set_data_science.union(set_data).union(set_credit_card).union(set_science)

# se crea la columna correspondiente al vocabulario de "Data_Science.txt"
hash_vocabulario_data_science = rellena_palabras_presentes(set_data_science,vocabulario)
matriz_total['Data_science.txt'] = hash_vocabulario_data_science

# se crea la columna correspondiente al vocabulario de "Data.txt"
hash_vocabulario_data = rellena_palabras_presentes(set_data,vocabulario)
matriz_total['Data.txt'] = hash_vocabulario_data

# se crea la columna correspondiente al vocabulario de "Credit_Card.txt"
hash_vocabulario_credit_card =  rellena_palabras_presentes(set_credit_card,vocabulario)
matriz_total['Credit_Card.txt'] = hash_vocabulario_credit_card

# se crea la columna correspondiente al vocabulario de "Science.txt"
hash_vocabulario_science = rellena_palabras_presentes(set_science,vocabulario)
matriz_total['Science.txt'] = hash_vocabulario_science


print("a. El número total de palabras diferentes juntando todos los textos : " + str(len(vocabulario))+ "\n")

print("b. Qué palabras aparecen en cada texto mediante TF (Term Frequency). Se debe llevar a cabo mediante una matriz (palabras x textos)"
      " que muestre 0 o 1 en la posición según si aparece o no la palabra en el texto\n")



df = pd.DataFrame(matriz_total)
print (df)
