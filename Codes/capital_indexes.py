def capital_indexes(text):
    capitals_list = []
    
    # PT-BR: Optei por utilizar 'position_pointer' para simplificar o código. Métodos como 'isupper()' retornariam apenas a primeira ocorrência da letra sendo verificada. O ponteiro me indica a posição exata da letra atual na string.
    # EN: I opted to use 'position_pointer' to simplify the code. Methods like 'isupper()' would only return the first occurrence of the checked letter. The pointer indicates the exact position of the current letter in the string.
    position_pointer = 0
    for letter in text:
        if letter.isupper() == True:
            capitals_list.append(position_pointer)
        position_pointer += 1
    return capitals_list

text = input()
print(capital_indexes(text))
