#!/usr/bin/python36

####################
#    2b-mol.py     #
# jeu + ou - auto  #
#  Jullian Bacle   #
#Gabriel Clemencon #
####################

from random import randint
import signal
import sys
import re

#fonction pour quitter proprement avec CTRL + C
def youcant(sig, frame):
    print("\nVous avez quitté")
    sys.exit(0)

signal.signal(signal.SIGINT, youcant)

#fonction return la phrase de win
def soluce(random):
 print("Le nombre a été trouvé -> ", random)

regex = re.compile('^([0-9])|([0-9]{2}|100)$')
rand = randint(0, 100)
success = False

#initialisation des bornes pour le nombre random
min = 0
max = 100
auto = randint(min,max)

#ouverture en écriture puis lecture du fichier soluce.txt,
#et récupère son contenu pour l'afficher
nb = open("soluce.txt", "w")
nb.write("**Bonjour**")
nb = open("soluce.txt", "r")
result = nb.read()
nb.close
print(result)

print("**Recherchez le nombre mystère**")
print("---Script en cours---")


nb = open("soluce.txt", "w")
nb.write(str(auto))
nb = open("soluce.txt", "r")
result = nb.read()

#boucle qui permet de rechercher le nombre random selon le contenu du fichier
while success == False:
  if  int(result) < rand:
    min = auto
#Les bornes de min et max rapetisse au fur et a mesure jusqu'à trouver le nombre désiré
    auto = randint(min, max)
    nb = open("soluce.txt", "w")
    nb.write(str(auto))
    nb = open("soluce.txt", "r")
    result = nb.read()
    nb.close()
#   print(result)
    if not regex.match(result):
      break
  elif int(result) > rand:
    max = auto
    auto = randint(min, max)
    nb = open("soluce.txt", "w")
    nb.write(str(auto))
    nb = open("soluce.txt", "r")
    result = nb.read()
    nb.close()
#   print(result)
    if not regex.match(result):
      break
  elif int(result) == rand:
    nb = open("soluce.txt", "w")
    nb.write("Félicitation")
    nb.close()
    print("---Script terminé---")
    soluce(rand)
    break

print("**Aurevoir**")
