#!/usr/bin/python36
######################################
#           `1d-mol.py`              #
#        jeu plus ou moins           #
#           23/10/2018               #
#        Gabriel Clémençon           #
######################################

from random import randint
import signal
import re
import sys


def exit_properly(sig, frame):
  print("User asked for exit. Exiting...")
  sys.exit(0)

signal.signal(signal.SIGINT, exit_properly)

regex = re.compile('[0-9]+|q')
nbToFound = randint(0, 100)
print (nbToFound)
nb = input('Veuillez rentrer un nombre entre 1 et 100 : ')

def endMsg():
  print ('aurevoir, la solution était : ', nbToFound)

while regex.match(nb) and nb != 'q':
    if int(nb) > nbToFound:
     nb =  input ('Trop grand, rentrer un nombre plus petit : ')
    elif int(nb) < nbToFound:
     nb = input ('Trop petit, rentrer un nombre plus grand : ')
    elif int(nb) == nbToFound:
      endMsg()
      break
