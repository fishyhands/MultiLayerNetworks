# Adjecency matrix practice

import matplotlib.pyplot as plt
import networkx as nx 
import random as rand

graph = nx.Graph()
# Undirected graph

def links_finder(matrix):
    position = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                position.append([i+1,j+1])
    return position

def noofNodes(position):
    noofNodes = []
    for i in range(len(position)):
        for j in range(len(position[i])):
            if position[i][j] not in noofNodes:
                noofNodes.append(position[i][j])
    return noofNodes


matrix = ([0,1,1,0],
          [1,0,1,1],
          [1,1,0,0],
          [0,1,0,0]
)


links = links_finder(matrix)
nodes = noofNodes(links)
graph.add_nodes_from(nodes)
graph.add_edges_from(links)
nx.draw_networkx(graph,with_labels=True)
plt.show()