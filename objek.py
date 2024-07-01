namaHero = "Layla"
skill1 = "x"
skill2 = "y"
ulti = "z"

namaHero2 = "Freya"

class Musuh():
    def __init__ (self,namaMusuh):
        self.nama = namaMusuh

#template untuk membuat hero menggunakan class
class Hero():
    def __init__(self,namaHero):
        self.nama = namaHero
        self.skill1 = ""
        self.skill2 = ""
        self.ulti = ""

    def menyerang(self,musuh):
        print(self.nama,"menyerang",musuh.nama)

#membuat objek
layla = Hero("Layla")
print(layla.nama)

clint = Hero("Clint")
print(clint.nama)

#memanfaatkan fungsi input
#lebih dinamis / karena nama hero di input dari keyboard
inputNama = input("silahkan masukan nama hero:")
freya = Hero(inputNama)
print(freya.nama)

inputNamaMusuh = input("silahkan masukan nama musuh:")
alucard = Musuh(inputNamaMusuh)

freya.menyerang(alucard)
