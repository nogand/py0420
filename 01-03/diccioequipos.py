planilla={
    "Saprissa": {
        "Portero": "Aarón Cruz",
        "Entrenador": "Paté Centeno"
    },
    "La Liga": {
        "Portero": "Leonel Moreira",
        "Entrenador": "Andrés Carevic"
    }
}

for equipo in ["Saprissa", "La Liga"]:
    print("Estos son los datos del equipo:",equipo)
    for puesto in ["Portero", "Entrenador"]:
        print("\tEl",puesto,"de",equipo,"es:",planilla[equipo][puesto])
    print("")