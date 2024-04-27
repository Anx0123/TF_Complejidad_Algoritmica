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
        # Ajustar grafico
        pos = nx.spring_layout(self.G, k=500.0)  
        plt.figure(figsize=(50, 50))  # Ajusta el tamaño de la figura
        nx.draw(self.G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12)
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


            # CRITERIOS DE CONEXIONES 
            # Criterio 1: Videojuegos favoritos compartidos
            shared_games = set(user1["videojuegosFavoritos"]) & set(user2["videojuegosFavoritos"])
            if len(shared_games) >= 3:  # Comparten al menos tres videojuegos favoritos
                self.G.add_edge(user1["id"], user2["id"])

            # Criterio 2: Géneros de juegos comunes
            shared_genres = set(user1["generosPreferidos"]) & set(user2["generosPreferidos"])
            if len(shared_genres) >= 3:  # Comparten al menos tres géneros de juegos preferidos
                self.G.add_edge(user1["id"], user2["id"])

            # Criterio 3: Plataformas de juego compartidas
            shared_platforms = set(user1["plataformasJuego"]) & set(user2["plataformasJuego"])
            if len(shared_platforms) >= 2:  # Comparten al menos dos plataformas de juego favoritas
                self.G.add_edge(user1["id"], user2["id"])
            
            # Criterio extra: Comparten al menos un juego y una misma plataforma
            shared_games = set(user1["videojuegosFavoritos"]) & set(user2["videojuegosFavoritos"])
            shared_platforms = set(user1["plataformasJuego"]) & set(user2["plataformasJuego"])
            if len(shared_games) > 0 and len(shared_platforms) > 0:
                self.G.add_edge(user1["id"], user2["id"])
