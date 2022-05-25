a=42
b=123

#Version avec Variable de Stockage
# c=a
# a=b
# b=c

#Version Arithmétique
# a=a+b
# b=a-b
# a=a-b

#Versione en affectation double
# a,b=b,a

#Version Logique
a=a^b
b=a^b
a=a^b


if a==123 and b==42:
	print("Vous avez réussi")
else:
	print("Non car :")
	print("a =",a,"et b =", b)


def arrondi(n: float):
	pDeci=n-int(n)
	if pDeci>0.4:
		return int(n)
	else:
		return int(n)+1

for i in range(10):
	print(i+0.5, round(i+0.5), arrondi(i+0.5))