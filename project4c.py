#insertion sort for strings

def insertion_sort(arr):
    if len(arr) == 0:
        return
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(["zebra", "alla", "skd", "ujsd", "akdm"]))