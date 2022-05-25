import random

has_cash = bool(random.randint(0,1))
has_card = bool(random.randint(0,1))
has_check = bool(random.randint(0,1))

print("has_cash :",has_cash)
print("has_card :",has_card)
print("has_check :",has_check)

print()

if has_cash or has_card or has_check:
	if has_cash:
		print("Tu as de l'espèce")
	if has_card:
		print("Tu as ta CB")
	if has_check:
		print("Tu as ton carnet de chèques")
	print("\t-> Tu peux aller aux courses")
else:
	print("Tu n'as aucun moyen de paiement")

