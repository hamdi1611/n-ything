class Bidak:
    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y
    def isWhite(self):
        return (self.char >='A' and self.char <= 'Z')
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
    def isSameCoorExist(self, list_of_object):
        for e in list_of_object:
            if e.x==self.x and e.y==self.y:
                return True
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

        # Menghitung jumlah konflik jika bidak adalah rock (benteng)
        elif self.char=='R' or self.char=='r':
            # list of info bidak lain yang konflik dengan bidak tsb. (atas, bawah, kiri, kanan)
            chars_conflict = [[' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0]]
            
            for e in list_of_object:
                # kondisi konflik di atas
                if e.x==self.x and e.y<self.y:
                    if chars_conflict[0][0]==' ' or chars_conflict[0][2] > e.y:
                        chars_conflict[0][0] = e.char
                        chars_conflict[0][1] = e.x
                        chars_conflict[0][2] = e.y
                
                # kondisi konflik di bawah
                elif e.x==self.x and e.y>self.y:
                    if chars_conflict[1][0]==' ' or chars_conflict[0][2] < e.y:
                        chars_conflict[1][0] = e.char
                        chars_conflict[1][1] = e.x
                        chars_conflict[1][2] = e.y

                # kondisi konflik di kiri
                elif e.x<self.x and e.y==self.y:
                    if chars_conflict[2][0]==' ' or chars_conflict[0][1] > e.x:
                        chars_conflict[2][0] = e.char
                        chars_conflict[2][1] = e.x
                        chars_conflict[2][2] = e.y

                # kondisi konflik di kanan
                elif e.x>self.x and e.y==self.y:
                    if chars_conflict[3][0]==' ' or chars_conflict[0][1] < e.x:
                        chars_conflict[3][0] = e.char
                        chars_conflict[3][1] = e.x
                        chars_conflict[3][2] = e.y
            temp = [1 for e in chars_conflict if e[0] >= min and e[0] <= max]
            N = sum(temp)

        # Menghitung jumlah konflik jika bidak adalah bishop (gajah)
        elif self.char=='B' or self.char=='b':
            for e in list_of_object:
                m = (self.y - e.y)/(self.x - e.x)
                if Int(m)==1 or Int(m)==-1:
                    N +=1

        # Menghitung jumlah konflik jika bidak adalah queen (ratu)
        elif self.char=='Q' or self.char=='q':
            for e in list_of_object:
                if e.x==self.x and e.y<self.y:
                    N +=1
                elif e.x==self.x and e.y>self.y:
                    N +=1
                elif e.x<self.x and e.y==self.y:
                    N +=1
                elif e.x>self.x and e.y==self.y:
                    N +=1
                m = (self.y - e.y)/(self.x - e.x)
                if Int(m)==1 or Int(m)==-1:
                    N +=1

        return N