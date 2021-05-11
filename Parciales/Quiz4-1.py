import matplotlib.pyplot as plt
pieExplode = [0,0,0,0,0.2]
precioSnacks = [500, 400, 500, 800, 1000]
pieLabels = ['Chokis', 'Quipitos', 'Masmelos', 'Gol', 'Oreo']

plt.pie(precioSnacks,labels=pieLabels, 
        explode=pieExplode, 
        shadow= True, 
        startangle= 45)
#####################
plt.title('Top 5 snacks favoritos')
plt.savefig('tortasSnacks.png')
#####################
plt.show()
