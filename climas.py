tiempo_hoy = {
    "soleado",
    "nublado",
    "lluvioso"
}

print("Opciones de tiempo: soleado, nublado, lluvioso")
clima = input("Como esta el tiempo hoy? ")

if clima in tiempo_hoy:
    print("Dato del tiempo guardado")
else:
    print("No se reconoce ese tipo de tiempo")

semana = {
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sabado",
    "domingo"
}

print("Opciones de dia: lunes, martes, miercoles, jueves, viernes, sabado, domingo")
dia = input("Que dia es hoy? ")

if dia in semana:
    print("Dia guardado correctamente")
else:
    print("Dia no valido")

# Lluvioso
if (dia in {"lunes","martes","miercoles","jueves","viernes"}) and clima == "lluvioso":
    print("Hoy es un buen dia para un cafe")
elif (dia in {"sabado","domingo"}) and clima == "lluvioso":
    print("Toca netflix n chill")
else:
    pass

# Soleado
if (dia in {"lunes","martes","miercoles","jueves","viernes"}) and clima == "soleado":
    print("Hoy es un buen dia para ir a la playa a comer mariscos")
elif (dia in {"sabado","domingo"}) and clima == "soleado":
    print("Hoy es un buen dia para ir al parque")
else:
    pass

# Nublado
if (dia in {"lunes","martes","miercoles","jueves","viernes"}) and clima == "nublado":
    print("Uy, vaya clima, exelente para programar en python ^_^")
elif (dia in {"sabado","domingo"}) and clima == "nublado":
    print("Toca maraton de videojuegosss")
else:
    pass
