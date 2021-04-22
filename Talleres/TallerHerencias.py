class Persona():
    
    def __init__(self, idEntrada, nombreEntrada, edadEntrada):
        self.id = idEntrada
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.raza = 'Humano'
    
    def hablar(self,mensaje):
        '''Expresa mensaje ingesado '''
        print(f'Hola soy {self.nombre} tengo un mensaje que decir ...', mensaje)
    
    def caminar(self,cantidadPasos):
        for i in range (cantidadPasos):
            print(f'Hola soy {self.nombre} y he dado {i+1} pasos')

class Medico(Persona):    
    def __init__(self, idEntrada, nombreEntrada, edadEntrada, especialidadEntrada):
        Persona.__init__(self, idEntrada, nombreEntrada, edadEntrada)
        self.especialidad = especialidadEntrada
    
    def diagnostico(self, nombreEnfermedad):
        print (f'Hola soy {self.nombre}{self.especialidad} y procedo a tratar dicha enfermedad {nombreEnfermedad}')

class Nutricionista (Persona):
    
    def __init__(self, idEntrada, nombreEntrada, edadEntrada, universidadEntrada):
        Persona.__init__(self, idEntrada, nombreEntrada, edadEntrada)
        self.universidad = universidadEntrada
    
    def IMC(self):
        preguntaPeso = "Cuantos pesas en kg? : "
        preguntaAltura = "Cuanto mides en metros? : "
        peso = float (input (preguntaPeso))
        altura = float (input (preguntaAltura))
        imc = peso /(altura **2)
        print (f'Hola soy {self.nombre} egresado de {self.universidad} y procedo a informarle que su IMC es de {imc}')
