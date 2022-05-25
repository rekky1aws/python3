import random
nbCartes=5
cartes=[]
n=random.randint(1,nbCartes)
cartes.append(n)

for i in range(nbCartes-1):
	while True:
		n=random.randint(1, nbCartes)
		if n not in cartes:
			break
	cartes.append(n)

print(cartes)

# exo 1 : affichez les nombres de 100 à 999 avec une boucle for
print("\n Exo 1 :")

for i in range(100, 1000):
	print(i, end=" ")

# exo 2 : affichez les nombres de 0 à 20 qui sont des multiples de 3
print("\n Exo 2 :")

for i in range(0, 21, 3):
	print(i, end=" ")

# exo 3 : affichez les nombres de 10 à 1 à rebours
print("\n Exo 3 :")

for i in range(10, 0, -1):
	print(i, end=" ")

# info : la fonction range() prend un troisième paramètre qui indique le "pas" (step)
print()