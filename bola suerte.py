yn = int(input("deseas saber tu suerte? (1=si/2=no): "))

if yn == 1:
    print("agitando la bola de la suerte...")
    import random
    suerte = random.randint(1, 9)

    if suerte == 1:
        print("tu suerte es 1, cuida de quien te rodea")
    elif suerte == 2:
        print("tu suerte es 2, dinero dinero dinero!!!")
    elif suerte == 3:
        print("tu suerte es 3, mira al suelo y veras una moneda")
    elif suerte == 4:
        print("tu suerte es 4, tendras un dia excelente")
    elif suerte == 5:
        print("tu suerte es 5, es un mal dia no una mala vida")
    elif suerte == 6:
        print("tu suerte es 6, a veces la fortuna se esconde en los lugares mas inesperados")
    elif suerte == 7:
        print("tu suerte es 7, que la suerte te acompañe")
    elif suerte == 8:
        print("tu suerte es 8, la venganza es un plato que se sirve frio")
    elif suerte == 9:
        print("tu suerte es 9, ja, hoy es tu dia de suerte")

else:
    print("cerrando la bola de la suerte...")
