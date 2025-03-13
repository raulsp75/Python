#PrimoNoPrimo
num=int(input("Selecciona el número: "))
primo= True
for i in range(2,num):
    if (num % i == 0):
        print(f"El número {num} no es primo ya que es divisble por {i}")
        primo= False
        break
if primo:
    print(f"El número {num} es primo") 