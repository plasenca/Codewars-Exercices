import log_file as log


# What I send to Codewars
def rolldice_sum_prob(num, quant_dies):
    
    from itertools import combinations_with_replacement
    # Initialize local variables
    cont = 0
    LIST_VALUES = [1, 2, 3, 4, 5, 6]*quant_dies
    
    # All numbers for each die
    total_combinations = list(set(combinations_with_replacement(LIST_VALUES, quant_dies)))

    for combination in total_combinations:
        sum_total = sum(combination)
        # Count how many combinations are
        if sum_total == num:
            cont+=1
    
    prob = cont/pow(6,quant_dies)
    return prob



# When I refactor the code 

def rolldice_sum_prob(num, quant_dies):
    
    from itertools import product
    # Initialize local variables
    cont = 0
    numbers_die = [1, 2, 3, 4, 5, 6]
    
    for combination in product(numbers_die, repeat=quant_dies):
        
        if sum(combination) == num:
            cont+=1
    
    prob = cont/pow(6,quant_dies)
    return prob
    

#? ¿Qué refactoricé?
#* Cambié el uso de la función "combinations_with_replacement", ya que tenía que hacer comversiones.
#* Estas conversiones, primero a set y luego a list, se dieron porque existían valores repetidos y
#* convertilos a set solo me retornaba los valores no repetidos. Era una buena solución, pero siento
#* que no era la mejor. Después, lo transformaba a lista porque necesitaba trabajar con ese objeto.
#* Era una buena solución, pero consumía más memoria de la que se nesecitaba realmente, tanto que tuve
#* dos errores en CodeWars, por el hecho de el tiempo de ejecución del programa.
#* Refactorización:
#* Esta refactorización fue hecha con dos ideas bien claras: evitar el uso de conversión de objetos y
#* evitar guardar todas esas combinaciones de números en memoria, ya que solo era necesario iterarlo.
#* Es por eso que usela función "product" de la librería itertools, que resolvió el primer problema.
#* Segundo, evité usar una variable y metí directamente el "product object" en la iteración for.
#* Esto, sumandole que el código se ve mejor diseñado, tiene mejor rendimiento que el anterior.

print(rolldice_sum_prob(35, 7))