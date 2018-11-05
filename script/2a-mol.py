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

def youcant(sig, frame):
    print("\nVous avez quitté")
    sys.exit(0)

signal.signal(signal.SIGINT, youcant)

def soluce(random):
 print(nb.read(), random)

regex = re.compile('[0-9]+|q')
rand = randint(1, 100)

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

while result:
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
    break
#  elif string(result) == 'q':
#    nb = open("soluce.txt", "w")
#    nb.write("Vous avez quitté")
#    nb = open("soluce.txt", "r")

print("Aurevoir")
