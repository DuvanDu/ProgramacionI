import matplotlib.pyplot as plt
def agregarElementos(preguntaAlimento, preguntaPrecio):
    lista1 = []
    lista2 = []
    for i in range(8):
        print (f'ingresando dato {i+1} de 8')
        lista1.append(input(preguntaAlimento))
        lista2.append(int(input(preguntaPrecio)))
    return lista1, lista2

preguntaAlimento = 'ingrese su alimento favorito: '
preguntaPrecio = 'ingrese el precio del snack: '
lista1, lista2 = agregarElementos(preguntaAlimento,preguntaPrecio)
print(lista1, lista2)
plt.bar(lista1, lista2, width =0.9, color = 'm')
###############
#titulo
plt.title('Top 8 alimentos y precios')
plt.xlabel('Alimentos')
plt.ylabel('Precios')
plt.savefig('graficoAlimentos.png')
###############
plt.show()