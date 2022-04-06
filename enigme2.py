# 2. Carré formé de deux nombres consécutifs

# 183 184 est le carre a six chiffres de 428. On remarque que ses trois
# premiers chiffres et ses trois derniers forment deux nombres consécutifs
# 183 et 184.
# Trouver 1'unique carré a huit chiffres tel que ses quatre premiers
# chiffres et ses quatre derniers représentent deux nombres consécutifs.

for i in range(1000, 9999):
	if(int(str(i)+str(i+1)))**0.5==int((int(str(i)+str(i+1)))**0.5):
		print(str(i)+str(i+1))
