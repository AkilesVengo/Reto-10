lista=[]
i= int(input("ingresa la cantidad de elementos de la lista: "))
for x in range(i):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)
print("el promedio de la lista es:")
print(sum(lista)/i)