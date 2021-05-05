def quick_sort(list):
    if len(list) < 2:
        return list
    
    left_list = []
    right_list = []
    pivot_list = []
    
    pivot = list[0]
    
    for value in list:
        if value == pivot:
            pivot_list.append(value)
        elif value < pivot:
            left_list.append(value)
        else:
            right_list.append(value)
            
    return quick_sort(left_list) + pivot_list + quick_sort(right_list)

if __name__ == '__main__': 
    

    print(quick_sort([99, 7, 1, 11, 0])  )                 