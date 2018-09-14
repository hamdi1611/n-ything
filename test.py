from Bidak import Bidak

a = Bidak('Q', 1, 2)
b = Bidak('K', 1, 1)
c = Bidak('R', 1, 3)
d = Bidak('A', 3, 4)
e = Bidak('B', 0, 1)

list = []
list.append(b)
list.append(c)
list.append(d)
list.append(e)

print (a.conflict(list, "PUTIH"))