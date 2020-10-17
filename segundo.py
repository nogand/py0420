numero=int(input('Introduzca un número: '))

if numero>100 :
  print ("El número",numero,"es mayor que cien")
  print ("Es un número grande")
else :
  if numero==100 :
    print ("Es el número 100")
    print ("¡Ganador!")
  else :
    print ("El número",numero,"es menor que cien")
    print ("Es un número pequeño")
