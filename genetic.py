import help
import math

def convertToChromosome(states):
	chromosome = []
	for i in range(len(states)):
		chromosome.append(states[i].getX())
		chromosome.append(states[i].getY())
	return chromosome

def init(k):
	states = []
	for i in range(k):
		states.append(help.getListRandomized())
	return states

def evaluation(states):
	score = []
	for i in range(len(states)):
		score.append(help.score(states[i]))
	return score

def selection():
	pass

def crossover():
	pass

def mutation():
	pass

def genetic(k):
	# Mendapatkan kumpulan list of bidak sebanyak k buah	
	states = init(k)

	# Mengubah tiap states (list of bidak)  menjadi population (list of chromosome) 
	population = []
	for i in range(len(states)):
		population.append(convertToChromosome(states[i]))

	# Mendapatkan fitness score tiap chromosome
	fitness_score = evaluation(states)