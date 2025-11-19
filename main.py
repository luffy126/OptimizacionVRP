import random
import os
import math
from lector import leer_vrp

print(os.listdir())

# ruta archivos
ruta_facil = "Facil.vrp"
ruta_medio = "Medio.vrp"
ruta_dificil = "Dificil.vrp"

capacidad, dimension, coords, demandas, dist = leer_vrp(ruta_medio)

def solucion_inicial(capacidad, demandas):
    sol = []
    ruta_actual = [0]  
    carga_actual = 0
    clientes = list(range(1, len(demandas)))
    random.shuffle(clientes)

    for nodo in range(1, len(demandas)):
        demanda = demandas[nodo]

        if carga_actual + demanda > capacidad:
            ruta_actual.append(0)
            sol.append(ruta_actual)

            ruta_actual = [0]      
            carga_actual = 0

        ruta_actual.append(nodo)
        carga_actual += demanda

    ruta_actual.append(0)
    sol.append(ruta_actual)

    return sol

# imprimir para verificar
print("Capacidad:", capacidad)
print("Dimension:", dimension)
print("Primeras coordenadas:", coords[:5])
print("Primeras demandas:", demandas[:10])
print("Distancia 1→2:", dist[0][1])

# hay exceso?
def exceso_capacidad(sol, capacidad, demandas):
    exceso = 0
    for ruta in sol:
        carga = sum(demandas[n] for n in ruta if n != 0)
        if carga > capacidad:
            exceso += (carga - capacidad)
    # print(exceso)
    return exceso

# calcular costo
def costo_ruta(ruta):
    c = 0
    for i in range(len(ruta) - 1):
        c += dist[ruta[i]][ruta[i+1]]
    return c

def costo(sol, capacidad, demandas, lam = 1000):
    total = 0
    for r in sol:
        total += costo_ruta(r)

    exceso = exceso_capacidad(sol, capacidad, demandas)
    total += lam * exceso
    return total

# solución inicial
sol = solucion_inicial(capacidad, demandas)

# swap
def vecino(sol):
    nuevo = [r[:] for r in sol]
    num_rutas = len(nuevo)

    v1 = random.randint(0, num_rutas - 1)
    v2 = random.randint(0, num_rutas - 1)

    if len(nuevo[v1]) > 2 and len(nuevo[v2]) > 2:
        i = random.randint(1, len(nuevo[v1]) - 2)
        j = random.randint(1, len(nuevo[v2]) - 2)

        nuevo[v1][i], nuevo[v2][j] = nuevo[v2][j], nuevo[v1][i]

    return nuevo

# parametros
alpha = 0.9999
temp = 1000
temp_min = 0.001
max_iter = 100000
i = 0

mejor = sol
costo_mejor = costo(sol, capacidad, demandas)

# busqueda
while temp > temp_min and i < max_iter:
    s2 = vecino(sol)

    delta = costo(s2, capacidad, demandas) - costo(sol, capacidad, demandas)

    # print(f"iteración {i}: costo actual {costo(sol)}, costo vecino {costo(s2)}, temp {temp:.4f}")

    if delta < 0 or random.random() < math.exp(-delta/temp):
        sol = s2

    if costo(sol, capacidad, demandas) < costo_mejor:
        mejor = sol
        costo_mejor = costo(sol, capacidad, demandas)

    temp *= alpha
    i += 1

print("Mejor solución:", mejor)
print("Costo:", costo_mejor)
