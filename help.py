# Fungsi-fungsi bantuan untuk N-ything problem

from Bidak import Bidak
import random

# Mengambil informasi dari file txt
# Mengembalikan list of object Bidak {Semua Bidak dalam posisi (0, 0)}
def getList():
    f = open('input.txt', 'r')
    list_of_object = []
    for line in f:
        info = line.split()
        for i in range(0, int(info[2])):
            char = info[1][0]
            if info[0][0]=='B':
                char = char.lower()
            list_of_object.append(Bidak(char, 0, 0))
    return list_of_object

# Mengambil informasi dari file txt
# Mengembalikan list of object Bidak {Semua Bidak dalam posisi RANDOM UNIK}
def getListRandomized():
    f = open('input.txt', 'r')
    list_of_object = []
    for line in f:
        info = line.split()
        for i in range(0, int(info[2])):
            char = info[1][0]
            if info[0][0]=='B':
                char = char.lower()
            
            # add objek bidak dengan posisi unik ke dalam list
            obj = Bidak(char, random.randint(0,7), random.randint(0,7))
            while obj.isSameCoorExist(list_of_object):
                obj = Bidak(char, random.randint(0,7), random.randint(0,7))
            
            list_of_object.append(obj)
    return list_of_object

def score(list_of_object):
    return (totalConflict(list_of_object, "HITAM") - totalConflict(list_of_object, "PUTIH"))

# list1 dan list2 adalah list of object Bidak
# Memeriksa apakah score list1 lebih besar dari score list2
def isBetter(list1, list2):
    return (score(list1) > score(list2))

# Mengembalikan jumlah total konflik bidak-bidak berwarna PUTIH dengan bidak lain
# berdasarkan warna yang ingin dihitung konfliknya ("PUTIH" atau "HITAM")
def totalConflict(list_of_object, color):
    total = 0
    for e in list_of_object:
        if e.isWhite():
            total += e.conflict(list_of_object, color)
    return total

# Mengembalikan character dari Object Bidak yang memilki koordinat (x,y)
# jika tidak ada, mengembalikan '.'
def charCoor(x, y, list_of_object):
    for e in list_of_object:
        if e.getX()==x and e.getY()==y:
            return e.getChar()
    return '.'

# Menampilkan seluruh objek bidak dalam matriks 8 x 8
def printResult(list_of_object):
    for j in range (0, 8):
        for i in range (0, 8):
            print (charCoor(i, j, list_of_object), end=" ")
        print ('\n')