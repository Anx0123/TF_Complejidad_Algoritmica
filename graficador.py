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
    
    def build_graph_from_criteria(self, users):
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            user1 = users[i]
            user2 = users[j]
            
            # Criterio 1: Videojuegos favoritos compartidos
            shared_games = set(user1["Videojuegos Favoritos"]) & set(user2["Videojuegos Favoritos"])
            if len(shared_games) > 0:
                self.G.add_edge(user1["ID"], user2["ID"])
            
            # Criterio 2: Géneros de juegos comunes
            shared_genres = set(user1["Géneros Preferidos"]) & set(user2["Géneros Preferidos"])
            if len(shared_genres) >= 2:  # Comparten al menos dos géneros de juegos
                self.G.add_edge(user1["ID"], user2["ID"])
            
            # Criterio 3: Plataformas de juego compartidas
            shared_platforms = set(user1["Plataformas de Juego"]) & set(user2["Plataformas de Juego"])
            if len(shared_platforms) > 0:
                self.G.add_edge(user1["ID"], user2["ID"])

<<<<<<< HEAD
# Ejemplo de uso
network = NetworkAnalysis()
network.add_nodes([1, 2, 3])
network.add_edges([(1, 2), (1, 3), (2, 3)])
network.build_graph_from_criteria(users)
network.visualize_graph()

print("Nodos:", network.get_nodes())
print("Aristas:", network.get_edges())
print("Número de nodos:", network.count_nodes())
print("Número de aristas:", network.count_edges())

shortest_path = network.shortest_path(1, 3)
print("Camino más corto entre 1 y 3:", shortest_path)

clustering_coefficient = network.clustering_coefficient()
print("Coeficiente de Clustering:", clustering_coefficient)
=======
>>>>>>> main
