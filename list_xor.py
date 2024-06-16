# Python has a built-in 'xor' operator (^), but we are solving this without using it 

def list_xor(num, list1, list2):
    if num in list1 and num in list2:
        return False
    
    elif num not in list1 and num not in list2:
        return False
    
    return True