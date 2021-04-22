class Torta():
    def __init__(self, formaEntrada, saborEntrada, alturaEntrada):
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada
    
    def mostrarAtributos(self):
        print(f'''La forma es {self.forma}
                    El sabor es de  {self.sabor}
                    La altura es de {self.altura}
        ''')

class Estudiante():
    def __init__(self, edadEntrada, nombreEntrada, idEntrada, carreraEntrada, semestreEntrada):
        self.id = idEntrada
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
    
    def estudiara(self, nombreMateria, cantidadTiempo):
        print (f'Hola soy {self.nombre} estudiante de {self.carrera}, y estudiare {nombreMateria} por {cantidadTiempo} minutos')

class Nutricionista ():
    def __init__(self, edadEntrada, nombreEntrada, universidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.universidad = universidadEntrada
    
    def IMC(self):
        preguntaPeso = "Cuantos pesas en kg? : "
        preguntaAltura = "Cuanto mides en metros? : "
        peso = float (input (preguntaPeso))
        altura = float (input (preguntaAltura))
        imc = peso /(altura **2)
        print (f'Hola soy {self.nombre} egresado de {self.universidad} y procedo a informarle que su IMC es de {imc}')