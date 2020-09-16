
def file_sum(text_file):
    try:
        fh = open('file_sum.txt', 'rt')
        text_sum = 0
        for line in fh.readlines():
            for i in line:
                if i.isdigit() == True:
                    text_sum += int(i)
        fw = open('file_sum.txt', 'a')
        fw.writelines("\n" + "Sum: " + str(text_sum))
    finally:
        fh.close()

file_sum('file_sum.txt')