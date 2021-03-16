listaC = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
preguntaUnidad = '''
    F- Fahrenheit
    K- Kelvin
    C- Celcius
'''
valoresF = 'Mostrando los valores en Fahrenheit'
valoresK = 'Mostrando los valores en Kelvin'
valoresC = 'La conversion no es necesaria'
mensajeErrorEntrada ='valor ingresado no valido'

listaF = []
for elemento in listaC:
    conversor = round (elemento*1.8+32)
    listaF.append(conversor)
listaK = []
for elemento in listaC:
    conversor = round (elemento+273.15)
    listaK.append(conversor)

opcionUnidad = input(preguntaUnidad)
while (opcionUnidad !='F' and opcionUnidad != 'K' and opcionUnidad !='C' ):
    print ('ingresa una opción válida')
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