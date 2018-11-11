#!/usr/bin/python36
#             1c-moy.py
#             15/10/2018           #
#         Gabriel Clémençon        #
#           Jullian Bacle          #
####################################

import re
import statistics
from statistics import mean

regex_letter = re.compile ('[a-z]+')
regex_note = re.compile ('[0-9]+')
print('appuyer sur q pour quitter')
dic = {}
prenom = 0
valeur = 0
moy = 0

while valeur != 'q' or prenom != 'q':
  prenom = input("Entrez un prenom : ")
  valeur = input("Entrez une note : ")
  if valeur != 'q' or prenom != 'q':
    dic[prenom] = valeur

lengt = len(dic)

for k in dic.keys():
 moy = moy + int(dic[k])


moy = moy / lengt
print("La moyenne est de :", moy)
i = 0
a = 0

dic2 = sorted(dic.values(), reverse=True)

for key in dic.keys():
  if a != 5:
    print(key, 'à eu', dic2[i])
    i = i + 1
    a = a + 1

#quitter
#On verifie les regex
#On affiche la moyenne
#On classe les notes en ASC pour le top 5

