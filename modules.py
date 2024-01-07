# Import dependencies and packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx  
from networkx.utils import powerlaw_sequence
import random as rand
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
import ndlib.models.CompositeModel as gc
import ndlib.models.compartments as cpm
import ndlib.models.compartments.ConditionalComposition as cif

class network:
    def __init__(self) -> None:
        self.nodes = 5000
        self.edges = 2
        self.exponent = 3

    def createNetwork(self):
        sequence = nx.utils.powerlaw_sequence(5000,3) # 5000 nodes, exponent of 3
        G = nx.configuration_model(sequence,create_using= nx.barabasi_albert_graph)
        G=nx.Graph(G)
        G.remove_edges_from(G.selfloop_edges())
        return G
        #while any(degree < self.edges for node, degree in G.degree()): # minimum nodal degree of 2
           # G = nx.barabasi_albert_graph(self.nodes,self.edges)

    def showNetwork(self,createGraph):
        G = createGraph()
        plt.figure(figsize=(90,65))
        nx.draw(G, with_labels = False)
        min_degree = min(dict(G.degree()).values())
        plt.title("Barabasi-Albert Graph, minimum nodal degree = 2")
        plt.show()

    
        


class model:
    def __init__(self) -> None:
        pass