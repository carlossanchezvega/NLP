import re, nltk
import string



def palabras_en_un_solo_texto (vocabulario1, vocabulario2, vocabulario3, vocabulario4):
    return (vocabulario1 ^ vocabulario2 ^ vocabulario3 ^ vocabulario4)


# hacemos todas las posibles combinaciones de intersecciones 2 a 2, porque la interseccion de dos conjuntos puede
#  no devolver elementos comunes respecto a la union con otro conjunto
def palabras_en_mas_de_un_texto (vocabulario1, vocabulario2, vocabulario3, vocabulario4):
    en_mas_de_un_texto= set()
    en_mas_de_un_texto = en_mas_de_un_texto.union(vocabulario1.intersection(vocabulario2))
    en_mas_de_un_texto = en_mas_de_un_texto.union(vocabulario1.intersection(vocabulario3))
    en_mas_de_un_texto = en_mas_de_un_texto.union(vocabulario1.intersection(vocabulario4))
    en_mas_de_un_texto = en_mas_de_un_texto.union(vocabulario2.intersection(vocabulario3))
    en_mas_de_un_texto = en_mas_de_un_texto.union(vocabulario2.intersection(vocabulario4))
    en_mas_de_un_texto = en_mas_de_un_texto.union(vocabulario3.intersection(vocabulario4))
    return en_mas_de_un_texto




# b. El tamaño del vocabulario para cada texto.
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
        if palabra not in string.punctuation and   palabra.isalpha():
            sinPuntuacion.add(palabra)
    return sinPuntuacion





set_data_science = elimina_signos_puntuacion(data_science)
set_data = elimina_signos_puntuacion(data)
set_credit_card = elimina_signos_puntuacion(credit_card)
set_science = elimina_signos_puntuacion(science)
concatenacion = set_data_science.union(set_data).union(set_credit_card).union(set_science)

print("a. El número total de palabras diferentes juntando todos los textos : " + str(len(concatenacion))+ "\n")
print("b. El tamaño del vocabulario para cada texto :\n")
print("- Data_Science.txt: "+str(len(set_data_science))+"\n")
print("- Data.txt: "+str(len(set_data))+"\n")
print("- Credit_card.txt: "+str(len(set_credit_card))+"\n")
print("- Science.txt: "+str(len(set_science))+"\n")
print("c. El vocabulario completo juntando todos los textos : \n");
print(concatenacion)
print("\n")
print("d. Palabras que están en un solo texto:")
print(palabras_en_un_solo_texto(set_data_science,set_data, set_credit_card, set_science ))
print("e. Palabras que están en más de un texto:")
print(palabras_en_mas_de_un_texto(set_data_science,set_data, set_credit_card, set_science ))
