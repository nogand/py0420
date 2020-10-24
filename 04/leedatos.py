
paises={}

def leerPais():
  pais=input('Nombre del país: ')
  lider=input('Presidente: ')
  capital=input('Capital: ')
  return pais, {"lider": lider, "capital": capital}

while True:
  print("Introduzca un país nuevo.")
  pais, datos=leerPais()
  paises[pais]=datos
  print("Tengo estos paises: ", paises)
