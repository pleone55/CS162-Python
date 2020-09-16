
def is_decreasing(arr):
    if len(arr) <= 1 or (len(arr) == 2 and arr[0] >= arr[1]):
        return True
    else:
        if arr[0] >= arr[1]:
            return is_decreasing(arr[1::])
        else:
            return False

def main():
    a_list = [5, 4, 3, 2, 1]
    b_list = [1, 2]
    c_list = [6, 5, 4, 4, 3, 2, 2, 1]
    
    result = is_decreasing(a_list)
    result2 = is_decreasing(b_list)
    result3 = is_decreasing(c_list)
    
    print("Is a_list decreasing? ", result)
    print("Is b_list decreasing? ", result2)
    print("Is c_list decreasing? ", result3)

if __name__=="__main()__": main()
main()