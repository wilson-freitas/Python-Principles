# given two lists, return a list of tuples, each tuple has the respective elements of the lists
# for example: [1, 2] [3, 4] should return [(1,3), (2,4)]
# we could do it using list comprehension, but i decide to go for the more readable approach
def zap(list1, list2):
    tuples_list = []
    pos = 0

    while pos < len(list1):
        aux_tuple = (list1[pos], list2[pos])
        tuples_list.append(aux_tuple)

        pos +=1

    return tuples_list
