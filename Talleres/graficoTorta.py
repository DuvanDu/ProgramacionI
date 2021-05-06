import matplotlib.pyplot as plt
pieExplode = [0.2,0,0,0]
acumulador = 0
porcentajeHabitantes = [5.10,4.42,1.81,0.99]
pieLabels = ['Medellin', 'Cali', 'Cartagena', 'SantaMarta',]
def etiquetarElementosPorcentuales(porcentajeHabitantes, labels, indicador= ' ->'):

  for i in range (len(labels)):
    pieLabels[i] += str(porcentajeHabitantes) +'%'

plt.pie(porcentajeHabitantes,labels=pieLabels, 
        explode=pieExplode, 
        shadow= True, 
        counterclock = True, 
        startangle= 45)
#####################
plt.title('Porcentaje de la poblacion 2018')
plt.savefig('tortasCiudades.png')
#####################
plt.show()