def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''

    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for ch in dna_string:
        if ch == 'A':
            count += 1
        if ch == 'C':
            count += 1
        if ch == 'G':
            count += 1
        if ch == 'T':
            count += 1

    return countA,countC,countG,countT

