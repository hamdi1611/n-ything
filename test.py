from hill import hill
import help

answer = hill(help.getListRandomized(), 20)
help.printResult(answer)
print (help.totalConflict(answer, "PUTIH"))
print (help.totalConflict(answer, "HITAM"))