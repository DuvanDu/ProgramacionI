listaC = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
preguntaTemperatura = '''
    H- Mostrar personas con hipotermia
    F- Mostrar personas con fiebre
    N- Mostrar personas con temperatura normal
'''
mensajeHipotermia = 'Mostrando persononas con Hipotermia'
mensajeFiebre = 'Mostrando personas con Fiebre'
mensajeNormales = 'Mostrando personas con temperatura Normal'
mensajeErrorEntrada ='valor ingresado no valido'

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

opcionUnidad = input(preguntaTemperatura)
while (opcionUnidad !='H' and opcionUnidad != 'F' and opcionUnidad !='N' ):
    print ('ingresa una opción válida')
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