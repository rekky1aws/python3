import random

my_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis id congue ante. Ut vitae quam posuere, sollicitudin dui id, laoreet massa. Phasellus interdum erat at congue luctus. Praesent maximus malesuada venenatis. Sed sit amet rutrum ligula, non porta dui. Nam lacinia, ante ut suscipit varius, tortor risus consectetur ipsum, vel ullamcorper dui enim eu lorem. Maecenas pellentesque hendrerit scelerisque. Curabitur viverra nulla quam, eget ultrices arcu dignissim non. Donec sodales libero massa, at luctus velit consectetur ac."
splitted_text=my_text.replace(',', '')
splitted_text=splitted_text.replace('.', '')
splitted_text=splitted_text.split()

debut=random.randint(0, len(splitted_text))
fin=random.randint(0, len(splitted_text))

splitted_text=splitted_text[min(debut,fin):max(debut,fin)]

print(splitted_text)
print(len(splitted_text))

partial_list=splitted_text[3:7]
print(partial_list)

# exo
# 1 - Récuperer dans splitted_text les mots de l'index 35 à 49 inclus
print("\n\t1. :")

partial_list=splitted_text[35:50]
print(partial_list)

# 2 - Afficher le numéro du dernier index
print("\n\t2. :")

last_index=len(splitted_text)-1
print(last_index)

# 3 - Récupérer 1 mot sur 2 de l'index 0 au dernier index
print("\n\t3. :")

# partial_list=[]
# for i in range(last_index+1):
# 	if i%2==1:
# 		partial_list.append(splitted_text[i])

partial_list=splitted_text[0:last_index+1:2]

print(partial_list)


# 4 - Créez trois listes contenant :
#		- Le premier mot sur trois
#		- Le deuxieme mot sur trois
#		- Le troisième mot sur trois
print("\n\t4. :")

partial_list1=splitted_text[0:last_index+1:3]
partial_list2=splitted_text[1:last_index+1:3]
partial_list3=splitted_text[2:last_index+1:3]

print(partial_list1)
print(partial_list2)
print(partial_list3)







