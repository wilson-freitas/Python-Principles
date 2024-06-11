def all_equal(par_list):
    for el in par_list:
        if el != par_list[0]:
            return False
    
    return True