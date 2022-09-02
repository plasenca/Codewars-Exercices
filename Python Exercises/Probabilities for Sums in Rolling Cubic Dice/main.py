import log_file as log

from collections import Counter
from itertools import combinations_with_replacement

def rolldice_sum_prob(num, quant_dies):
    # Initialize local variables
    cont = 0
    list_matched = []
    LIST_VALUES = [1, 2, 3, 4, 5, 6]*quant_dies
    
    # All numbers for each die
    
    total_combinations = list(set(combinations_with_replacement(LIST_VALUES, quant_dies)))

    list_ = map()
    
    for combination in total_combinations:
        sum_total = sum(combination)
        if sum_total == num:
            list_matched.append(combination)
            cont+=1
    
    print(f"Conteo: {cont}\nDivisión: {cont}/{pow(6,quant_dies)}")
    return cont/pow(6,quant_dies)

print(rolldice_sum_prob(35, 7))
