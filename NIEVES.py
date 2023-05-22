def sacar_unidad(n_int):
   n_int_str = str(n_int)
   unidad = n_int_str[1:]
   unidad = int(unidad)
   return unidad

def decimales(n_int):
    d = sacar_unidad(n_int)
    u = entero_a_romano(d)
    decimal = n_int - d
    if n_int > 11 and n_int < 19: #MIRAR QUE FALLA
      return simbolos[10] + u
    elif n_int >= 20 and n_int <=39:  
      return simbolos[10] * (decimal//10) + u
    elif n_int >= 40 and n_int <= 49:
       return simbolos[10] + simbolos[50] + u
    elif n_int >= 50 and n_int <= 59:
       return simbolos[50]  + u
    elif n_int >= 60 and n_int <= 69:
       return simbolos[50]  + simbolos[10] + u
    elif n_int >= 70 and n_int <= 79:
       return simbolos[50]  + simbolos[10]*2 + u
    elif n_int >= 80 and n_int <= 89:
       return simbolos[50]  + simbolos[10]*3 + u
    elif n_int >= 90 and n_int <= 99:
       return simbolos[10]  + simbolos[100] + u
