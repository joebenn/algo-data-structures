def bubble_sort(list):
    for iter_num in range(len(list)-1, 0, -1):
        for i in range(iter_num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [19,2,31,45,6,11,121,27]
bubble_sort(list)
print(list)