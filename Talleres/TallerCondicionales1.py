#-----Constantes-----#
MENSAJE_INTRODUCTORIO = "Hola buen dia, a continuacion debera ingresar dos numeros"
MENSAJE_IGUALES = "Los numeros X y Y son iguales"
MENSAJE_MAYOR = "X es mayor que Y"
MENSAJE_MENOR = "Y es mayor que X"
INGRESE_X = "Ingrese numero X : "
INGRESE_Y = "Ingrese numero Y : "

#-----Entrada al codigo-----#
print (MENSAJE_INTRODUCTORIO)
numeroX = int (input (INGRESE_X))
numeroY = int (input (INGRESE_Y))
isMayor = numeroX > numeroY
isMenor = numeroX < numeroY
resultado = ""
if (isMayor) :
    resultado = MENSAJE_MAYOR
elif (isMenor) :
    resultado = MENSAJE_MENOR
else :
    resultado = MENSAJE_IGUALES

print (resultado)
