import math

l = float(input("Masukkan Nilai L = "))
m = float(input("Masukkan Nilai M = "))
n = float(input("Masukkan Nilai N = "))

if (l == 0):
    print("Bukan Merupakan Persamaan Kuadrat")
else:
    O = pow(m, 2)-(4*l*n)
    if (O > 0):
        x1 = ((-m)+math.sqrt(O))/(2*l)
        x2 = ((-m)-math.sqrt(O))/(2*l)
        print("Persamaan Kuadrat " + str(l) + " x² + " + str(m) + " x + " + str(n))
        print("Determinannya = " + str(O))
        print("Memiliki Akar Berbeda")
        print("Akar x1 = " + str(x1))
        print("Akar x2 = " + str(x2))
    elif (O == 0):
        x1 = (-m)/(2*l)
        x2 = x1
        print("Persamaan Kuadrat " + str(l) + " x² + (" + str(m) + ") x + " + str(n))
        print("Determinannya = " + str(O))
        print("Merupakan Akar Kembar")
        print("Akar = " + str(x2))
    elif (O < 0):
        print("Persamaan Kuadrat " + str(l) + " x² + " + str(m) + " x + " + str(n))
        print("Determinannya = " + str(O))
        print("Merupakan Akar Imaginer")
        print("Akar x1 = -" + str(m) + " + √" + str(O) + "/2*" + str(l))
        print("Akar x2 = -" + str(m) + " - √" + str(O) + "/2*" + str(l))
    else:
        print("Error, Tolong Masukkan Nilai yang Valid!")