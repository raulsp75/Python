#Suma número y haz la media hasta poner el número 0
num=(int)
suma=0
contador=0
while num != 0:
    contador= (contador + 1)
    num=(int(input("Selecciona un número: ")))
    suma= suma + num
media=(suma/(contador-1))
media=round(media, 2)
print(f"La suma de todos los número es {suma}")
print(f"La media de todos los número es {media}")