def switch(array, k, l):
    temp = array[k]
    array[k] = array[l]
    array[l] = temp
    
def bubbleSort(array, n):
    for k in range(n-1):
        if array[k] > array[k + 1]:
            switch(array, k, k + 1)
    if n - 1 > 1:
        bubbleSort(array, n - 1)
        
array = [51, 26, -8, 2, -12, 15, 57, -24, 86, -15]
bubbleSort(array, len(array))
print("List yang sudah disorting: ")
print(array)