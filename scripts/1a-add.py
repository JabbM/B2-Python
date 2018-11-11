#!/usr/bin/python36

print("ecrire 2 nombres séparé par ENTER")
nb1 = int(input())
nb2 = int(input())


def add(param1, param2):
    if (type(param1) == int) and (type(param2) == int):
      result = param1 + param2
      print(result) 
    else:
      print("ce ne sont pas des chiffres")

add(nb1, nb2)



