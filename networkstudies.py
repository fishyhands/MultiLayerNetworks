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

model.add_status("Susceptible")
model.add_status("Idea 1")
model.add_status("Idea 2")
model.add_status("Exposed both Ideas")
model.add_status("Susceptible again")



# cured and susceptible again probability: delta1/delta2
# spreading rate v1/delta1
#Note that in the proposed model, we assume that the chance of getting infected depends on the presence of infectious neighbors rather than the number of them.
# Compartment definition

# if in presence of 1 idea only, P(idea 1) = v1 or P(idea 2)= v2
# if in presence of both, P(idea 1) = alpha1 and P(idea 2)= beta2, where alpha and beta are factors of v1 and v2 respectively
v1 = 0.2
v2 = 0.1
alpha = rand.random()
beta = rand.uniform(alpha,0) # alpha is more dominant
exclusive = False

if exclusive == False: # exclusive influence is when alpha or beta = 0
    alpha1 = alpha* v1
    beta2 = beta * v2
else:
    alpha1 = alpha * v1
    beta2 = 0

#cured and susceptible again
delta1 = 0.3 
delta2 = 0.2

c_idea1 = cpm.NodeStochastic(v1, triggering_status= "Idea 1")
c_idea2 = cpm.NodeStochastic(v2,triggering_status = "Idea 2")
c_both1 = cpm.NodeStochastic(alpha1, triggering_status= "Idea 1")
c_both2 = cpm.NodeStochastic(beta2, triggering_status="Idea 2")
c_cure1 = cpm.NodeStochastic(delta1, triggering_status= "Susceptible again")
c_cure2 = cpm.NodeStochastic(delta2, triggering_status = "Susceptible again")

# Add rules

model.add_rule("Susceptible", "Idea 1", c_idea1)
model.add_rule("Susceptible", "Idea 2", c_idea2)


"""
Basic SIS Model

model = ep.SISModel(G)
cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.01)
cfg.add_model_parameter('lambda', 0.005)
cfg.add_model_parameter("fraction_infected", 0.05)
model.set_initial_status(cfg)


# Degree distribution and stuff
degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
dmax = max(degree_sequence)

# Figure size and Graphs
fig = plt.figure("Degree of a random graph", figsize=(8, 8))
axgrid = fig.add_gridspec(5, 4)
ax0 = fig.add_subplot(axgrid[0:3, :])
Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
pos = nx.spring_layout(Gcc, seed=10396953)
nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=20)
nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
ax0.set_title("Scale-Free Network G")
ax0.set_axis_off()
ax1 = fig.add_subplot(axgrid[3:, :2])
ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("Degree Distribution Plot (2000 nodes)")
ax1.set_ylabel("Degree")
ax1.set_xlabel("Node Count")
ax2 = fig.add_subplot(axgrid[3:, 2:])
ax2.bar(*np.unique(degree_sequence, return_counts=True))
ax2.set_title("Degree histogram")
ax2.set_xlabel("Degree")
ax2.set_ylabel("Node Count")
fig.tight_layout()
plt.show()



# Visualizing Results

iterations = model.iteration_bunch(200)
trends = model.build_trends(iterations)
viz = DiffusionTrend(model, trends)
viz.plot()

"""