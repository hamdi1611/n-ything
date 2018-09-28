from Bidak import Bidak
import help, math, random

# Algoritma Simulated-Annealing
# Masukan : list_of_object		Jenis dan koordinat bidak-bidak yang ada di papan
#			n					Banyaknya iterasi pencarian
#			temperature			Suhu awal sebelum pencarian
#			temperature_param	Kecepatan penurunan suhu
def annealing(list_of_object, n, temperature, temperature_param):
	# Membuat list untuk mencatat state sekarang
	current_list = list(list_of_object)
	# Membuat list untuk mencatat state terbaik
	best_list = list(list_of_object)
	# Evaluasi nilai heuristik state sekarang
	current_e = help.score(current_list)
	# Mencatat nilai evaluasi yang terbaik
	best_e = current_e
	# Mencatat suhu sekarang
	current_temperature = temperature
	# Iterasi ke-i
	i = 0
	while(i < n):
		# State yang akan dibandingkan didapat secara random dari moveset
		next_list = list(help.getRandomTetangga(list_of_object))
		# Evaluasi nilai heuristik state yang terpilih
		next_e = help.score(next_list)
		# Bandingkan nilai evaluasinya, jika lebih baik atau sama dengan state sekarang maka
		if(next_e >= current_e):
			# Jika lebih baik dari nilai evaluasi terbaik selama iterasi sebelumnya
			if(next_e > best_e):
				# Catat sebagai state terbaik
				best_list = list(next_list)
				best_e = next_e
			# Catat sebagai state sekarang
			current_list = list(next_list)
			current_e = next_e
		# Jika lebih buruk maka
		else:
			# Bangkitkan sebuah nilai acak, dan hitung probabilitas menggunakan fungsi Boltzman
			if(boltzman(current_e, next_e, current_temperature) >= random.random()):
				# Catat sebagai state sekarang
				current_list = list(next_list)
				current_e = next_e
		# Ubah suhu sekarang menggunakan schedule yang sudah ditentukan
		current_temperature = temperature_schedule(temperature, i, temperature_param)
		i += 1
	# Selesai iterasi
	# Kembalikan state yang memiliki nilai evaluasi terbaik
	if(current_e > best_e):
		return current_list
	else:
		return best_list

# Fungsi penentu probabilitas
def boltzman(e, ei, T):
	prob = math.exp((ei - e) / T)
	return prob

# Fungsi penurunan suhu
def temperature_schedule(T, k, param):
	return T / (1 + param * math.log(1 + k, 10))
