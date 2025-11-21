import random
import os
import math
from lector import leer_vrp
import time
import statistics

# ruta archivos
ruta_facil = "Facil.vrp"
ruta_medio = "Medio.vrp"
ruta_dificil = "Dificil.vrp"

capacidad, dimension, coords, demandas, dist = leer_vrp(ruta_dificil)

def solucion_inicial(capacidad, demandas):
    sol = []
    ruta_actual = [0]
    carga_actual = 0
    clientes = list(range(1, len(demandas)))
    random.shuffle(clientes)

    for nodo in clientes:
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

def exceso_capacidad(sol, capacidad, demandas):
    exceso = 0
    for ruta in sol:
        carga = sum(demandas[n] for n in ruta if n != 0)
        if carga > capacidad:
            exceso += (carga - capacidad)
    return exceso

def costo_ruta(ruta):
    c = 0
    for i in range(len(ruta) - 1):
        c += dist[ruta[i]][ruta[i+1]]
    return c

def costo(sol, capacidad, demandas, lam=1000):
    total = sum(costo_ruta(r) for r in sol)
    exceso = exceso_capacidad(sol, capacidad, demandas)
    return total + lam * exceso

def vecino(sol):
    nuevo = [r[:] for r in sol]
    rutas_validas = [i for i, r in enumerate(nuevo) if len(r) > 2]

    if len(rutas_validas) < 2:
        return nuevo

    v1, v2 = random.sample(rutas_validas, 2)
    i = random.randint(1, len(nuevo[v1]) - 2)
    j = random.randint(1, len(nuevo[v2]) - 2)

    nuevo[v1][i], nuevo[v2][j] = nuevo[v2][j], nuevo[v1][i]
    return nuevo


# ================================
#       BENCHMARK AUTOMÁTICO
# ================================

N = 10
resultados = []

for prueba in range(1, N + 1):

    print(f"\n========== PRUEBA {prueba} ==========")

    # parámetros SA
    alpha = 0.9999
    temp = 1000
    temp_min = 0.001
    max_iter = 150000
    i = 0

    sol = solucion_inicial(capacidad, demandas)
    costo_actual = costo(sol, capacidad, demandas)
    mejor = sol
    costo_mejor = costo_actual

    tiempo_inicio = time.time()

    while temp > temp_min and i < max_iter:
        s2 = vecino(sol)
        costo_vecino = costo(s2, capacidad, demandas)
        delta = costo_vecino - costo_actual

        if delta < 0 or random.random() < math.exp(-delta / temp):
            sol = s2
            costo_actual = costo_vecino

        if costo_actual < costo_mejor:
            mejor = sol
            costo_mejor = costo_actual

        temp *= alpha
        i += 1

    tiempo_fin = time.time()
    duracion = tiempo_fin - tiempo_inicio
    exceso = exceso_capacidad(mejor, capacidad, demandas)

    resultados.append((duracion, i, costo_mejor))

    print("\n--- Rutas finales ---")
    for idx, ruta in enumerate(mejor, start=1):
        cadena = " - ".join(str(n) for n in ruta)
        print(f"Camión {idx}: {cadena}")

    print(f"Tiempo: {duracion:} segundos")
    print(f"Iteraciones: {i}")
    print(f"Costo mejor solución: {costo_mejor}")
    print(f"Exceso: {exceso}")

# ==================================
#     RESUMEN ESTADÍSTICO
# ==================================

tiempos = [r[0] for r in resultados]
iters = [r[1] for r in resultados]
costos = [r[2] for r in resultados]

print("\n\n===== RESUMEN FINAL =====")
for idx, (t, it, c) in enumerate(resultados, start=1):
    print(f"{idx}) tiempo={t:}s  iter={it}  costo={c}")

print("\n--- Estadísticas ---")
print(f"Promedio costo: {statistics.mean(costos):}")
print(f"Desviación estándar costo: {statistics.stdev(costos):}")
print(f"Promedio tiempo: {statistics.mean(tiempos):}s")
print(f"Promedio iteraciones: {statistics.mean(iters):.0f}")
