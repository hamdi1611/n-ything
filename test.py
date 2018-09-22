import s_annealing
import help

soal = help.getListRandomized()
soal = help.getRandomTetangga(soal)
help.printResult(soal)
print (help.totalConflictSesama(soal))
print (help.totalConflictLawan(soal))
print('\n')
answer = s_annealing.annealing(soal, 1000)
help.printResult(answer)
print (help.totalConflictSesama(answer))
print (help.totalConflictLawan(answer))
for e in answer:
    if e.isWhite():
        print (e.getChar(), e.conflict(answer, "PUTIH"), e.conflict(answer, "HITAM"))
    else:
       print (e.getChar(), e.conflict(answer, "HITAM"), e.conflict(answer, "PUTIH"))
