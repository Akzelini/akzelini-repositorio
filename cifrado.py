def cifrado_cesar(texto, desp):
    res = ""
    for c in texto:
        if c.isalpha():
            if c.isupper():
                res += chr((ord(c) - 65 + desp) % 26 + 65)
            else:
                res += chr((ord(c) - 97 + desp) % 26 + 97)
        else:
            res += c
    return res

print("que deseas hacer?")
print("1. cifrar")
print("2. descifrar")
op = input("elige una opcion? ")

txt = input("escribe el texto? ")
desp = int(input("cuanto mover? "))

if op == "1":
    print("resultado:", cifrado_cesar(txt, desp))
elif op == "2":
    print("resultado:", cifrado_cesar(txt, -desp))
else:
    print("opcion no valida")
