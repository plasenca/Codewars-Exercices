import log_file as log


def rolldice_sum_prob(num, quant_dies):
    
    from itertools import combinations_with_replacement
    # Initialize local variables
    cont = 0
    list_matched = []
    LIST_VALUES = [1, 2, 3, 4, 5, 6]*quant_dies
    
    # All numbers for each die
    
    total_combinations = list(set(combinations_with_replacement(LIST_VALUES, quant_dies)))

    for combination in total_combinations:
        sum_total = sum(combination)
        # Count how many combinations are
        if sum_total == num:
            cont+=1
    
    print(f"Conteo: {cont}\nDivisión: {cont}/{pow(6,quant_dies)}")
    return cont/pow(6,quant_dies)
        
print(rolldice_sum_prob(35, 7))
