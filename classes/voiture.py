from vehicule import Vehicule

class Voiture(Vehicule):
	# Nb Places, Nb Portes et type_carrosserie a ajouter en plus des propriétés de la classse Vehicule
	def __init__(self, marque:str, modele:str, carburant:str, ptac:int, type_carrosserie:str, nb_portes:int=5, nb_places:int=5, vitesse:int=0):
		self._marque=marque
		self._modele=modele
		self._carburant=carburant
		self._PTAC=ptac
		self._type_carrosserie=type_carrosserie
		self._nb_portes=nb_portes
		self._nb_places=nb_places
		self.set_vitesse(vitesse)

	def __str__(self):
		return f"""Objet (Voiture):
		>\tMarque : {self._marque}
		>\tModele : {self._modele}
		>\tCarburant : {self._carburant}
		>\tPTAC : {self.PTAC_en_kg()}
		>\tType de Carrosserie : {self._type_carrosserie}
		>\tNombre de Portes : {self._nb_portes}
		>\tNombre de Places : {self._nb_places}
		>\tVitesse : {self.get_vitesse()} km/h"""

	# GETTERS

	def get_type_carrosserie(self):
		return self._type_carrosserie

	def get_nb_portes(self):
		return self._nb_portes

	def get_nb_places(self):
		return self._nb_places

	# SETTERS


	