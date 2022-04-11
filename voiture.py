class Voiture:
	def __init__(self, marque: str, modele: str, carburant: str, type_carrosserie: str, vitesse:int=0): # Constructeur de l'objet
		self._marque = marque
		self._modele = modele
		self._carburant = carburant
		self._type_carrosserie = type_carrosserie
		self.set_vitesse(vitesse)

	def __str__(self): # Ce que retourne cette fonction sera affiché lorsque l'on voudra afficher ( avec print() ) un objet de cette classe
		return f"Objet (Voiture) : \n>\tMarque : {self._marque}\n>\tModele: {self._modele}\n>\tCarburant : {self._carburant}\n>\tType : {self._type_carrosserie}\n>\tVitesse : {self._vitesse}"

	def get_marque (self):
		return self._marque

	def get_modele (self):
		return self._modele

	def get_carburant(self):
		return self._carburant

	def get_type_carrosserie (self):
		return self._type_carrosserie

	def get_vitesse (self):
		return self._vitesse

	def set_vitesse (self, vitesse):
		if type(vitesse) is int:
			self._vitesse = vitesse
		else:
			self._vitesse=0
			print("La vitesse doit etre un nombre entier, par défaut elle a été mise à 0")





