#count number of comparisons and exchanges

def bubble_sort(arr):
    if len(arr) == 0:
        return
    
    comparisons = 0
    exchanges = 0
    for i in range(len(arr) - 1): 
        for j in range(len(arr) - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                exchanges += 1
        comparisons += 1
    return (comparisons, exchanges)

print(bubble_sort([4, 10, 9, 1, 5, 12, 7]))