import random
from random import randint

def bubble_sort (tab):
	moved = True
	i = 0
	while(moved and (i < len(tab) - 1)):
		moved = False
		for j in range(len(tab)-1-i):
			if( tab[j] > tab[j+1] ):
				storage_var = tab[j]
				tab[j] = tab[j+1]
				tab[j+1] = storage_var
				moved = True
		i += 1
	return tab

def gen_tab_int (length, min = 0, max = 100):
	result = []
	for i in range(length):
		result.append(randint(min, max))
	return result

def test_sorted (tab) :
	is_sorted = True
	for i in range(len(tab)-1):
		if(tab[i] > tab[i+1]):
			is_sorted = False
	return is_sorted

def display_is_sorted (value):
	if (value):
		return "\033[32mGood\033[37m"
	else:
		return "\033[31mNot Good\033[37m"

for i in range(5):
	tab = gen_tab_int(10)
	print(tab)
	print(">",bubble_sort(tab))
	print(display_is_sorted(test_sorted(tab)))
	print()

tab = gen_tab_int(15)
print(tab)
print(display_is_sorted(test_sorted(tab)))