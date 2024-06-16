# The special *args syntax allow us to pass multiple variables to a function, it store them in a list 

def param_count(*args):
    return len(args)

print (param_count(5, 4, 3))

