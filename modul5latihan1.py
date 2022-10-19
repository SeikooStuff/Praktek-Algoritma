n = 0
l = 0
u = 1

while (u == 1):
    r = input("Masukkan nilai = ")
    
    h = n
    t = h + n
    l += 1
    
    if (r == "A"):
        n = 4.00
        print("Nilai = ",n)
    elif (r == "A-"):
        n = 3.75
        print("Nilai = ",n)
    elif (r == "B+"):
        n = 3.50
        print("Nilai = ",n)
    elif (r == "B"):
        n = 3.00
        print("Nilai = ",n)
    elif (r == "B-"):
        n = 2.75
        print("Nilai = ",n)
    elif (r == "C+"):
        n = 2.50
        print("Nilai = ",n)
    elif (r == "C"):
        n = 2.00
        print("Nilai = ",n)
    elif (r == "C-"):
        n = 1.75
        print("Nilai = ",n)
    elif (r == "D"):
        n = 1.50
        print("Nilai = ",n)
    elif (r == "E"):
        n = 1.25
        print("Nilai = ",n)
    else :
        u = 0
        
O = t/(l-1)
print("Rata-ratanya adalah = ", O)