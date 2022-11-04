def is_prima():
    x = int(input("Masukkan angka = "))
    for i in range(2, x):
        if x % i == 0:
            return x, "bukanlah bilangan prima"
        
    return x, "adalah bilangan prima"

p = is_prima()
print(p)