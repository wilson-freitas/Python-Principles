# The catch here is to notice that the number of syllabes is the number of "-" + 1
# example: ho-tel --> 1 "-" and 2 syllabes

# we could create a loop that counts the hyphens, but the 'count' method is so easy to use
def count(word):
    num_syllabes = word.count("-") + 1
    return num_syllabes

word = input()
count(word)