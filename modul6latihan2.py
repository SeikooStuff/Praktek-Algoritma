print("Program menentukan jumlah hari dalam bulan tertentu!")

F = False

year = ''

def Kabisat(year):
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        print("29 Hari dalam Sebulan")
    else:
        print("28 Hari dalam Sebulan")
        
def NonKabisat(month):
    if month in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        if month in [4, 6, 9, 11]:
            print("30 Hari dalam Sebulan")
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            print("31 Hari dalam Sebulan")
        elif month == 2:
            year = int(input("Masukkan Tahun = "))
            Kabisat(year)
    else:
        print("Error")

while (not F):
    print("Masukkan 0 untuk Berhenti")
    month = int(input("Masukkan Bulan (1 - 12) = "))
    if month == 0:
        F = True
    else:
        NonKabisat(month)