import help
import random

### Fungsi pembantu ###

def convertToChromosome(states):
	chromosome = []
	for i in range(len(states)):
		chromosome.append(states[i].getX())
		chromosome.append(states[i].getY())
	return chromosome

def getPopulation(states):
	population = []
	for i in range(len(states)):
		population.append(convertToChromosome(states[i]))
	return population

def findBestChromosome(states):
	return states[0]

### Fungsi genetic ###

def init(k):
	states = []
	for i in range(k):
		states.append(help.getListRandomized())
	return states
	
	# Mengubah tiap states (list of bidak) menjadi population (list of chromosome) 
	# population = getPopulation(states)

def evaluation(states):
	score = []
	for i in range(len(states)):
		score.append(help.score(states[i]))
	return score

def selection(states, fitness_score):
	pass
	# Mendapatkan index chromosome dengan fitness score terendah dan tertinggi

	# Menghapus chromosome terburuk dan menggandakan chromosome terbaik

	# Melakukakan pengacakan pada population

def crossover(states):
	pass

def mutation(states):
	pass

### Fungsi utama ###

def genetic(k):
	# Mendapatkan kumpulan list of bidak sebanyak k buah
	states = init(k)

	# Mendapatkan fitness score tiap chromosome
	fitness_score = evaluation(states)

	# Melakukan seleksi pada masing-masing chromosome berdasarkan fitness score
	selection(states, fitness_score)

	# Menentukan kumpulan gen yang akan dilakukan crossover
	crossover(states)

	# Melakukan mutasi pada chromosome terpilih
	mutation(states)

	# Mengembalikan chromosome terbaik dari hasil mutasi
	return findBestChromosome(states)