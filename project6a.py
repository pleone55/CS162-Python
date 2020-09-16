from math import floor

def array_max(arr):
    first = 0
    last = len(arr) - 1
    
    return arr_max_helper(arr, first, last)

def arr_max_helper(arr, first, last):
    if first == last:
        largest_val = arr[first]
        return largest_val
    else:
        middle = int(floor(first + (last - first) / 2))
        
        left = arr_max_helper(arr, first, middle)
        
        right = arr_max_helper(arr, middle + 1, last)
        
        largest_val = max(left, right)
    
    return largest_val

def main():
    arr = [2,3,1,4,6,0,19,22,20]
    print("Max: ", array_max(arr))

if __name__=="__main__()": main()
main()