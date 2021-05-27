
PREGUNTA_USUARIO = "Ingrese nombre de usuario : "
PREGUNTA_DOLARES = "Ingrese cuantos dolares tiene : "

isCorrectData = False
while (isCorrectData == False):
    try:
        usuario = input(PREGUNTA_USUARIO)
        assert(usuario.isalpha())
        isCorrectData = True
    except AssertionError:
        print('datos incorrectos ingrese nuevamente')

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        dolares = int (input('ingrese cuantos dolares tiene :'))
        isCorrectInfo = True
    except ValueError:
        print('ingresaste un dato no válido')

euros = dolares*0.82
print(f'Hola {usuario} procedo a decirle cuantos euros tiene.. {euros}€')
