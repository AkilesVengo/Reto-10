lista1=[]  
lista2=[] 
x:int= int(input("ingresa la cantidad de elementos de la lista: "))
for i in range(x):
    valorProductopunto=int(input("Ingrese un valor entero perteneciente a la lista 1:"))
    lista1.append(valorProductopunto)

for i in range(x):
    valorProductopunto=int(input("Ingrese un valor entero perteneciente a la lista 2:"))
    lista2.append(valorProductopunto)

def CalcularProductoPunto(lista1, lista2)->int:
    ProductoPunto = 0
    y = 0
    for y in range(x):
       ProductoPunto+= ((lista1[y])*(lista2[y]))
    return ProductoPunto

if __name__ == "__main__":
    ProductoPunto = CalcularProductoPunto (lista1, lista2)

print(lista1)
print(lista2)
print("El producto punto de estos dos arreglos de listas es: ")
print(ProductoPunto)