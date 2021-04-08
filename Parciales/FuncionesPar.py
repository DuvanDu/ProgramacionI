#----------Linea de separacion -----------#
def linedesign(cantidad = 10, simbolo = '#'):
    print(simbolo *cantidad)
    return None
#----------Punto 1 -----------#
#----------Sumar dos números -----------#
def sumar (a = 0, b = 0, c = 0):
    suma = a + b + c
    return suma
print(sumar())
#----------Restar dos números -----------#
def restar (a = 0, b = 0, c = 0):
    resta = a - b
    return resta
print(restar())
#----------Multiplicar dos números -----------#
def multiplicar (a = 0, b = 0, c = 0):
    multiplica = a * b * c
    return multiplica
print(multiplicar())
#----------dividir dos números -----------#
def dividir (a = 4, b = 2, c = 2):
    dividi = a / b / c
    return dividi
print(dividir())
#----------potenciar dos números -----------#
def potenciar (base = 2, exponente = 1, exponente2 = 2):
    potencia = (base ** exponente) ** exponente2
    return potencia
print(potenciar())
#----------Punto 2 -----------#
#----------mostrar listas -----------#
def mostrarLista(listaEntrada = []):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista= [213,32,23123,321,233,1232,23]
lista2 = [564654,645,64543,2565,547,57865]
lista3 = [2123,575,747,8696,8779,123]
linedesign(3,'(ง •̀_•́)ง')
mostrarLista(lista)
linedesign(3,'(ง •̀_•́)ง')
mostrarLista(lista2)
linedesign(3,'(ง •̀_•́)ง')
mostrarLista(lista3)
#----------Punto 3 -----------#
#----------Area triangulo -----------#
def areaTrir (baseTri, alturaTri):
    area = ((baseTri * alturaTri) / 2)
    return area
baseIngresada = int (input('Ingrese una base entera : '))
alturaIngresada = int (input('ingrese un altura entero : '))
print(areaTrir(baseIngresada, alturaIngresada))
#----------Punto 4 -----------#
#----------Valores lista -----------#
def mostrarTopes(listaEntrada = []):
    acumulador = 0
    for elemento in listaEntrada:
        acumulador += elemento
    mayor =max(listaEntrada)
    menor =min(listaEntrada)
    promedio =acumulador/len(listaEntrada)
    return mayor, menor, promedio
lista= [213,32,23123,321,233,1232,23]
print('El numero mayor es', mostrarTopes(lista)[0])
print('El numero menor es', mostrarTopes(lista)[1])
print ('El promedio de la lista es', mostrarTopes(lista)[2])

