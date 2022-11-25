def BinarySearch(array, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if array[mid] == k:
            return mid
        elif array[mid] > k:
            return BinarySearch(array, k, low, mid-1)
        else:
            return BinarySearch(array, k, mid+1, high)
    else: 
        return -1
    
array = [11, 13, 9, 26, 22, 96, 19, 27, 66, 36]
k = int(input("Masukan angka yang dicari: "))
array.sort()

result = BinarySearch(array, k, 0, len(array)-1) + 1
print(array)

if k not in array:
    print("Elemen tidak ditemukan pada list")
if k in array:
    print("Elemen ditemukan pada posisi ke-" + str(result))