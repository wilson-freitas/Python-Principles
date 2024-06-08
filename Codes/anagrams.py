def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        for letter in word2:
            if word1.count(letter) != word2.count(letter):
                return False
        
        return True

