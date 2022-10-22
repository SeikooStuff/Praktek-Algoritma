def average(n = "0", t = 0, l = 0):
    while (n != ""):
        n = input("Masukkan Nilai: ")
        l += 1
        if(n == ""):
            if(l == 1):
                return 0
            else:
                return t/(l - 1)
        elif (n == "A"):
            print("Nilai = 4")
            t += 4
        elif (n == "A-"):
            print("Nilai = 3.75")
            t += 3.75
        elif (n == "B+"):
            print("Nilai = 3.25")
            t += 3.25
        elif (n == "B"):
            print("Nilai = 3")
            t += 3
        elif (n == "B-"):
            print("Nilai = 2.75")
            t += 2.75
        elif (n == "C+"):
            print("Nilai = 2.5")
            t += 2.5
        elif (n == "C"):
            print("Nilai = 2")
            t += 2
        elif (n == "C-"):
            print("Nilai = 1.75")
            t += 1.75
        elif (n == "D"):
            print("Nilai = 1.5")
            t += 1.5
        elif (n == "E"):
            print("Nilai = 1.25")
            t += 1.25
        else:
            n = 0
            
O = average()
print("Nilai Rata-Ratanya Adalah %0.2f " % O)
            
