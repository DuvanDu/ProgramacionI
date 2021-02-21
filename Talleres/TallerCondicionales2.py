#-----Constantes-----#
MENSAJE_INTRODUCTORIO = "Hola buenos dias, aqui te informaremos en que rango de edad estas"
PREGUNTA_EDAD = "Cuantos años tienes? : "
MENSAJE_MENOR_EDAD = "Eres menor de edad"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = "Eres adulto"
MENSAJE_ADULTO_MAYOR = "Eres un adulto mayor"

#-----Entrada al codigo-----#
print (MENSAJE_INTRODUCTORIO)
edad = int (input (PREGUNTA_EDAD))
isMenorEdad = edad < 18
isJoven = edad >= 18 and edad < 26
isAdulto = edad >= 26 and edad < 61
isAdultoMayor = edad >= 61
resultado = ""
if (isMenorEdad) :
    resultado = MENSAJE_MENOR_EDAD
elif (isJoven) :
    resultado = MENSAJE_JOVEN
elif (isAdulto) :
    resultado = MENSAJE_ADULTO
else :
    resultado = MENSAJE_ADULTO_MAYOR

print (resultado)