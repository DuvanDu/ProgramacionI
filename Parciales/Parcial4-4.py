import sys
nombre  = input('ingrese su nombre : ')
descripcionenf = input('ingrese informacion de su enfermedad: ')
precio = int(input('ingrese precio de la consulta : '))

nombreArchivo = "pacientes.txt"
try:
    archivo = open(nombreArchivo)
    print('1')
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    descripcion = 'Archivo de pacientes'
    print("2")
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open(nombreArchivo,'a')
linea = "\nnombre:" + nombre + " enfermedad: " + descripcionenf + " precio: "+ str(precio)
archivo.writelines(linea)
archivo.close()

#leer
with open (nombreArchivo,'r') as reader:
    for line in reader:
        print(line)