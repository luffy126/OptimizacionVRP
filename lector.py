import math

def leer_vrp(path):
    capacidad = None
    dimension = None
    coords = []
    demands = []
    leyendo_coords = False
    leyendo_demands = False

    with open(path, 'r') as f:
        for linea in f:
            linea = linea.strip()

            # Leer parámetros principales
            if linea.startswith("CAPACITY"):
                capacidad = int(linea.split(":")[1])
            elif linea.startswith("DIMENSION"):
                dimension = int(linea.split(":")[1])
            elif linea.startswith("NODE_COORD_SECTION"):
                leyendo_coords = True
                continue
            elif linea.startswith("DEMAND_SECTION"):
                leyendo_coords = False
                leyendo_demands = True
                continue
            elif linea.startswith("DEPOT_SECTION"):
                leyendo_coords = False
                leyendo_demands = False
                continue

            # Leer coordenadas
            if leyendo_coords:
                parts = linea.split()
                if len(parts) >= 3:
                    _, x, y = parts
                    coords.append((float(x), float(y)))

            # Leer demandas
            elif leyendo_demands:
                parts = linea.split()
                if len(parts) == 2:
                    _, d = parts
                    demands.append(int(d))

    # Construir matriz de distancias
    dist = [[0]*dimension for _ in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            if i != j:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                dist[i][j] = int(round(math.sqrt((x1-x2)**2 + (y1-y2)**2)))

    # Si no existen demandas en el archivo
    if len(demands) == 0:
        demands = [0] + [1]*(dimension - 1)

    return capacidad, dimension, coords, demands, dist
