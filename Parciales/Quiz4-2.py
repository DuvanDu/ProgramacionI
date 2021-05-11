import matplotlib.pyplot as plt
pieExplode = [0.2,0,0,0,0]
poblacion = [3967000, 675218, 2161000, 261905, 914552]
pieLabels = ['Los Angeles', 'Vancouver', 'Paris', 'Venecia', 'Cartagena']

acumulador = 0
for elemento in poblacion :
    acumulador += elemento
for i in range (len(pieLabels)):
    porcentaje = round(poblacion[i]/acumulador*7979675,2)
    pieLabels[i] += '-'+str(porcentaje) +'Poblacion'

plt.pie(poblacion,labels=pieLabels, 
        explode=pieExplode, 
        shadow= True, 
        startangle= 45)
#####################
plt.title('Poblacion de tus 5 ciudades favoritas')
plt.savefig('tortasPoblacion.png')
#####################
plt.show()