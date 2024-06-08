def largest_difference(list_of_numbers): # We could use the min() and max() methods, but it would be too easy
    count = 0

    for number in list_of_numbers:
        if count == 0:
            big_num = number
            small_num = number
            count = 1

        else:
            if number > big_num:
                big_num = number
            if number < small_num:
                small_num = number
        
    return big_num - small_num
    
