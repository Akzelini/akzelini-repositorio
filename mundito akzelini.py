import random

palabras = (
    "abajo","abeja","abeto","abono","abril",
    "abrir","abuso","acaso","acato","acebo",
    "acera","acero","achis","acial","acnur",
    "acoso","actor","acuse","ademe","adobe"
)

while True:
    palabra = palabras[random.randint(0, len(palabras)-1)]
    wordle = list(palabra)

    print("""\033[1;37;44m
==============================[wordle]==============================
bienvenido ya elegi la palabra secreta tienes 5 intentos para adivinarla
====================================================================\033[0;30;47m""")

    for i in range(5):
        intento = input("ingresa una palabra de 5 letras sin acentos\n").lower()[:5]
