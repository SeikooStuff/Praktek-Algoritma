def writeFile():
    file = open("modul9latihan2.txt", "w")
    name = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    gen = input("Masukkan Angkatan: ")
    file.write("Nama: " + name)
    file.write("\nNIM: " + nim)
    file.write("\nAngkatan: " + gen)
    file.close()
    
def readFile():
    file = open("modul9latihan2.txt", "r")
    text = file.read()
    print(text)
    file.close()
    
def addFile():
    file = open("modul9latihan2.txt", "a")
    drink = input("Masukkan Minuman Favorit: ")
    food = input("Masukkan Makanan Favorit: ")
    file.write("\nMinuman Favorit: " + drink)
    file.write("\nMakanan Favorit: " + food)
    file.close()
    
def utama():
    repeat = True
    while(repeat):
        print("=========================")
        print("Program File Handling \n=========================")
        print("1. Membuat & Menulis File")
        print("2. Membaca File")
        print("3. Menambah File")
        print("4. Keluar dari Program \n=========================")
        choose = int(input("Masukkan nomor yang dipilih: "))
        
        if(choose == 1):
            print("\n")
            writeFile()
            print("\n")
        elif(choose == 2):
            print("\n")
            readFile()
            print("\n")
        elif(choose == 3):
            print("\n")
            addFile()
            print("\n")
        elif(choose == 4):
            print("Terima kasih telah menggunakan program saya.")
            repeat = False
        else:
            print("Masukkan nomor yang ada di list!")
            print("\n")
            
utama()  