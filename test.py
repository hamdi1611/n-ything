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
#list.append(e)

list1 = help.getListRandomized()
list2 = help.getListRandomized()

help.printResult(list1)
help.printResult(list2)

print (help.totalConflict(list1, "HITAM"))
print (help.totalConflict(list1, "PUTIH"))

print (help.totalConflict(list2, "HITAM"))
print (help.totalConflict(list2, "PUTIH"))

print (help.isBetter(list1, list2))