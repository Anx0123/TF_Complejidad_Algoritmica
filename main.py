# main.py
from graficador import NetworkAnalysis

# Ejemplo de uso

import json
# Leer los datos del JSON
with open('dataset.json', 'r') as file:
    usuarios = json.load(file)

#primeros_tres_usuarios = usuarios[:3]


network = NetworkAnalysis()
# Agregar los nodos al grafo utilizando los ID de los tres primeros usuarios
#network.add_nodes([usuario["id"] for usuario in primeros_tres_usuarios])

# Construir las aristas del grafo basado en los criterios definidos
network.build_graph_from_criteria(usuarios)
network.visualize_graph()

print("Nodos:", network.get_nodes())
print("Aristas:", network.get_edges())

print("Número de nodos:", network.count_nodes())

print("Número de aristas:", network.count_edges())

shortest_path = network.shortest_path(1, 3)
print("Camino más corto entre 1 y 3:", shortest_path)

clustering_coefficient = network.clustering_coefficient()
print("Coeficiente de Clustering:", clustering_coefficient)