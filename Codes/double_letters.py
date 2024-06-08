def double_letters(word):
    count = 0
    while count <= len(word) - 2:
        if word[count] == word[count + 1]:
            return True
        count += 1
    return False
        
word = input()

print(double_letters(word))
