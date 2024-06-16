def format_number(num):
    if num <= 999:
        return (str(num))
    
    else:
        num_str = str(num)
        size_num = len(num_str)

        if size_num %3 == 1:
            aux_list = []
            pos = 0
            while pos < size_num:
                if pos == 1 or (pos-1)%3 == 0:
                    aux_list.append(",")
                aux_list.append(num_str[pos])
                pos +=1

            formated_num = ''.join(aux_list)
            return formated_num
        
        
        elif size_num %3 == 2:
            aux_list = []
            pos = 0
            while pos < size_num:
                if pos == 2 or (pos-2)%3 == 0:
                    aux_list.append(",")
                aux_list.append(num_str[pos])
                pos +=1

            formated_num = ''.join(aux_list)
            return formated_num
        
        else:
            aux_list = []
            pos = 0
            while pos < size_num:
                if pos == 3 or ((pos)%3 == 0 and pos!= 0):
                    aux_list.append(",")
                aux_list.append(num_str[pos])
                pos +=1

            formated_num = ''.join(aux_list)
            return formated_num
