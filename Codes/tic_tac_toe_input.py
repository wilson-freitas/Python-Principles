def get_row_col(position_str):
    if position_str[0] == "A":
        col = 0

    elif position_str[0] == "B":
        col = 1
        
    elif position_str[0] == "C":
        col = 2

    row = int(position_str[1]) - 1
    position_tuple = (row, col)

    return(position_tuple)