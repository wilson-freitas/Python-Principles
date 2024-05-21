def mid(text):
    if len(text) %2 == 0:
        return ""
    else:
        middle_letter_pos = int((len(text) / 2) - 0.5)
        return(text[middle_letter_pos])

text = input()
print(mid(text))