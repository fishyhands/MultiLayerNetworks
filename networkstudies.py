import matplotlib.pyplot as plt
import networkx as nx 

def add_Nodes(matrix):
    position = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                position.append([i,j])
    return position


matrix = ([0,1,1,0],
          [1,0,1,1],
          [1,1,0,0],
          [0,1,0,0]
)

print(add_Nodes(matrix))