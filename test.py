#!/usr/bin/python3


# import de lib sys
import sys

print(sys.version_info)
print(sys.version)

print(sys.platform)

print("hello mon ami")
print("tu trouveras le fichier dans c:\\reda")

string = 'spam'
print(string)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
a
print(a[:4])
print(a[-4:])
print(a[3:-3])
print(a[4:-4])
print(len(a))

i=5
mykey='temps'
fois=20
print("La valeur %d et le mot '%s' apparaissent %d fois." %(i, mykey, fois))
print("La valeur {} et le mot '{}' apparaissent {} fois.".format(i, mykey, fois))

valeur1="toto"
valeur2="titi"
if valeur1=="toto" and valeur2=="titi" : print('OK..')
# elif valeur3=="tata" : print('peu OK')
else:print('KO')


seq=[1,2,3,4]
a,b,c,d=seq
print(a)

for letter in 'spam' : print("curent letter", letter)
fruits=['banane', 'pomme', 'mangue']
for fruit in fruits:
  #  if fruit=='banane' : print(fruit[2])
   # elif fruit=='pomme' : print(fruit[1])
   # elif fruit=='mangue' : print(fruit[0])
   # break
    print("mon fruit..:", fruit)

for num in range(1,10):
    print(num)
    if num==5:
        continue
    if num==7:
        break
print(

)
var=10
while True:
    var-=1
    if var==6:
        continue
    print(var)
    if var==0:
        break
print("end loop")

print(

)
a=[1,2,3,4,5,6,7,8,9]
squares=[x**2 for x in a]
print(squares)

#on a deux variables temps et distance

print(

)
temps=6.896
distance=19.7

vitesse = distance / temps
msg='La vitesse est de : {:.2f} metre par seconde'
print('la vitesse est %.2f:' % vitesse, 'metre par seconde')
print('La vitesse est : {:.2f} metre par seconde'.format(vitesse))
print(msg.format(vitesse))
print(

)
#en utilisant la foncion range
#afficher les entiers de 0 à 3
#de 4 à 7

for num in range(0,10):
    print(num)
    if num==0:
        continue
    if num==3:
        break
print(

        )
for num in range(0, 10):
    if num >3:
        print(num)
    if num == 7:
        break

#avec une boucle afficher les caractères de la chaine suivante
print(

)
msg="c'est la formation DevOps"
for c in msg:
    print(c)

#sur la liste suivante faire les actions suivantes
liste=[17,38,10,25,72]

#trier et afficher la liste
print(

)
liste.sort()
print(liste)

#ajouter l'element 12 et afficher la liste
print(

)
liste.append(12)
print(liste)

#afficher l'indice de l'element 17
print(

)
print(liste.index(17))

#enlevez l'element 38 et afficher la lise
print(

)
liste.remove(38)
print(liste)

#afficher la sous-liste du 3eme element jusquà la fin de la liste
print(

)
print(liste[2:])

#"https://github.com/redafakir/Python.git"
#aficher a git