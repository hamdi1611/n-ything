#main program
<<<<<<< HEAD

from hill import hill
import help

# menampilkan algoritma yg akan digunakan
print ("Daftar algoritma\n")
print ("1 : Hill Climbing\n")
print ("2 : Simulated Annealing\n")
print ("3 : Genetic Algoritthm\n")

# menerima masukan algoritma yg akan digunakan 
nama = input("Algoritma yang akan digunakan : ")

if nama ==1:
	soal = help.getListRandomized()
	help.printResult(soal)
	print (help.totalConflictSesama(soal))
	print (help.totalConflictLawan(soal))
	print('\n')
	answer = hill(soal, 1000)
	help.printResult(answer)
	print (help.totalConflictSesama(answer))
	print (help.totalConflictLawan(answer))
elif nama == 2:
	

elif nama == 3:
	
=======
from genetic import genetic
import help

genetic(5)
>>>>>>> da6e5b96ce0723d2cbc3c7010333847e972760ee
