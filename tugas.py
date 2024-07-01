class Hero:
    def __init__(self,nama,attack):
        self.nama = nama
        self.attack = attack
        self.item = [] #list kosong

    def menyerang(self,lord):
        totalDamage = self.attack + self.item.damage
        lord.hp -= totalDamage
        print(self.nama, "menyerang" , lord.nama, "dengan senjata" ,self.item.nama, "sebesar", totalDamage , lord.hp , "sekarang" , lord.hp)

    def pakaiSenjata(self,item):
        if self.item.nama == 0:
            print(self.nama, "berhasil memakai", self.item.nama,"!")
        else:
            print(self.nama, "sudah memiliki senjata.")

class Lord:
    def __init__(self,nama,hp):
        self.nama = nama
        self.hp = hp

class Item:
    def __init__(self,nama,damage):
        self.nama = nama
        self.damage = damage

ListHero = []
masukan = input("Masukan jumlah hero :") #string
for i in range(int(masukan)):
    print("<Hero",i+1,">")
    inputHero = input()
    #print(inputHero)
    pisahData = inputHero.split("%")
    #print(pisahData[0],pisahData[1])
    hero = Hero(pisahData[0],pisahData[1])
    ListHero.append(hero)
print(ListHero)

print(ListHero[0].nama)

ListItem = [] #menampung seluruh item hero
masukan = int(input("Masukan jumlah item :"))
for i in range(masukan):
    print("<Item", i+1,">")
    inputItem = input()
    pisahData = inputItem.split(";")
    #objek item
    item = Item(pisahData[0],pisahData[1])
    ListItem.append(item)

print(ListItem[0].nama)

print("!! Lord Respawn !!")
print("<Lord>")

inputLord = input()
pisahData = inputLord.split("*")
lord = Lord(pisahData[0],pisahData[1])

print(lord.hp)

#sintaks untuk menambahkan item WON pada hero Raj Alam
ListHero[0].item.append(ListItem[0])
print(ListHero[0].item[0].nama) #WON

print(len(ListHero[0].item)) #1
print(len(ListHero[1].item)) #0

