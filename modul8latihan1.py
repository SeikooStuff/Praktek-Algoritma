def summation(n = 0, summ = 0, i = 1):
    if (summ <- 0):
        return 0
    else:
        n = int(input("Masukkan bilangan ke-" + str(i) + " : "))
        if (summ == 1):
            return n 
        else:
            i += 1
            return n + summation(n, summ-1, i)
        
angka = int(input("Masukkan Angka: "))
value = summation(summ = angka)
print("Hasil dari penjumlahan tersebut adalah : " + str(value))