# main.py
from TF_Complejidad_Algoritmica.graficador import NetworkAnalysis

import json
# Leer los datos del JSON
with open('dataset.json', 'r') as file:
    usuarios = json.load(file)

network = NetworkAnalysis()

# Construir las aristas del grafo basado en los criterios definidos
network.build_graph_from_criteria(usuarios)
network.visualize_graph()

print("Nodos:", network.get_nodes())
print("Aristas:", network.get_edges())