# Nécessite la présence de voiture.py dans le même dossier.
from voiture import Voiture
from camion import Camion

v1 = Voiture("Renault", "Modus", "Diesel", 500, "Monospace")
v2 = Voiture("Ford", "Mustang 68", "Essence", 700, "MuscleCar", 3)

print(v1)
print(v2)

#exit()

print(v1.get_marque())

v1.set_vitesse(50)

print(v1)

v2.accelerer()
print(v2.get_vitesse())

# print(v2.PTAC_en_T())

print("\n\n\n")

c1 = Camion("Scania", "?", "Sans-Plomb 95", 3500, 500)

print(c1)