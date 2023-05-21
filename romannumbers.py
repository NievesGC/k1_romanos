simbolos = {
    1: "I",
    5: "V",
    10:"X"
}

def entero_a_romano(n_int):
    if n_int in simbolos:                   #POR AQUI ENTRA : 1, 5 Y 10
      return simbolos[n_int]

    if n_int < 4:                            #POR AQUI ENTRA : 2 Y 3
       return n_int * simbolos[1]       
    elif n_int == 4:                         #POR AQUI ENTRA : 4
        return simbolos[1] + simbolos[5]     
    elif n_int == 9:
       return simbolos[1] + simbolos[10]
    else:
       multiplicador = n_int -5
       return simbolos[5] + multiplicador * simbolos[1]
    
    