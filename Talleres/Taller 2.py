#-----Constantes-----#
PREGUNTA_NUMEROA = "Ingrese un numero X : "
PREGUNTA_NUMEROB = "Ingrese un numero Y : "


#-----Entrada al codigo-----#
numeroX = int (input (PREGUNTA_NUMEROA))
numeroY = int (input (PREGUNTA_NUMEROB))
print ("#"*15, "¿X Mayor que Y?", "#"*15)
isMayorNumero = numeroX > numeroY
print (isMayorNumero)
print ("#"*15, "¿X menor que Y?", "#"*15)
isMenorNumero = numeroX < numeroY
print (isMenorNumero)
print ("#"*15, "¿X igual a Y?", "#"*15)
isIgualNumero = numeroX == numeroY
print (isIgualNumero)
sumar = numeroX + numeroY
print ("El resultado de la suma", sumar)
resta = numeroX - numeroY
print ("El resultado de la resta", resta)
multiplicacion = numeroX * numeroY
print ("El resultado de la multiplicacion", multiplicacion)
dividir = numeroX / numeroY
print ("El resultado de la division", dividir)
elevar = numeroX ** numeroY
print ("El resultado del exponente", elevar)

