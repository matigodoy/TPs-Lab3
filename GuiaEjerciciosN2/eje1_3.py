def carga():
    num1 = int(input("ingrese el primer valor: "))
    num2 = int(input("ingrese el segundo valor: "))
    num3 = int(input("ingrese el tercer valor: "))
    return (num1,num2,num3)

def mayor(num1,num2,num3):
    lista = [num1,num2,num3]
    return (max(lista))

valores = carga()
print("El mayor numero es:",mayor(valores[0],valores[1],valores[2]))

'''
----MANU----
numero = []
def carga():
    for i in range(3):
        num = int(input("Introduce el número: "))
        numero.append(num)
carga()
a = sorted(numero)
print("El mayor numero es:",numero[-1])

----LUCAS----
def carga():
    for x in range(3):
        num1 = int(input("Ingrese el primer valor"))
        num2 = int(input("Ingrese el segundo valor"))
        num3 = int(input("Ingrese el tercer valor"))
        aux = [num1, num2 , num3]
        return (aux)

def max_1(aux):
    return(max(aux))

print(max_1(carga()))
'''