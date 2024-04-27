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

