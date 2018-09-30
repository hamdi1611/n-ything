import help
import random

### Fungsi pembantu ###

def convertToChromosome(states):
	chromosome = []
	for i in range(len(states)):
		chromosome.append(states[i].getX())
		chromosome.append(states[i].getY())
	return chromosome

def findBestChromosome(states):
	return states[0]

### Fungsi genetic ###

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

def selection(states, population, fitness_score):
	# Mendapatkan index chromosome dengan fitness score terendah dan tertinggi
	worst_chromosome_index = fitness_score.index(min(fitness_score))
	best_chromosome_index = fitness_score.index(max(fitness_score))

	# Menghapus chromosome terburuk dan menggandakan chromosome terbaik
	states.pop(worst_chromosome_index)
	population.pop(worst_chromosome_index)

	if (len(population) % 2 == 1):
		states.append(best_chromosome_index)
		population.append(best_chromosome_index)

	# Melakukakan pengacakan pada population
	random.shuffle(states)
	random.shuffle(population)

def crossover(states):
	pass

def mutation(states):
	pass

### Fungsi utama ###

def genetic(k):
	# Mendapatkan kumpulan list of bidak sebanyak k buah
	states = init(k)

	# Mengubah tiap states (list of bidak) menjadi population (list of chromosome) 
	population = []
	for i in range(len(states)):
		population.append(convertToChromosome(states[i]))

	# Mendapatkan fitness score tiap chromosome
	fitness_score = evaluation(states)

	# Melakukan seleksi pada masing-masing chromosome berdasarkan fitness score
	selection(states, population, fitness_score)

	# Menentukan kumpulan gen yang akan dilakukan crossover
	crossover(states)

	# Melakukan mutasi pada chromosome terpilih
	mutation(states)

	# Mengembalikan chromosome terbaik dari hasil mutasi
	return findBestChromosome(states)