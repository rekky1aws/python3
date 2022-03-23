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
