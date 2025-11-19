import random
import math

clientes = [0, 15, 10, 18, 12, 8, 14, 9] # clientes con su demanda
vehiculos = [35, 30, 30] # capacidad de los vehículos

dist = [ # matriz de distancias
    [0, 4, 6, 7, 6, 10, 9, 8],
    [4, 0, 3, 4, 5, 7, 5, 5],
    [6, 3, 0, 5, 3, 4, 4, 2],
    [7, 4, 5, 0, 8, 7, 2, 7],
    [6, 5, 3, 8, 0, 5, 8, 2],
    [10, 7, 4, 7, 5, 0, 5, 3],
    [9, 5, 4, 2, 8, 5, 0, 6],
    [8, 5, 2, 7, 2, 3, 6, 0]
]

# calcular costo
def costo_ruta(ruta):
    c = 0
    for i in range(len(ruta) - 1):
        c += dist[ruta[i]][ruta[i+1]]
    return c

def costo(sol):
    total = 0
    for r in sol:
        total += costo_ruta(r)
    return total

# solución inicial
sol = [
    [0, 1, 4, 0],
    [0, 2, 7, 0],
    [0, 3, 5, 6, 0]
]

# swap
def vecino(sol):
    nuevo = [r[:] for r in sol]
    v1 = random.randint(0,2)
    v2 = random.randint(0,2)

    if len(nuevo[v1]) > 2 and len(nuevo[v2]) > 2:
        i = random.randint(1, len(nuevo[v1])-2)
        j = random.randint(1, len(nuevo[v2])-2)
        nuevo[v1][i], nuevo[v2][j] = nuevo[v2][j], nuevo[v1][i]

    return nuevo

# parametros
alpha = 0.999
temp = 1000
temp_min = 0.01
max_iter = 30000
i = 0

mejor = sol
costo_mejor = costo(sol)

# busqueda
while temp > temp_min and i < max_iter:
    s2 = vecino(sol)

    delta = costo(s2) - costo(sol)

    print(f"iteración {i}: costo actual {costo(sol)}, costo vecino {costo(s2)}, temp {temp:.4f}")

    if delta < 0 or random.random() < math.exp(-delta/temp):
        sol = s2

    if costo(sol) < costo_mejor:
        mejor = sol
        costo_mejor = costo(sol)

    temp *= alpha
    i += 1

print("Mejor solución:", mejor)
print("Costo:", costo_mejor)
