pruebaV = True
pruebaF = False
print (pruebaF)
print (pruebaV)
pruebaV = pruebaF
print (pruebaV)
edad = 21
estatura = 1.83
peso = 77
NOMBRE = "Duvan Felipe Duque"
print ("#"*15, "Mayor de Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
print ("#"*15, "Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print (isMayorEstatura)
print ("#"*15, "Peso diferente 77", "#"*15)
isPesoDiferente = peso != 77
print (isPesoDiferente)
print ("#"*15, "Esta apellido en el nombre?", "#"*15)
apellido = "Duque"
isApellido = apellido in NOMBRE
print (isApellido)
