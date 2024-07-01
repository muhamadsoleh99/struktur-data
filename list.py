#Studi Kasus Item di Mobile Legend

#1 Hero ada 6 slot Item
#1 Item bisa terdiri dari beberapa item kecil
#Item memiliki hierarki
#Membeli Item menggunakan gold
#Untuk mendapatkan gold -> farming

# Hero: Leyla
# Item: Swift Boots , Haas’s Claws, Scarlet Phantom , 
# Berserker’s Fury, Malefic Roar , Blade of Despair 
# Swift Boots: Speed Boots , Knife

import random

Hero = "Layla"
Gold = 0
Item = []
print(Hero)
print(Item)

def farming():
    global Gold
    HPmonster = random.randint(300, 500)
    print("Monster dengan HP" , HPmonster)
    DamageLayla = int(input("Masukan Damage Layla:"))
    if DamageLayla > HPmonster:
        Gold += HPmonster
    return Gold

itemKecil = [["Speed Boots" , 250],["Knife",280]]
#Layla ingin membeli item kecil
print(itemKecil)

def beliItem():
    global Gold
    if Gold > hargaItem :
        #Layla sudah berhasil membeli item pertama
        Item.append(itemKecil[itemDibeli][0])
        print(Item)
        Gold -= itemKecil[itemDibeli][1]
        print(Gold)
    else:
        print("Layla tidak memiliki cukup Gold, silahkan farming")
        Gold = farming()
        print(Gold)

while True:
    itemDibeli = int(input("Silahkan masukan index item yang akan dibeli: "))

    #Cek dulu apakah layla memiliki gold yang cukup
    hargaItem = itemKecil[itemDibeli][1]
    if Gold < hargaItem:
        farming()
    else:
        beliItem()