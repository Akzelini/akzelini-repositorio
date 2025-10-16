texto = input("Ingresa un texto: ").lower()
letras = []
for i in range(3):
    letra = input(f"Ingrese una letra {i+1}: ").lower()
    letras.append(letra)

print("Resultado")

for letra in letras:
    if letra in texto:
        print(f"La letra {letra} aparece {texto.count(letra)} veces")

palabras = texto.split()
print("El texto tiene", len(palabras), "palabras")
print(f"Primera letra del texto: {texto[0]}")
print(f"Última letra del texto: {texto[-1]}")
texto_invertido = " ".join(palabras[::-1])
print(f"Texto invertido: {texto_invertido}")

if "python" in texto:
    print("La palabra 'python' sí está en el texto")
else:
    print("La palabra 'python' no está en el texto")
