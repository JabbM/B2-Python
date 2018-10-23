#!/usr/bin/python36

####################
#    1d-mol.py     #
#   jeu + ou -     #
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
 print("Bravo le nombre a trouver était : ", random)

regex = re.compile('[0-9]+|q')
rand = randint(0, 100)
nb = input("Entrez un nombre entre 0 et 100 :  ")

while nb != 'q' and regex.match(nb):
  if int(nb) < rand:
    nb = input("Entrez un nombre plus grand :  ")
  elif int(nb) > rand: 
    nb = input("Entrez un nombre plus petit :  ")
  elif int(nb) == rand:
    soluce(rand)
    break

print("Aurevoir")
