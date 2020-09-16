#binary search

from math import floor

def bin_except(arr, num):
    if len(arr) == 0:
        return None
    
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        mid = floor((first + last) / 2)
        if num == arr[mid]:
            return mid
        elif arr[mid] > num:
            last = mid - 1
        else:
            first = mid + 1
    raise TargetNotFound

class TargetNotFound(Exception):
    pass

def main():
    try:
        result = bin_except([2,3,16,22,29], 29)
    except:
        print("Target not found")
    else:
        print("Target found at: ", result)

if __name__=="__main()__": main()
main()