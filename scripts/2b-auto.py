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

def youcant(sig, frame):
    print("\nVous avez quitté")
    sys.exit(0)

signal.signal(signal.SIGINT, youcant)

def soluce(random):
 print("Le nombre a été trouvé -> ", random)

regex = re.compile('[0-9]+|q')
rand = randint(0, 100)

min = 0
max = 100
auto = randint(min,max)

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

while result:
  if  int(result) < rand:
    min = auto
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
