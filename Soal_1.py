#Rumus 1
def jumlah(bilper,bilked):
    jumlah = (bilper+bilked)
    return jumlah
def kurang(bilper,bilked):
    kurang = (bilper-bilked)
    return kurang
def kali(bilper,bilked):
    kali = (bilper*bilked)
    return kali
def bagi(bilper,bilked):
    bagi = (bilper/bilked)
    return bagi
print("=========================")
print("Operasi Matematika")
print("   1. Jumlah     [+]")
print("   2. Kurang     [-]")
print("   3. Kali       [*]")
print("   4. Bagi       [/]")
print("=========================")
m=int(input("Pilih operasi 1/2/3/4):"))
print("=========================")
#Rumus 2
if m == 1:
    bilper=int(input("Masukkan bilangan pertama:"))
    bilked=int(input("Masukkan bilangan kedua:"))
    print("Hasil operasi dari", bilper , "+" , bilked, "=" , jumlah(bilper,bilked))
elif m == 2:
    bilper=int(input("Masukkan bilangan pertama:"))
    bilked=int(input("Masukkan bilangan kedua:"))
    print("Hasil operasi dari", bilper , "-" , bilked, "=" , kurang(bilper,bilked))
elif m == 3:
    bilper=int(input("Masukkan bilangan pertama:"))
    bilked=int(input("Masukkan bilangan kedua:"))
    print("Hasil operasi dari", bilper , "*" , bilked, "=" , kali(bilper,bilked))
elif m == 4:
    bilper=int(input("Masukkan bilangan pertama:"))
    bilked=int(input("Masukkan bilangan kedua:"))
    print("Hasil operasi dari", bilper , "/" , bilked, "=" , bagi(bilper,bilked))

        
        
