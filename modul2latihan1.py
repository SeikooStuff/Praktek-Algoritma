import math
a = float(input("Masukkan nilai a = "))
b = float(input("Maukkan nilai b = "))

jumlah = a+b
selisih = abs(b-a)
kali = a*b
sisabagi = a%b
pembagian = a/b
pemangkatan = a**b
math.log10(a)

print("Jumlah a dan b = ", jumlah)
print("Selisih antara b dengan a = ", selisih)
print("Hasil kali a dan b = ", kali)
print("Sisa pembagian a dengan b = ", sisabagi)
print("Pembagian a dengan b = ", pembagian)
print("a pangkat b = ", pemangkatan)
print("Hasil logaritma = ", math.log10(a))