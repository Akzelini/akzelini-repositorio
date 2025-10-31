info_tienda = ("hacemos que parezca facil", 2007)

juegos = {
    "COD" : 2,
    "Yakuza" : 3,
    "RDR2" : 5
}

print("akzelini videojuegos")
print(info_tienda[0], "-", info_tienda[1])
print("")

while True:
    ele = input("escribe el juego que juego quieres comprar? COD, Yakuza, RDR2: ")
    if ele in juegos:
        if juegos[ele] > 0:
            print("compraste", ele)
            juegos[ele] -= 1
            print("quedan", juegos[ele], "en stock")
            if juegos[ele] == 0:
                print("ya no hay mas de ese juego")
        else:
            print("no hay stock de ese juego")
    else:
        print("ese juego no existe")

    op = input("quieres comprar otro? (si/no) ").strip().lower()
    if op == "no":
        print("gracias por comprar en akzelini videojuegos")
        print(info_tienda[0], "-", info_tienda[1])
        break