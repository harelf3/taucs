def control_digit(id_num):
    """ compute the check digit in an Israeli ID number,
    given as a string of 8 digits
    """

    total = 0
    for i in range(8):
        val = int(id_num[i]) # converts char to int
        if i%2 == 0: # even index (0,2,4,6)
            total += val
        else: # odd index (1,3,5,7)
            if val < 5:
                total += 2*val
            else:
                total += ((2*val)%10) + 1 # sum of digits in 2*val
            # 'tens' digit must be 1
        print(type(val))
    total = total%10 # 'ones' (rightmost) digit
    check_digit = (10-total)%10 # the complement modulo 10 of total
    # for example 42->8, 30->0
    
    return str(check_digit)

control_digit("212077333")