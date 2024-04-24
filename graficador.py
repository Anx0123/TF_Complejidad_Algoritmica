import networkx as nx
import matplotlib.pyplot as plt

class NetworkAnalysis:
    def __init__(self):
        self.G = nx.Graph()
    
    def add_nodes(self, nodes):
        self.G.add_nodes_from(nodes)
    
    def add_edges(self, edges):
        self.G.add_edges_from(edges)
    
    def visualize_graph(self):
        nx.draw(self.G, with_labels=True)
        plt.show()
    
    def get_nodes(self):
        return self.G.nodes()
    
    def get_edges(self):
        return self.G.edges()
    
    def count_nodes(self):
        return self.G.number_of_nodes()
    
    def count_edges(self):
        return self.G.number_of_edges()
    
    def shortest_path(self, source, target):
        return nx.shortest_path(self.G, source=source, target=target)
    
    def clustering_coefficient(self):
        return nx.clustering(self.G)
    
    def write_to_file(self, filename):
        nx.write_gexf(self.G, filename)
    
    def read_from_file(self, filename):
        self.G = nx.read_gexf(filename)

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
