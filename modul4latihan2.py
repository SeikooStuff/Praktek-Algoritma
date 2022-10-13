import calendar

print("Menentukan jumlah hari di salah satu bulan")

ulang = "y"
while ulang == "y" or ulang == "n":
    year = int(input("Masukkan Tahun = "))
    month = int(input("Masukkan Bulan = "))
    print("Ada", (calendar.monthrange(year, month)[1]), "Hari di bulan ke ", month)
    ulang = input("ketik 'y' jika ingin lanjut, ketik 'n' jika ingin berhenti ")
    if ulang == 'n':
        break