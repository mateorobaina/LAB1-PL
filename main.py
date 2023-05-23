from nltk.book import text1, text7
from nltk.tokenize import word_tokenize, re


#mysent = "The cat sat on the mat."
#mysent_tokens = word_tokenize(mysent)
#print(len(mysent_tokens))
#m =	re.search("leng",	"procesamiento	del	lenguaje natural")
#print(m.start())


#
moby_dick_tokens = text1.tokens
#1 Numeros de tokens en moby dick: 260819
#print(len(moby_dick_tokens))
#2 Numero de types: 19317
types_mb = set(moby_dick_tokens)
#print(len(types))
#3 Type token ratio: 7.406285585022563
#ttr_mobydick = (len(types_mb) / len(moby_dick_tokens)) * 100
#print(ttr_mobydick)
#4 Lo mismo para WSJ, su ratio es de 12.32468512853113
wsj_tokens = text7.tokens
#types_wsj = set(wsj_tokens)
#ttr_wsj = (len(types_wsj) / len(wsj_tokens)) * 100
#print(ttr_wsj)
#5 WSJ
#6 El diario abarca mas cantidad de topics a comparacion de moby dick.
#7 el mle de la palabra whale es 0.003473673313677301 en moby dick.
whale = "whale"
ocurrencias_md = moby_dick_tokens.count(whale)
mle_md = ocurrencias_md / len(moby_dick_tokens)
#print(mle_md)
ocurrencias_wsj = wsj_tokens.count(whale)
mle_wsj = ocurrencias_wsj / len(wsj_tokens)
print(mle_wsj)
#7 el mle de la palabra whale es 0.0 en WSJ.
