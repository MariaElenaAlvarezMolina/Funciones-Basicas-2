#1. Cuenta regresiva

def countdown(num):
    lista = []
    for i in range(num, -1, -1):
        lista.append(i) #También se puede usar "lista += [i]"
    return lista

lista_countdown = countdown(5)
print(lista_countdown)

def countdownWhile(num):
    lista = []
    while num >-1:
        lista.append(num)
        num -= 1
    return lista

lista_countdownWhile = countdownWhile(5)
print(lista_countdownWhile)

#2. Imprimir y devolver

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

lista_imprimir = ([1,2])
print(lista_imprimir)

#3. Primero más longitud

def primero_mas_longitud(lista):
    suma = lista[0] + len(lista)
    return suma

sum = primero_mas_longitud([1,2,3,4,5])
print(sum)

#4. Valores mayores que el segundo

def valores_mayores_que_el_segundo(lista1):
    lista2 = []
    if len(lista1) < 2:
        return False
    else:
        for num in lista1:
            if num > lista1[1]:
                lista2.append(num)

        print(len(lista2))
        return lista2

print_valores = valores_mayores_que_el_segundo([5,2,3,2,1,4])
print(print_valores)

#5. Esta longitud, ese valor

def length_and_value(a,b):
    lista = []
    for num in range(a):
        lista.append(b)
    return lista

print(length_and_value(4,7))