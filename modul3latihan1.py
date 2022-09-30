print("Jenis - Jenis Segitiga")

a = float(input("Masukkan Sisi Tegak Segitiga = "))
b = float(input("Masukkan Sisi Bawah Segitiga = "))
c = float(input("Masukkan Sisi Miring Segitiga = "))

if a == b == c :
    print("Segitiga Sama Sisi")
elif c == (a**2 + b**2)**0.5 :
    print("Segitiga Siku - Siku")
else :
    print("Segitiga Sembarang")