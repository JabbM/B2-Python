#!/usr/bin/python36

import re

regex = re.compile('^[a-z][0-9][q]$')

saisi = input("Entrez un prénom et une note :").split(" ")
length = (len(saisi) - 1)

def moy(param):
    if regex.match(saisi):
      number = number + saisi[1]
      i+=1
      print(number)
      print(i)
    if saisi[2] != "q":
      saisi = input().split(" ")

moy(saisi)

