def WriteFile():
    file = open("Star.txt", "w")
    file.write(f'Nama: {name}\nUmur: {age}\nAlamat: {address}\nEmail: {email}\nDosen Wali: {dosenwali}')
    file.close()
    
def ReadFile():
    file = open("Star.txt", "r")
    text = file.read()
    print(text)
    file.close()
    
name = str(input("Masukkan Nama mu: "))
age = int(input("Masukkan Umur mu: "))
address = str(input("Masukkan Alamat mu: "))
email = str(input("Masukkan Email mu: "))
dosenwali = str(input("Masukkan Dosen Wali mu: "))
print()
print("Berikut ini adalah data kamu!")

WriteFile()
ReadFile()                