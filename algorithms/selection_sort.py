def selection_sort(input_list):
    for i in range(len(input_list)):
        min_index = i
        for j in range(i+1, len(input_list)):
            if input_list[min_index] > input_list[j]:
                min_index = j
        # Swap the minimum value with the compared value
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

l = [19,2,31,45,30,11,121,27]
selection_sort(l)
print(l)
