rows = int(input("Masukkan jumlah maksimal = "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print(i, end=' ')
    print("\r")
