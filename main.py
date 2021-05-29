__author__="kvda"

class myClass():
    def myFunc(self):
        print("Program determinan Matriks")
        print("---")
        barisInp = input("Masukkan jumlah baris : ")
        kolomInp = input("Masukkan jumlah kolom : ")
        print("")

        matriks1 = []
        matriks2 = []

        offset = 0
        
        print("Masukkan matriks anda")
        print("---")
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                Amatriks = input("Masukkan angka untuk baris {0} kolom {1} : ".format(offset+1,offset2+1))
                matriks1.append(Amatriks)
                offset2+=1
            offset+=1
        print("---")
        print("kvda-creator")
        print("---")
        offset = 0
        offsetMatriks = 0
        while offset<int(barisInp):
            offset2 = 0
            while offset2<int(kolomInp):
                print(int(matriks1[offsetMatriks]),end=" ")
                offsetMatriks+=1
                offset2+=1
            print(" ")
            offset+=1
        print("---")
        
        print("Determinan matriks anda : ", end=" ")
        if(barisInp=="2"):
            ad = int(matriks1[0])*int(matriks1[3])
            bc = int(matriks1[1])*int(matriks1[2])
            determinan = int(ad)-int(bc)
            print(determinan)
        elif(barisInp=="3"):
            aei = int(matriks1[0])*int(matriks1[4])*int(matriks1[8])
            bfg = int(matriks1[1])*int(matriks1[5])*int(matriks1[6])
            cdh = int(matriks1[2])*int(matriks1[3])*int(matriks1[7])
            side1 = int(aei)+int(bfg)+int(cdh)
            gec = int(matriks1[6])*int(matriks1[4])*int(matriks1[2])
            afh = int(matriks1[7])*int(matriks1[5])*int(matriks1[0])
            bdi = int(matriks1[8])*int(matriks1[3])*int(matriks1[1])
            side2 = int(gec)-int(afh)-int(bdi)
            print(int(side1)," - ",int(side2)," = ", end=" ")
            print(int(side1)-int(side2))
         
if __name__ == '__main__':
    myClass().myFunc()