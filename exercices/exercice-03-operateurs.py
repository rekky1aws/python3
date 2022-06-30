# exercice-03-operateurs.py

# exo 3.1
# Alice est née le 10 février 1988.
# Quelle âge a-t-elle cette année ?
# Ne tenez pas compte du mois, on va partir du principe qu'on est après le 10 février pour ne pas se compliquer la vie.
# Stockez l'année en cours dans une variable nommée `year`.
# Calculez l'âge d'Alice en utilisant les variables `birthyear` et `year` puis stockez le résultat dans une variable nommée `age` et affichez ce résultat.
birthyear = 1988

print("3.1 :")

# réponse 3.1
year=2022
age=year-birthyear
print(age)

# exo 3.2
print(f"\n3.2 :")
# Bob veut distribuer tous ses bonbons et chocolats à ses amis.
# Il a 15 bonbons, 17 chocolats et 3 amis.
# Combien de bonbons lui restera-t-il ?
# Calculez le reste de bonbons et de chocolats puis stockez les résultats dans les variables `candies_rest` et `chocolates_rest`.
# Affichez ces résultats.
candies = 15
chocolates = 17
friends = 3

# réponse 3.2
candies_rest = candies%friends
chocolates_rest = chocolates%friends

print(candies_rest)
print(chocolates_rest)

# exo 3.3
print(f"\n3.3 :")
# Suite de l'exercice précédent.
# Calculez combien de bonbons et chocolats Bob va distribuer par personne et stockez les résultats dans les variables `candies_per_person` et `chocolates_per_person`.
# Affichez ces résultats.
#
# Indice : si vous séchez, reprenez le temps d'examiner la liste des opérateurs arithémtiques.
# Il y en a un qui va tout de suite vous donner la réponse.

# réponse 3.3
candies_per_person = candies // friends
chocolates_per_person = chocolates // friends

print(candies_per_person)
print(chocolates_per_person)

# exo 3.4
print(f"\n3.4 :")
# Calculez la moyenne des nombres suivants : 1, 1, 2, 3, 5, 8, 13.
# Affectez le résultat à une variable et affichez le résultat.

# réponse 3.4
moyenne = (1+1+2+3+5+8+13) / 7

print(moyenne)

# exo 3.5
print(f"\n3.5 :")
# Alice est en vacance et elle veut suivre ses dépenses quotidiennes.
# Stockez le montant de chacune de ses dépenses quotidiennes dans une variable différente :
# - day1 : 26,82
# - day2 : 42,00
# - day3 : 31,41
# - day4 : 63,7
# - day5 : 32
# Stockez le nombre de jours dans la variable `days`.
# Calculez le montant total des dépenses en utilisant les variables `day1`, `day2`, etc et stockez le résultat dans la variable `total`.
# Calculez la moyenne des dépenses quotidiennes en utilisant les variables `total` et `days` et stockez le résultat dans la variable `average`.
# Affichez le nombre jours, le montant total et la moyenne des dépenses.

# réponse 3.5
day1 = 26.82
day2 = 42.00
day3 = 31.41
day4 = 63.7
day5 = 32
total = day1+day2+day3+day4+day5
days=5
average=total/days
print(days,total,average)

# exo 3.6
print(f"\n3.6 :")
# La formule suivante permet de convertir des miles en mètres :
#
# meters = miles * 1609.344
#
# Bob est en Angleterre.
# On lui dit que la boulangerie la plus proche est à 3 miles.
# Calculez la distance en mètres avec la variable `miles` puis stockez le résultat dans la variable `meters`.
# Convertissez les mètres en kilo mètres puis stockez le résultat dans la variable `km`.
# Affichez un résultat arrondi de la distance en kilo mètre avec la fonction `round()`.
miles = 3

# réponse 3.6
meters = miles * 1609.344
km = meters / 1000
print(round(km))

# exo 3.7
print(f"\n3.7 :")
# La formule suivante permet de calculer le montant de la TVA à partir d'un prix « hors TVA » (HTVA) et du taux de la TVA en pourcentage
#
# tax_fee = price * tax_rate / 100
#
# La variable price contient le prix HTVA
# La variable tax_rate contient le taux de la TVA en pourcentage (c-à-d le nombre 20 si la TVA est de 20 %)
# Affichez le montant de la TVA à partir du prix HTVA et du taux de TVA

price = 314
tax_rate = 20

# réponse 3.7
tax_fee=price * tax_rate / 100
print(tax_fee)

# exo 3.8
print(f"\n3.8 :")
# La formule suivante permet de calculer un prix TVA inlcuse à partir du prix HTVA et du taux de TVA en pourcentage
#
# tax_included_price = price + price * tax_rate / 100
#
# ou encore
#
# tax_included_price = price * (1 + tax_rate / 100)
#
# La variable price contient le prix HTVA
# La variable tax_rate contient le taux de la TVA en pourcentage (c-à-d le nombre 20 si la TVA est de 20 %)
# Affichez le prix TVA incluse à partir du prix HTVA et du taux de TVA

price = 271
tax_rate = 20

# réponse 3.8
tax_included_price = price + price * tax_rate / 100
print(tax_included_price)

# exo 3.9
print(f"\n3.9")
# Charly fait ses courses.
# Il compare le prix de deux marques différentes de chocolat.
# La première marque propose une tablette à 1,79 euros (pour 120 g).
# La deuxième marque propose une tablette à 1,7 euros (pour 100 g).
# Charly a l'intuition que la première marque est plus avantageuse.
# A-t-il raison ?
# Calculez le prix au kilo puis stockez les résultat dans les variables `price_kilo_1` et `price_kilo_2`.
# Utilisez un opérateur de comparaison (qui doit donc renvoyer une valeur booléenne) pour vérifier si Charly a raison.
# Affichez le résultat booléen.

# réponse 3.9
price_kilo_1 = 1.79/120*1000
price_kilo_2 = 1.7/100*1000

print(price_kilo_1)
print(price_kilo_2)

intuition = price_kilo_1<price_kilo_2

print(intuition)
