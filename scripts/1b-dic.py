#!/usr/bin/python36

prenom = input().split(" ")
long = (len(prenom) - 1)


def pren(param):
  if param[long] == 'q':
    return param
#  else:
#    print("finir la chaines de prénom par 'q'")



toto = pren(prenom)

toto.remove('q')

toto.sort()

print(toto)



