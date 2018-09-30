# Fungsi-fungsi bantuan untuk N-ything problem

from Bidak import Bidak
import random

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
    return (totalConflictLawan(list_of_object) - 1.5*totalConflictSesama(list_of_object))

# Mengembalikan total conflict sesama dan lawan dengan format [sesama, lawan]
# berdasarkan warna yang ingin dihitung konfliknya ("PUTIH" atau "HITAM")
def totalConflict(list_of_object):
    total = [0, 0] # [sesama, lawan]

    for e in list_of_object:
        if e.isWhite():
            total[0] += e.conflict(list_of_object, "PUTIH")
            total[1] += e.conflict(list_of_object, "HITAM")
        else:
            total[0] += e.conflict(list_of_object, "HITAM")
            total[1] += e.conflict(list_of_object, "PUTIH")

    return total

def totalConflictSesama(list_of_object):
    return totalConflict(list_of_object)[0]

def totalConflictLawan(list_of_object):
    return totalConflict(list_of_object)[1]

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

# Mengembalikan sebuah list_of_object baru yang merupakan tetangga list input secara random
def getRandomTetangga(list_of_object):
    i = random.randint(0, len(list_of_object)-1)
    
    new_list = list(list_of_object)
    temp = new_list.pop(i)
    e = Bidak(temp.getChar(), temp.getX(), temp.getY())

    while e.isSameCoorExist(list_of_object):
        e.setCoor(random.randint(0,7), random.randint(0,7))
    new_list.append(e)
    return new_list
