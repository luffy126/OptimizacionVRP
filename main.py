print("Hello, World!")

clientes = [0, 15, 10, 18, 12, 8, 14, 9] # clientes y demanda
vehiculos = [35, 30, 30] # vehiculos y capacidad
distancia_entre_clientes = [
    [0, 4, 6, 7, 6, 10, 9, 8],
    [4, 0, 3, 4, 5, 7, 5, 5],
    [6, 3, 0, 5, 3, 4, 4, 2],
    [7, 4, 5, 0, 8, 7, 2, 7],
    [6, 5, 3, 8, 0, 5, 8, 2],
    [10, 7, 4, 7, 5, 0, 5, 3],
    [9, 5, 4, 2, 8, 5, 0, 6],
    [8, 5, 2, 7, 2, 3, 6, 0]
] # matriz de distancias, simetrica (numero = distancia entre cliente i y j)

solucion_inicial = [0, 1, 4, 2, 3, 7, 5, 6] # solucion inicial para ir explorando
#mejor_solucion 

# parametros

alpha = 0.996
temp_inicial = 1000
temp = temp_inicial
temp_minima = 0.01
iteraciones_max = 30000
i = 0

while (temp > temp_minima and i < iteraciones_max):
    temp = temp * alpha
    print(temp)
    i += 1
    print (i)
