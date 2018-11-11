#!/usr/bin/python36

####################
#    2a-mol.py     #
# jeu + ou - 2.0   #
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
 return print(nb.read(), random)

regex = re.compile('^([0-9])|([0-9]{2}|100)$')
rand = randint(1, 100)

#ouverture en écriture puis lecture du fichier soluce.txt,
#et récupère son contenu pour l'afficher
nb = open("soluce.txt", "w")
nb.write("Bonjour")
nb = open("soluce.txt", "r")
result = nb.read()
nb.close
print(result)

nb = open("soluce.txt", "w")
nb.write(input("Entrez un nombre entre 0 et 100 : "))
nb = open("soluce.txt", "r")
result = nb.read()
nb.close()

#boucle pour comparer le contenu du fichier et le nombre random
while regex.match(result):
  if  int(result) < rand:
    nb = open("soluce.txt", "w")
    nb.write(input("Entrez un nombre plus grand : "))
    nb = open("soluce.txt", "r")
    result = nb.read()
    nb.close()
    if not regex.match(result):
      break
  elif int(result) > rand:
    nb = open("soluce.txt", "w")
    nb.write(input("Entrez un nombre plus petit : "))
    nb = open("soluce.txt", "r")
    result = nb.read()
    nb.close()
    if not regex.match(result):
      break
  elif int(result) == rand:
    nb = open("soluce.txt", "w")
    nb.write("Félicitation vous avez trouvé le chiffre qui était :")
    nb = open("soluce.txt", "r")
    soluce(rand)
    nb.read()
    break

#si l'utilisateur n'entre pas un nombre
if not regex.match(result):
  print("Vous n'avez pas entré de nombre")
print("Aurevoir")
