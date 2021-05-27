class Humano():
    def __init__(self, nombreEntrada, edadEntrada,sexoEntrada):
        print('Hola soy un humano nuevo')
        self.edad = edadEntrada
        self.raza = 'Humano'
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
    
    def hablar(self,mensaje):
        '''Expresa mensaje ingesado '''
        print(f'Hola soy {self.nombre} tengo un mensaje que decir ...', mensaje)

class Doctor(Humano):
    def __init__(self,nombreEntrada, edadEntrada,estaturaEntrada,areaEntrada):
        Humano.__init__(self, nombreEntrada,edadEntrada,estaturaEntrada)
        self.area = areaEntrada

    def imc(self, pesoEntrada, estaturaEntrada):
        self.peso = pesoEntrada
        self.estatura = estaturaEntrada
        imc = peso /(estatura **2)
        print(f'Hola soy el doctor {self.nombre} y procedo a decirle su imc el cual es.. {imc}')