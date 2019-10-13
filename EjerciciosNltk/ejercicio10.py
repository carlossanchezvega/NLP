import nltk, string


def escribe_notaciones (frases):
    for frase in frases:

        palabras = nltk.word_tokenize(frase)
        lTokens = nltk.pos_tag(palabras)
        for lToken in lTokens:
            if lToken[0] not in string.punctuation and  lToken[0].isalpha():
                print("- NOTACION POR DEFECTO:["+lToken[0]+"]->"+lToken[1])
                print("+ NOTACION UNIVERSAL: ["+lToken[0]+"]->" +traduce_notacion_universal(lToken[1])+"\n")

def es_nombre(palabra):
    return palabra in ['NN', 'NNS', 'NNP', 'NNPS']

def es_verbo(palabra):
    return palabra in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def es_adverbio(palabra):
    return palabra in ['RB', 'RBR', 'RBS']

def es_adjectivo(palabra):
    return palabra in ['JJ', 'JJR', 'JJS']


def traduce_notacion_universal(palabra):
    if es_adjectivo(palabra):
        return "ADJ"
    elif es_nombre(palabra):
        return "NOUN"
    elif es_adverbio(palabra):
        return "ADV"
    elif es_verbo(palabra):
        return "VERB"
    return palabra

with open('./Data_Science.txt','r',encoding='utf-8') as f:
    text=f.read()
    f.close()

frases = nltk.sent_tokenize(text, 'english')

escribe_notaciones(frases)
