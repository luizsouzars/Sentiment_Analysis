import re
import numpy as np
from nltk import word_tokenize
import nltk
# nltk.download('punkt')

texto = '''No meio do caminho tinha uma pedra
tinha uma pedra no meio do caminho
tinha uma pedra
no meio do caminho tinha uma pedra.
Nunca me esquecerei desse acontecimento
na vida de minhas retinas tão fatigadas.
Nunca me esquecerei que no meio do caminho
tinha uma pedra
tinha uma pedra no meio do caminho
no meio do caminho tinha uma pedra.'''

texto_min = texto.lower()

txt_letras = re.findall(r'[a-zéóáêâãõç]+', texto_min)

novo_texto = ' '.join(txt_letras)

tokens = word_tokenize(novo_texto)

vocab = []

for token in tokens:
    if token not in vocab:
        vocab.append(token)

def cria_vetor(documento,vocab):
    vetor = []

    for palavra in vocab:
        if palavra in documento:
            vetor.append(1)
        else:
            vetor.append(0)

    return np.array(vetor)

def dicionario_de_contagem(vocabulario,documento):
    dic = dict.fromkeys(vocabulario,0)
    for palavra in documento:
        dic[palavra] += 1

    return dic

print(dicionario_de_contagem(vocab,novo_texto.split()))