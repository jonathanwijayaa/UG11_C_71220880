print("Pemeriksa Kelipatan 9")
b = int(input("Masukkan Kelipatan 9 yang ingin diperiksa:"))
sisa = b % 9
def kelipatan_sembilan(b):
    h = (b/9)
    return h
if kelipatan_sembilan(b) == 9 :
    print("Benar")
else:
    print("Salah")
    print( sisa )
