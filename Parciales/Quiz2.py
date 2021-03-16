#----Preguntas----#
preguntaNumero = '''Ingrese alguna de estas opciones
    1.Hacer conversión de temperatura
    2.Temperatura saludables
    3.Mostrar maximos y minimos
    4.Salir
    '''
preguntaUnidad = '''
    F- Fahrenheit
    K- Kelvin
    C- Celcius
'''
preguntaTemperatura = '''
    H- Mostrar personas con hipotermia
    F- Mostrar personas con fiebre
    N- Mostrar personas con temperatura normal
'''
#----Mensajes---#
valoresF = 'Mostrando los valores en Fahrenheit'
valoresK = 'Mostrando los valores en Kelvin'
valoresC = 'La conversion no es necesaria'
mensajeHipotermia = 'Mostrando persononas con Hipotermia'
mensajeFiebre = 'Mostrando personas con Fiebre'
mensajeNormales = 'Mostrando personas con temperatura Normal'
mensajeErrorEntrada ='valor ingresado no valido'
mensajeMayor = 'La temperatura maxima ingresado es -->'
mensajeMenor = 'La temperatura minima ingresado es -->'
mensajeDespedida ='☺Que tengas un feliz día ☺☻'

#----Error---#
mensajeErrorEntrada ='valor ingresado no valido'


listaC = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#Conversion punto 1
listaF = []
for elemento in listaC:
    conversor = round (elemento*1.8+32)
    listaF.append(conversor)
listaK = []
for elemento in listaC:
    conversor = round (elemento+273.15)
    listaK.append(conversor)

#Clasificacion punto 2
listaHipo = []
for elemento in listaC:
    conversor = round (elemento < 36)
    listaHipo.append(conversor)
listaFie = []
for elemento in listaC:
    conversor = round (elemento > 37.6)
    listaFie.append(conversor)
listaNorm = []
for elemento in listaC:
    conversor = round (elemento >= 36 and elemento <= 37)
    listaNorm.append(conversor)



opcionEscogida = int(input(preguntaNumero))
while (opcionEscogida !=4):
    #---------Opcion1---------#
    if (opcionEscogida == 1):
        opcionUnidad = input(preguntaUnidad)
        if (opcionUnidad == 'F'):
            print(valoresF)
            print(listaF)
        elif (opcionUnidad == 'K'):
            print(valoresK)
            print(listaK)
        elif (opcionUnidad == 'C'):
            print(valoresC)
            print(listaC)
        else:
            print(mensajeErrorEntrada)
    #---------Opcion2---------#
    elif (opcionEscogida == 2):
        opcionUnidad = input(preguntaTemperatura)
        if (opcionUnidad == 'H'):
            print(mensajeHipotermia)
            print(listaHipo)
        elif (opcionUnidad == 'F'):
            print(mensajeFiebre)
            print(listaFie)
        elif (opcionUnidad == 'N'):
            print(mensajeNormales)
            print(listaNorm)
        else:
            print(mensajeErrorEntrada)
    #---------Opcion3---------#
    elif(opcionEscogida == 3):
        print(mensajeMayor, max(listaC))
        print(mensajeMenor, min(listaC))
    #---------Opcion no valida---------#
    else:
        print(mensajeErrorEntrada)
    opcionEscogida = int(input(preguntaNumero))

print (mensajeDespedida)