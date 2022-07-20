import itertools

carre = [
	[0, 0, 1, 0],
	[0, 4, 0, 0],
	[2, 0, 0, 0],
	[0, 0, 0, 3]
]

def verif_resolu (carre) :
	sommes = []

	# Lignes
	for ligne in carre :
		sommes.append(sum(ligne))

	# Colonnes
	for i in range(len(carre[0])) :
		somme_temp = 0
		for j in range(len(carre)) :
			somme_temp += carre[j][i]
		sommes.append(somme_temp)
	
	# Diagonales
	somme_temp = 0
	somme_temp_bis = 0
	for i in range(len(carre)):
		somme_temp += carre[i][i]
		somme_temp_bis += carre[i][len(carre) - i -1]
	sommes.append(somme_temp)
	sommes.append(somme_temp_bis)

	for i in range(len(sommes) - 1):
		if sommes[i] != sommes[i + 1]:
			return False
	
	return True

def resoudre_carre (carre) :
	cases_zero = []
	nombres_presents = []
	nb_cases = 0
	for i in range(len(carre)):
		for j in range(len(carre[i])) :
			nb_cases += 1
			if carre[i][j] == 0:
				cases_zero.append([i, j])
			else :
				nombres_presents.append(carre[i][j])

	nombres_a_placer = []
	for i in range(1, nb_cases+1) :
		if i not in nombres_presents :
			nombres_a_placer.append(i)

	# print(cases_zero)
	# print(nombres_presents)
	# print(nombres_a_placer)

	nb_permut = 0
	for permut in itertools.permutations(nombres_a_placer) :
		nb_permut += 1
		carre_a_tester = carre
		for i in range(len(permut)) :
			carre_a_tester[cases_zero[i][0]][cases_zero[i][1]] = permut[i]
		est_resolu = verif_resolu(carre_a_tester)
		if est_resolu:
			return carre_a_tester
		else :
			print(f"Essai n°{nb_permut} : Echec")

	return None

def afficher_carre (carre) :
	for i in range(len(carre) * 4 + 1) :
		print("-", end="")
	print()
	for i in range(len(carre)):
		for j in range(len(carre[i])) :
			print("|", end=" ")
			if carre[i][j] != 0:
				print(carre[i][j], end=" ")
			else:
				print(" ", end=" ")
		print("|")
		for i in range(len(carre) * 4 + 1):
			print("-", end="")
		print()
	print("\n")

afficher_carre(carre)
carre_resolu = resoudre_carre(carre)

if carre_resolu == None :
	print("Aucun carré magique fonctionnel n'a été trouvé...")
else :
	afficher_carre(carre_resolu)