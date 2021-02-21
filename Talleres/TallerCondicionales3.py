#-----Constantes-----#
MENSAJE_INTRODUCTORIO = "Bienvenido, a continuacion se les pedira unos datos"
AÑO_ACTUAL = "Digitar en que año se encuentra actualmente : "
AÑO_CUALQUIERA = "Digitar un año cualquiera : "
MENSAJE_TRANSC = "Han pasado...."
MENSAJE_FALT = "Faltan....."
AÑOS = "años"

#-----Entrada al codigo-----#
print (MENSAJE_INTRODUCTORIO)
añoA = int (input (AÑO_ACTUAL))
añoB = int (input (AÑO_CUALQUIERA))
añostransc = añoA - añoB
añosfalt = añoB - añoA 
isMayor = añoA > añoB
if (isMayor) :
    print (MENSAJE_TRANSC, añostransc,AÑOS)
else :
    print (MENSAJE_FALT, añosfalt,AÑOS)

