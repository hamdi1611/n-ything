from Bidak import Bidak
import help, math, random

# Algoritma Simulated-Annealing
# Masukan : list_of_object Bidak dan bilangan maksimum proses Simulated-Annealing
def annealing(list_of_object, temperature):
	current_list = list(list_of_object)
	best_list = list(list_of_object)
	current_e = help.score(current_list)
	best_e = current_e
	while(temperature > 1):
		next_list = list(help.getRandomTetangga(list_of_object))
		next_e = help.score(next_list)
		if(next_e >= current_e): 
			if(next_e > best_e):
				best_list = next_list
				best_e = next_e
			current_list = next_list
			current_e = next_e
		else:
			if(boltzman(current_e, next_e, temperature) >= random.random()):
				current_list = next_list
				current_e = next_e
		temperature = temperature_schedule(temperature)
	if(current_e > best_e):
		return current_list
	else:
		return best_list

def boltzman(e, ei, T):
	return math.exp((ei - e) / T)

def temperature_schedule(T):
	return T*0.8
