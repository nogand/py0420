numero=int(input('Introduzca un número: '))
numero2=int(input('Introduzca otro número: '))

if numero>numero2 :
  print ("El número",numero,"es mayor que",numero2)
  print ("Es un número grande")
else :
  if numero==numero2 :
    print ("Ambos son iguales")
    print ("¡Ganador!")
  else :
    print ("El número",numero,"es menor que",numero2)
    print ("Es un número pequeño")
