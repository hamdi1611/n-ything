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
	if (len(population) % 2 == 1):
		population.append(population[bestChromosomeIndex])
	population.pop(worstChromosomeIndex)	

def crossover(population):
	# Melakukan pengulangan pada tiap pasangan
	for i in range(0, len(population) - 1, 2):
		randomPoint = random.randint(0, len(population[i]['state']))
		firstStateEndSlice = population[i]['state'][randomPoint:]
		secondStateEndSlice = population[i+1]['state'][:randomPoint]

		# Melakukan swap pada tiap pasangan
		firstStateEndSlice, secondStateEndSlice = secondStateEndSlice, firstStateEndSlice

def mutation(population):
	# Membangkitkan secara acak koordinat baru
	new_x = random.randint(1, 8)
	new_y = random.randint(1, 8)
	mutated = False

	# Melakukan pengulangan hingga salah satu kromosom termutasi
	while not mutated:
		# Memilih kromosom yang akan dimutasi secara acak
		selectedChromosomeIndex = random.randint(0, len(population) - 1)
		selectedChromosome = population[selectedChromosomeIndex]
		selectedStateIndex = random.randint(0, len(selectedChromosome['state']) - 1)
		selectedState = selectedChromosome['state'][selectedStateIndex]
		
		# Mengecek kromosom lain yang memiliki koordinat sama
		sameCoorExist = 0
		for _ in range(len(population[selectedChromosomeIndex]['state'])):
			restPopulationState = list(population[selectedChromosomeIndex]['state'])
			restPopulationState.pop(selectedStateIndex)
			if (selectedState.isSameCoorExist(restPopulationState)):
				sameCoorExist = sameCoorExist + 1

		# Hanya dimutasi jika tidak ada koordinat yang sama dengan yang lain
		if (sameCoorExist == 0):
			selectedState.setX(new_x)
			selectedState.setY(new_y)
			selectedChromosome['chromosome'] = convertStateToChromosome(selectedChromosome['state'])
			mutated = True

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