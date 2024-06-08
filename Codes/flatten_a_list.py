def flatten(list_of_lists):
    flat_list = []

    for list in list_of_lists:
        for item in list:
            flat_list.append(item)
    
    return flat_list