import help
import random

#######################
### Fungsi Pembantu ###
#######################

# Mengubah state yang merupakan list of Bidak menjadi kromosom yang merupakan list of koordinat
def convertStateToChromosome(state):
	chromosome = []
	for i in range(len(state)):
		chromosome.append(state[i].getX())
		chromosome.append(state[i].getY())
	return chromosome

# Mengembalikan kromosom yang skornya paling tinggi dibandingkan yang lain
def findBestChromosome(population):
	bestChromosomeIndex = 0
	for i in range(len(population) - 1):
		if help.score(population[i]["state"]) > help.score(population[bestChromosomeIndex]["state"]):
			bestChromosomeIndex = i
	return population[bestChromosomeIndex]

#######################
### Fungsi Genetic ####
#######################

# Inisiasi populasi dengan sejumlah kromosom sesuai inputan pengguna 
def init(totalChromosome):
	population = []
	for _ in range(totalChromosome):
		randomizedState = help.getListRandomized()
		population.append({ 
			"state": randomizedState, 
			"chromosome": convertStateToChromosome(randomizedState),
			"score": None
		})
	return population

# Menghitung fitness score tiap populasi untuk menentukan mana kromosom terbaik dan terburuk
def evaluation(population):
	for i in range(len(population)):
		population[i]['score'] = help.score(population[i]["state"])

def selection(population):
	# Melakukakan pengacakan pada populasi
	random.shuffle(population)

	# Mendapatkan index chromosome dengan fitness score terendah dan tertinggi
	scores = []
	for i in range(len(population)):
		scores.append(population[i]['score'])

	bestChromosomeIndex = scores.index(max(scores))
	worstChromosomeIndex = scores.index(min(scores))

	# Menghapus chromosome terburuk dan menggandakan chromosome terbaik (jika ganjil)
	population.pop(worstChromosomeIndex)
	if (len(population) % 2 == 1):
		population.append(population[bestChromosomeIndex])

def crossover(population):
	pass

def mutation(population):
	pass

### Fungsi utama ###

def genetic():
	totalChromosome = int((input("Masukkan jumlah kromosom yang diinginkan: ")))
	totalIteration = int((input("Masukkan jumlah iterasi yang diinginkan: ")))
	bestResult = []

	# Melakukan pencarian kromosom terbaik di tiap iterasi
	for _ in range(totalIteration):
		# Mendapatkan kumpulan list of bidak sebanyak k buah
		population = init(totalChromosome)

		# Mendapatkan fitness score tiap chromosome
		evaluation(population)

		# Melakukan seleksi pada masing-masing chromosome berdasarkan fitness score
		selection(population)

		# Menentukan kumpulan gen yang akan dilakukan crossover
		crossover(population)

		# Melakukan mutasi pada chromosome terpilih
		mutation(population)
		
		# Mengembalikan chromosome terbaik dari hasil mutasi
		bestResult.append(findBestChromosome(population))

	# Mengembalikan chromosome terbaik dari semua hasil iterasi
	return findBestChromosome(bestResult)['state']