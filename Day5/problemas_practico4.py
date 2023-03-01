#funcion contar primos que ingrese un numero y devuelva la cantidad de numeros primos que hay entre 1 y ese numero

def contar_primos(num):
  primos = [2]
  iteracion = 3
  
  if num < 2:
    return 0
  
  while iteracion <= num:
        for i in range(3, iteracion):
      
            if iteracion % i == 0:
                iteracion += 1
                break
        else:
            primos.append(iteracion)
            iteracion += 1
  print(primos)
  return len(primos)

print(contar_primos(150))