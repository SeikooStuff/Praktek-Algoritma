def value():
    print()
    print("Program pemangkatan negatif dan positif, Tekan enter untuk berhenti")
    n = input("Masukkan Angka: ")
    
    if n == '':
        print("Program selesai")
        return 0
    
    p = input("Masukkan Pangkatnya: ")
    result = int(n) ** int(p)
    print("Hasilnya adalah: ", result)
    value()
    
value()