class Vehicule:
	"""
		Cette classe permet de créer des vehicules en fonction de leur marque, leur modele, leur type de carburant, leur type de carrosserie, leur poids total a charge en kilos et leur vitesse.
		Attention c'est une classe abstraite.
		Elle est destinéee à être étendue par des classes enfants.
	"""
	def __init__(self, marque: str, modele: str, carburant: str, ptac:int, vitesse:int=0): # Constructeur de l'objet
		self._marque = marque
		self._modele = modele
		self._carburant = carburant
		self._PTAC = ptac
		self.set_vitesse(vitesse)

	def __str__(self) -> str: # Ce que retourne cette fonction sera affiché lorsque l'on voudra afficher ( avec print() ) un objet de cette classe
		return f"Objet (Voiture) : \n>\tMarque : {self._marque}\n>\tModele: {self._modele}\n>\tCarburant : {self._carburant}\n>\tVitesse : {self._vitesse}"

	# GETTERS
	def get_marque (self) -> str:
		return self._marque

	def get_modele (self) -> str:
		return self._modele

	def get_carburant(self) -> str:
		return self._carburant

	def get_vitesse (self) -> int:
		return self._vitesse

	def get_PTAC (self) -> int:
		return self._PTAC

	def PTAC_en_kg(self) -> str :
		return f"{self.get_PTAC()} kg"

	def PTAC_en_T(self) -> str:
		return f"{self.get_PTAC()/1000} tonnes"

	# SETTERS
	def set_vitesse (self, vitesse):
		if type(vitesse) is int:
			self._vitesse = vitesse
		else:
			self._vitesse=0
			print("La vitesse doit etre un nombre entier, par défaut elle a été mise à 0")
	
	def accelerer (self):
		self._vitesse+=20

	def ralentir (self):
		self._vitesse-=10




