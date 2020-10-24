meses=[('enero', 'febrero', 'marzo'), ['abril', 'mayo', 'junio']]
for mes in meses:
  if type(mes) == type('palabra') :
    print(mes)
  else :
    print("Apareció un contenedor:")
    for contenido in mes :
      print("",contenido)
