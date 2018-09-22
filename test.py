from hill import hill
import help

soal = help.getListRandomized()
help.printResult(soal)
print (help.totalConflictSesama(soal))
print (help.totalConflictLawan(soal))
print('\n')
answer = hill(soal, 1000)
help.printResult(answer)
print (help.totalConflictSesama(answer))
print (help.totalConflictLawan(answer))
#for e in answer:
#    if e.isWhite():
#        print (e.conflict(answer, "PUTIH"), e.conflict(answer, "HITAM"))
#   else:
#       print (e.conflict(answer, "HITAM"), e.conflict(answer, "PUTIH"))
