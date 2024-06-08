def add_dots(text):
    left_limit = 0
    right_limit = 1
    new_text = ""

    while right_limit <= len(text):
        new_text += text[left_limit: right_limit]+"."
        left_limit += 1
        right_limit += 1
    return new_text[0:-1]

def remove_dots(text):
    return text.replace(".", "")

text_inpt = input()
print(remove_dots(add_dots(text_inpt)))
