#-----Constantes-----#
MENSAJE_INTRODUCTORIO = "Hola, a continuacion necesitaremos que nos suministre la siguiente informacion"
DIST_CM = "Introduzca una distancia en cm : "
UNIDAD = "Introduzca en que unidad quiere recibir la conversion : "
DIST_KM= "La distancia en KM es...."
DIST_M= "La distancia en M es...."
DIST_MM = "La distancia en MM...."
NO_VALIDO = "La unidad que esta utilizando no es valida"

#-----Entrada al codigo-----#
print (MENSAJE_INTRODUCTORIO)
cmdx = float (input (DIST_CM))
unidad = input (UNIDAD)
kmdist = cmdx / 100000
mdist = cmdx / 100
mmdist = cmdx * 10
resultado = ""
if (unidad == "KM") :
    resultado = DIST_KM, kmdist
elif (unidad == "M") :
    resultado = DIST_M, mdist
elif (unidad == "MM") :
    resultado = DIST_MM, mmdist
else :
    resultado = NO_VALIDO

print (resultado)

