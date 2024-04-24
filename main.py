# main.py
from graficador import NetworkAnalysis

# Ejemplo de uso
network = NetworkAnalysis()
network.add_nodes([1, 2, 3])
network.add_edges([(1, 2), (1, 3), (2, 3)])
network.visualize_graph()

print("Nodos:", network.get_nodes())
print("Aristas:", network.get_edges())

print("Número de nodos:", network.count_nodes())

print("Número de aristas:", network.count_edges())

shortest_path = network.shortest_path(1, 3)
print("Camino más corto entre 1 y 3:", shortest_path)

clustering_coefficient = network.clustering_coefficient()
print("Coeficiente de Clustering:", clustering_coefficient)