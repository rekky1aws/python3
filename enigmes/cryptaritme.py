# 17. Un cryptarithme est une opération dans laquelle chaque
# chiffre a été remplacé par une lettre. Une même lettre représente tou-
# jours le même chiffre, deux lettres différentes représentent deux chiffres
# différents et aucun nombre ne peut commencer par un zéro. La figure 7
# montre un exemple de cryptarithme.

#   NEUF
# +   UN
# +   UN
# ------
#   ONZE
# Figure 7 - Cryptarithme

# À partir de cette addition en lettres, retrouver celle en chiffres.

# Variables : N,E,U,F,O,Z

count = 0

for e in range(10):
	for f in range(10):
		if(f not in [e]):
			for n in range(1,9):
				if(n not in [e,f]):
					for o in range(1,10):
						if(o not in [e,f,n]):
							for u in range(1,10):
								if (u not in [e,f,n,o]):
									for z in range(10):
										if (z not in [e,f,n,o,u]):
											count += 1
											neuf = 1000 * n + 100 * e + 10 * u + f 
											un = 10 * u + n
											onze = 1000 * o + 100 * n + 10 * z + e

											if (onze == (neuf + un + un)):
												print(f"  {neuf}\n+   {un}\n+   {un}\n------\n= {onze}\n")
												print(f"E = {e}, F = {f}, N = {n}, O = {o}, U = {u} et Z = {z}\n")


print(count)

