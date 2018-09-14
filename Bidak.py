class Bidak:
    # Inisiasi pembuatan objek bidak
    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y

    # Memeriksa apakah bidak merupakan warna putih atau tidak
    def isWhite(self):
        return (self.char >='A' and self.char <= 'Z')

    # Mengembalikan list of object-object yang merupakan adjacent-nya 
    def tetangga(self):
        tetangga = []
        if self.x > 0:
            tetangga.append(Bidak(self.char, self.x-1, self.y))
        if self.x < 7:
            tetangga.append(Bidak(self.char, self.x+1, self.y))
        if self.y > 0:
            tetangga.append(Bidak(self.char, self.x, self.y-1))
        if self.y < 7:
            tetangga.append(Bidak(self.char, self.x, self.y+1))
        return tetangga

    # Memeriksa apakah ada objek(bidak) dalam list_of_object yang memiliki koordinat yang sama dengan bidak
    def isSameCoorExist(self, list_of_object):
        for e in list_of_object:
            if e.x==self.x and e.y==self.y:
                return True
        return False
    
    # Menghitung jumlah konflik bidak dengan bidak lain berdasarkan warna putih/hitam
    def conflict(self, list_of_object, color):
        if color=="PUTIH":
            min = 'A'
            max = 'Z'
        else:
            min = 'a'
            max = 'z'
        N = 0

        # Menghitung jumlah konflik jika bidak adalah knight (kuda)
        if self.char=='K' or self.char=='k':
            for e in list_of_object:
                if e.char >= min and e.char <= max:
                    if e.x==self.x-1 and e.y==self.y-2:
                        N +=1
                    elif e.x==self.x-2 and e.y==self.y-1:
                        N +=1
                    elif e.x==self.x-2 and e.y==self.y+1:
                        N +=1
                    elif e.x==self.x-1 and e.y==self.y+2:
                        N +=1
                    elif e.x==self.x+2 and e.y==self.y+1:
                        N +=1
                    elif e.x==self.x+1 and e.y==self.y+2:
                        N +=1
                    elif e.x==self.x+1 and e.y==self.y-2:
                        N +=1
                    elif e.x==self.x+2 and e.y==self.y-1:
                        N +=1
        else:
            # Menghitung jumlah konflik jika bidak adalah rock (benteng) atau queen(ratu)
            if self.char=='R' or self.char=='r' or self.char=='Q' or self.char=='q':
                # list of info bidak lain yang konflik dengan bidak tsb. (atas, bawah, kiri, kanan)
                chars_conflict = [[' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0]]
                
                for e in list_of_object:
                    # kondisi konflik di atas bidak
                    if e.x==self.x and e.y<self.y:
                        if chars_conflict[0][0]==' ' or chars_conflict[0][2] > e.y:
                            chars_conflict[0][0] = e.char
                            chars_conflict[0][1] = e.x
                            chars_conflict[0][2] = e.y
                    
                    # kondisi konflik di bawah bidak
                    elif e.x==self.x and e.y>self.y:
                        if chars_conflict[1][0]==' ' or chars_conflict[0][2] < e.y:
                            chars_conflict[1][0] = e.char
                            chars_conflict[1][1] = e.x
                            chars_conflict[1][2] = e.y

                    # kondisi konflik di kiri bidak
                    elif e.x<self.x and e.y==self.y:
                        if chars_conflict[2][0]==' ' or chars_conflict[0][1] > e.x:
                            chars_conflict[2][0] = e.char
                            chars_conflict[2][1] = e.x
                            chars_conflict[2][2] = e.y

                    # kondisi konflik di kanan bidak
                    elif e.x>self.x and e.y==self.y:
                        if chars_conflict[3][0]==' ' or chars_conflict[0][1] < e.x:
                            chars_conflict[3][0] = e.char
                            chars_conflict[3][1] = e.x
                            chars_conflict[3][2] = e.y
                temp = [1 for e in chars_conflict if e[0] >= min and e[0] <= max]
                N += sum(temp)
                
            # Menghitung jumlah konflik jika bidak adalah bishop (gajah) atau queen(ratu)
            if self.char=='B' or self.char=='b' or self.char=='Q' or self.char=='q':
                # list of info bidak lain yang konflik dengan bidak tsb. (atas-kiri, atas-kanan, bawah-kiri, bawah-kanan)
                chars_conflict2 = [[' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0]]

                for e in list_of_object:
                    # nilai gradient harus 1 atau -1 (menyatakan posisi bidak relatif serong)
                    if self.x - e.x == 0:
                        m = 0
                    else:
                        m = (self.y - e.y)/(self.x - e.x)
                    
                    if int(m)==1 or int(m)==-1:
                        # kondisi konflik di atas-kiri bidak
                        if e.y<self.y and e.x<self.x:
                            if chars_conflict2[0][0]==' ' or chars_conflict2[0][2] > e.y:
                                chars_conflict2[0][0] = e.char
                                chars_conflict2[0][1] = e.x
                                chars_conflict2[0][2] = e.y

                        # kondisi konflik di atas-kanan bidak
                        elif e.y<self.y and e.x>self.x:
                            if chars_conflict2[1][0]==' ' or chars_conflict2[0][2] > e.y:
                                chars_conflict2[1][0] = e.char
                                chars_conflict2[1][1] = e.x
                                chars_conflict2[1][2] = e.y

                        # kondisi konflik di bawah-kiri bidak
                        elif e.y>self.y and e.x<self.x:
                            if chars_conflict2[2][0]==' ' or chars_conflict2[0][2] < e.y:
                                chars_conflict2[2][0] = e.char
                                chars_conflict2[2][1] = e.x
                                chars_conflict2[2][2] = e.y

                        # kondisi konflik di bawah-kanan bidak
                        elif e.y>self.y and e.x>self.x:
                            if chars_conflict2[3][0]==' ' or chars_conflict2[0][2] < e.y:
                                chars_conflict2[3][0] = e.char
                                chars_conflict2[3][1] = e.x
                                chars_conflict2[3][2] = e.y

                temp = [1 for e in chars_conflict2 if e[0] >= min and e[0] <= max]
                N += sum(temp)
                
        # Mengembalikan jumlah konflik
        return N