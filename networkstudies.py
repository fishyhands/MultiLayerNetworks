# Import dependencies and packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx  
import random as rand
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
import ndlib.models.CompositeModel as gc
import ndlib.models.compartments as cpm
import ndlib.models.compartments.ConditionalComposition as cif
mpl.use('TkAgg')


## Create Graph
nodes = 5000
edges = 2

G = nx.barabasi_albert_graph(nodes, edges)
while any(degree < 2 for node, degree in G.degree()): # minimum nodal degree of 2
    G = nx.barabasi_albert_graph(nodes, edges)

nx.draw(G, with_labels = False)
plt.title("Scale-Free Graph, minimum nodal degree = 2")
plt.show()


## Model creation
model = gc.CompositeModel(G)

model.add_status("S")
model.add_status("1")
model.add_status("2")
model.add_status("C")




# cured and susceptible again probability: delta1/delta2
# spreading rate v1/delta1
#Note that in the proposed model, we assume that the chance of getting infected depends on the presence of infectious neighbors rather than the number of them.
# Compartment definition

# if in presence of 1 idea only, P(idea 1) = v1 or P(idea 2)= v2
# if in presence of both, P(idea 1) = alpha1 and P(idea 2)= beta2, where alpha and beta are factors of v1 and v2 respectively
v1 = 0.6
v2 = 0.5

alpha = 0.15
beta = 0.35

lamb1 = 0.3
lamb2  = 0.25

del1 = v1/lamb1
del2 = v2/lamb2

exclusive = False

if exclusive == False: # exclusive influence is when alpha or beta = 0
    alpha1 = alpha* v1
    beta2 = beta * v2
else:
    alpha1 = alpha * v1
    beta2 = 0

c_idea1 = cpm.NodeStochastic(v1, triggering_status= "1")
c_idea2 = cpm.NodeStochastic(v2,triggering_status = "2")
c_both = cpm.NodeStochastic()




model.add_rule("S", "1", c_idea1)
model.add_rule("S", "2", c_idea2)


