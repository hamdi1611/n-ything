from Bidak import Bidak
import help, math, random

# Algoritma Simulated-Annealing
# Masukan : list_of_object Bidak dan bilangan maksimum proses Simulated-Annealing
def annealing(list_of_object, n, temperature, temperature_param):
	current_list = list(list_of_object)
	best_list = list(list_of_object)
	current_e = help.score(current_list)
	best_e = current_e
	current_temperature = temperature
	i = 0
	while(i < n):
		next_list = list(help.getRandomTetangga(list_of_object))
		next_e = help.score(next_list)
		if(next_e >= current_e): 
			if(next_e > best_e):
				best_list = list(next_list)
				best_e = next_e
			current_list = list(next_list)
			current_e = next_e
		else:
			if(boltzman(current_e, next_e, current_temperature) >= random.random()):
				current_list = list(next_list)
				current_e = next_e
		current_temperature = temperature_schedule(temperature, i, temperature_param)
		i += 1
	if(current_e > best_e):
		return current_list
	else:
		return best_list

def boltzman(e, ei, T):
	prob = math.exp((ei - e) / T)
	return prob

def temperature_schedule(T, k, param):
	return T / (1 + param * math.log(1 + k, 10))
