año=[('enero', 'febrero', 'marzo'), ('abril', 'mayo', 'junio'),('julio','agosto','septiembre'),('octubre','noviembre','diciembre')]

for trimestre in año:
  if type(trimestre) == type('texto') :
    print("ERROR: El contenido no es un conjunto de meses.")
  else :
    print("El trimestre contiene:")
    for mes in trimestre :
      print("",mes)
