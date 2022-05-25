from vehicule import Vehicule

class Camion(Vehicule):
	def __init__(self, marque:str, modele:str, carburant:str, ptac:int, volume:int, vitesse:int=0):
		self._marque=marque
		self._modele=modele
		self._carburant=carburant
		self._PTAC=ptac
		self._volume=volume
		self.set_vitesse(vitesse)

	def __str__(self):
		return f"""Objet (Camion):
		>\tMarque : {self._marque}
		>\tModele : {self._modele}
		>\tCarburant : {self._carburant}
		>\tPTAC : {self.PTAC_en_kg()}
		>\tVolume : {self._volume}
		>\tVitesse : {self.get_vitesse()} km/h"""

	# GETTERS

	def get_volume(self):
		return self._volume

	# SETTERS


	