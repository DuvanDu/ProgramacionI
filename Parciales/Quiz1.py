#-----Constantes-----#
MENSAJE_BIENVENIDA = "Hola como estas? Porfavor suministranos tu nivel de trigliceridos y homocisteina"
PREGUNTA_TRIGLI = "Nivel de trigliceridos en sangre? : "
PREGUNTA_HOMOCIS = "Nivel de homocisteina en sangre? : "
MENSAJE_OPTIMO_TRI = "Trigliceridos en sangre en estado optimo"
MENSAJE_SOBRE_LIMITE_TRI = "Trigliceridos en sangre en el limite optimo"
MENSAJE_ALTO_TRI = "Trigliceridos en sangre alto, favor consultar con un medico"
MENSAJE_MUY_ALTO_TRI = "Trigliceridos en sangre demasiado alto, consultar urgentemente con un medico"
MENSAJE_OPTIMO_HO = "Homocisteina en sangre en estado optimo"
MENSAJE_SOBRE_LIMITE_HO = "Homocisteina en sangre en el limite optimo"
MENSAJE_ALTO_HO = "Homocisteina en sangre alto, favor consultar con un medico"
MENSAJE_MUY_ALTO_HO = "Homocisteina en demasiado alto, consultar urgentemente con un medico"

#-----Entrada al codigo-----#
print (MENSAJE_BIENVENIDA)
trigliceridos = int (input (PREGUNTA_TRIGLI))
homocisteina = int (input (PREGUNTA_HOMOCIS))
isOptimoTri = trigliceridos < 150
isSobreLimiteTri = trigliceridos >= 150 and trigliceridos < 199 
isAltoTri = trigliceridos >= 200 and trigliceridos < 499
isOptimoHomocis = homocisteina >= 2 and homocisteina < 15
isSobreLimiteHomocis = homocisteina >= 15 and homocisteina < 30
isAltoHomocis = homocisteina >= 30 and homocisteina < 100

resultado = ""

if (isOptimoTri) :
    resultado = MENSAJE_OPTIMO_TRI
elif (isSobreLimiteTri) :
    resultado = MENSAJE_SOBRE_LIMITE_TRI
elif (isAltoTri) :
    resultado = MENSAJE_ALTO_TRI
else :
    resultado = MENSAJE_MUY_ALTO_TRI

print (resultado)

if (isOptimoHomocis) :
    resultado = MENSAJE_OPTIMO_HO
elif (isSobreLimiteHomocis) :
    resultado = MENSAJE_SOBRE_LIMITE_HO
elif (isAltoHomocis) :
    resultado = MENSAJE_ALTO_HO
else :
    resultado = MENSAJE_MUY_ALTO_HO

print (resultado)
