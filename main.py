from hill import hill
from s_annealing import annealing
from genetic import genetic
import help

# menampilkan algoritma yg akan digunakan
print ("Daftar algoritma:")
print ("1 : Hill Climbing")
print ("2 : Simulated Annealing")
print ("3 : Genetic Algoritthm")

# menerima masukan algoritma yg akan digunakan 
nama = int(input("Algoritma yang akan digunakan : "))

print("\nSOAL:")
soal = help.getListRandomized()
help.printResult(soal)
print (help.totalConflictSesama(soal), help.totalConflictLawan(soal))

print("\nJAWABAN:")

answer = []
if nama == 1:
	answer = hill(soal, 1000)
elif nama == 2:
	answer = annealing(soal, 10000, 100, 5)
elif nama == 3:
	answer = genetic(4)

help.printResult(answer)

result = []
result = help.totalConflict(answer)
print (result[0], result[1])
