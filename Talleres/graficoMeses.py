#Aqui explicaremos como hacer un gráfico de barras
import matplotlib.pyplot as plt 
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
ingresos = [500,100,200,100,150,500]
plt.bar(meses, ingresos, width =0.9, color = 'c')
###############
#titulo
plt.title('Ingresos Mensuales')
plt.xlabel('Meses')
plt.ylabel('Nivel de Ingresos en Miles')
plt.savefig('graficoIngresos.png')
###############
plt.show()