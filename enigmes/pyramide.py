# On importe la racine carrée depuis le module math
import math
from math import sqrt

def pyramide_boulets():
	sommes_precedentes = [4900, 10714447476283923160, 12468161476861877920, 37614623785401808860, 90344007169446735964, 104602885962245220264]
	sommes_precedentes = sommes_precedentes[0:-1:-1] # Pour supprimer les sommes en gardant la ligne au dessus (rajoute de la complexité algoritmique mais permet de decider si l'on sohaite trouver le premier, ou un rang supérieur).
	# On initialise
	somme = 1 # On skip etages = 0 car ce n'est pas une pyramide, et etages = 1 car l'artilleur a "des boulets". On commence donc la somme à 1.
	etages = 2

	while(True): # On teste toutes les possibilités jusque la bonne
		somme = somme + etages**2 # On ajoute un etage a la pyramide
		etages += 1 # On incrémente le nombre d'étages
		if ((sqrt(somme) == int(sqrt(somme))) and somme not in sommes_precedentes): # Si la somme des boulets dans notre pyramide est un carré, alors :
			print(somme, etages) # DEBUG : Pour voir la somme totale et le nombre d'étages.
			return somme


def nombre_lisible (nb): # En prends un nombre en paramètre et on mets un espace tous les 3 caractères en partant de la fin :
	string = str(nb)[::-1] # On inverse l'ecriture du nombre donné
	tab = [] # On initialise un tableau vide
	for i in range(len(string)): # On parcours tous les caractères de la chaine de caractères représentant le nombre
		if(i % 3 == 0 and i != 0): # Tous les trois caractères, on ajoute un espace
			tab.append(' ')
		tab.append(string[i]) # On ajoute le caractère dans le tableau
	result = "".join(tab[::-1]) # On inverse de nouveau le nombre en joinant tous les caractères
	return result # On retourne la chaine de caractère avec les espaces qui permet de lire plus aisément le nombre.


print(nombre_lisible(pyramide_boulets()))