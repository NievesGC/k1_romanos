unidades = {
    1: "I",
    5: "V",
    10:"X",
}

decenas = {
   1: "X",
   5: "L",
   10: "C"
}

centenas = {
   1: "C",
   5: "D",
   10: "M"
}

millares = {
   1: "M"
}

class RomanNumberError(Exception):
   pass

def entero_a_romano(n_int):

   if n_int > 3999:
      raise RomanNumberError("El número debe ser inferior a 4000")

   n__mil = n_int // 1000 * 1000
   n_cen = (n_int % 1000) // 100 * 100
   n_dec = (n_int % 100)//10*10
   n_uni = (n_int % 10)

   digitos = [n__mil,n_cen,n_dec,n_uni]

   resultado = ""

   for digito in digitos:
      if digito == 0:
         continue
      
      if digito >= 1000:
         clave = millares
         digito = digito // 1000
      elif digito >= 100:
         clave = centenas
         #digito //=100   
         digito = digito//100
      elif digito >= 10:
         clave = decenas
         digito = digito // 10
      else:
         clave = unidades
            

      if digito < 4:                            
         resultado += digito * clave[1]       
      elif digito == 4:   
         resultado += clave[1] + clave [5]                      
      elif digito< 9:
         num_palitos = digito -5
         resultado += clave[5] + num_palitos * clave[1]
      else:
         resultado += clave[1] + clave[10]
   return resultado
  
