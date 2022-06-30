# Un artilleur sort ses boulets de canon et les dispose au sol en carré.
# Pour gagner de la place, il sohaite faire une pyramide avec ses boulets.
# Au minimum, combien lui faut-il de boulets de canon afin de former sa pyramide sans qu'il n'en manque un ?

from timeit import default_timer as timer

import math
from math import sqrt

nb_pass=1000000

# Start benchmark
start = timer()

for _ in range(nb_pass):
	taille=2
	total=5
	while int(sqrt(total))!=sqrt(total):
		taille+=1
		total+=taille**2

	print(total, taille)
	print(sqrt(total))

# Stop Benchmark
end = timer()
duration = (end-start)/nb_pass
print('Duration : ', duration)