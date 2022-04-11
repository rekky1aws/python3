# Nécessite la présence de voiture.py dans le même dossier.
from voiture import Voiture

v1 = Voiture("Renault", "Modus", "Diesel", "Monospace", "non")
v2 = Voiture("Ford", "Mustang 68", "Essence", "MuscleCar")

print(v1)
print(v2)

print(v1.get_marque())

v1.set_vitesse(50)

print(v1)