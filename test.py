from hill import hill
from Bidak import Bidak
import help

x = Bidak('k', 0, 0)
soal = help.getListRandomized()
help.printResult(soal)
print (help.totalConflict(soal, "PUTIH"))
print (help.totalConflict(soal, "HITAM"))
print('\n')
help.printResult(x.otherPositions(soal))
print('\n')
answer = hill(soal, 20)
help.printResult(answer)
print (help.totalConflict(answer, "PUTIH"))
print (help.totalConflict(answer, "HITAM"))