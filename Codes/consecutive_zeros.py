def consecutive_zeros(binary_str):
    # Storing the consecutive zeros in a list ex: 10010001 will be --> ['', '00', '', '000', '']
    zeros_list = binary_str.split("1")

    return (len(max(zeros_list)))

    