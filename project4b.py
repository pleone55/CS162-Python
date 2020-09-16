class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def volume(self):
        return self.length * self.height * self.width

def box_sort(arr):
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

def main():
    
    box1 = Box(13.4, 12, 14.45)
    box1_vol = round(box1.volume(), 2)

    box2 = Box(12, 2.34, 9)
    box2_vol = round(box2.volume(), 2)

    box3 = Box(4, 15.9, 11.11)
    box3_vol = round(box3.volume(), 2)

    box4 = Box(5.5, 7.78, 19)
    box4_vol = round(box4.volume(), 2)

    box_list = [box1_vol, box2_vol, box3_vol, box4_vol]
    
    print(box_sort(box_list))

if __name__=="__main__()": main()
main()
