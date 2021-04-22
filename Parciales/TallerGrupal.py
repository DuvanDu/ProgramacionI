class ElementosDigitales():
    
    def __init__(self, nombreEntrada, creadorEntrada, fechapuEntrada):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fechapu = fechapuEntrada
    
    def mostrarAtributos(self):
        print(f'''El nombre del autor {self.nombre}
                    Su creador es {self.creador}
                    Su fecha de publicacion {self.fechapu}
        ''')

class Usuario():
    
    def __init__(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.sexo = sexoEntrada
        self.nacionalidad = nacionalidadEntrada
    
    def mostrarAtributos(self):
        print(f'''El nombre del usuario {self.nombre}
                    Su edad es {self.edad}
                    Sexo {self.sexo}
                    Su nacionalidad es {self.nacionalidad}
        ''')
    
    def cancion(self,nombreCancion):
        '''Expresa que esta escuchando una cancion'''
        print(f'Hola soy {self.nombre} y estoy escuchando {nombreCancion}')

class Pagina():
    
    def __init__(self, tipoEntrada, formatoEntrada, fechapuEntrada):
        self.tipo = tipoEntrada
        self.formato = formatoEntrada
        self.fechapu = fechapuEntrada
    
    def mostrarAtributos(self):
        print(f'''Su tipo de entrada es {self.tipo}
                    Su formato es {self.formato}
                    Se publico el {self.fechapu}
        ''')

class Cancion(ElementosDigitales):
    
    def __init__(self, nombreEntrada, creadorEntrada, fechapuEntrada, generoEntrada, duracionEntrada):
        ElementosDigitales.__init__(self, nombreEntrada, creadorEntrada, fechapuEntrada)
        self.genero = generoEntrada
        self.duracion = duracionEntrada
    
    def nueCancion(self,nombreCancion, fecha):
        '''Expresa que esta escuchando una cancion'''
        print(f'Hola soy {self.nombre} y estoy escuchando {nombreCancion} de {fecha} ')
    
    def bucleCancion(self, cantidadRepro, nombreCancion):
        for i in range (cantidadRepro):
            print(f'{nombreCancion} sonando {i+1} vez')

class Artista(Usuario):
    
    def __init__(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada, generoEntrada, numeroCanEntrada, numeroAlbEntrada):
        Usuario.__init__(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada)
        self.genero = generoEntrada
        self.numeroCan = numeroCanEntrada
        self.numeroAlb = numeroAlbEntrada
    
    def concierto(self,nombreCiudad):
        '''Expresa que dara un concierto en dicha ciudad'''
        print(f'Hola soy {self.nombre} y dare un concierto en {nombreCiudad}')

class Favoritos(Pagina):
    
    def __init__(self, tipoEntrada, formatoEntrada, fechapuEntrada, favoritosComEntrada, listaFavEntrada, fechaUpEntrada):
        Pagina.__init__(self, tipoEntrada, formatoEntrada, fechapuEntrada)
        self.favoritosCom = favoritosComEntrada
        self.listaFav = listaFavEntrada
        self.fechaUp = fechaUpEntrada
#-----Integrantes: Mariana Villegas y  Duvan Duque-----#