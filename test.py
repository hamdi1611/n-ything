from Bidak import Bidak
import help

a = Bidak('Q', 1, 2)
b = Bidak('K', 2, 0)
c = Bidak('K', 2, 1)
d = Bidak('r', 2, 2)
e = Bidak('R', 3, 2)

list = []
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)

print (help.totalConflict(list, "HITAM"))
print (help.totalConflict(list, "PUTIH"))
help.printResult(list)