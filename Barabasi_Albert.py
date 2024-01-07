# Import dependencies and packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx  
import ndlib.models.CompositeModel as gc
import ndlib.models.compartments as cpm
import ndlib.models.compartments.ConditionalComposition as cif
import powerlaw as pl

mpl.use('TkAgg')

## Create Graph
nodes = 500
edges = 2

G = nx.barabasi_albert_graph(nodes,edges)
while any(degree < 2 for node, degree in G.degree()): # minimum nodal degree of 2
    G = nx.barabasi_albert_graph(nodes,edges)
deg = dict(nx.degree(G))
deg = list(deg.values())
fit = pl.Fit(deg, discrete=True)
fit.distribution_compare('power_law', 'lognormal')


"""
plt.figure(figsize=(90,65))
nx.draw(G, with_labels = False)
plt.title("Scale-Free Graph, minimum nodal degree = 2")
plt.show()
min_degree = min(dict(G.degree()).values())
print(min_degree)
## Model configuration
model = gc.CompositeModel(G)

model.add_status("S")
model.add_status("1")
model.add_status("2")
model.add_status("B")

v1 = 0.6 #probability of idea 1
v2 = 0.5 #probability of idea 2

alpha = 0.15 #influential factor if both ideas are present
beta = 0.35 #influential factor if both ideas are present

lamb1 = 0.3 #spreading rate of idea 1
lamb2  = 0.25 #spreading rate of idea 2

del1 = v1/lamb1 #recovery rate idea 1
del2 = v2/lamb2 #recovery rate idea 2

exclusive = False

if exclusive == False: # exclusive influence is when alpha or beta = 0
    alpha1 = alpha* v1
    beta2 = beta * v2
else:
    alpha1 = alpha * v1
    beta2 = 0

c_recover1 = cpm.NodeStochastic(del1, triggering_status= "S")
c_recover2 = cpm.NodeStochastic(del2, triggering_status= "S")

c_1Both =  cpm.EdgeStochastic(alpha1, triggering_status= "1") 
c_2Both = cpm.EdgeStochastic(beta2, triggering_status= "2")

c_idea1Only = cpm.EdgeStochastic(v1, triggering_status= "1")
c_idea2Only = cpm.EdgeStochastic(v2, triggering_status = "2")

neighbor1 = cpm.NodeStochastic(1,"1") #check if at least 1 neighbor is infected with idea1
neighbor2 = cpm.NodeStochastic(1,"2")   #check if at least 1 neighbor is infected with idea2
neighborBoth = cpm.NodeStochastic(1, triggering_status="B") 


check2T = cif.ConditionalComposition(neighbor2,neighborBoth,c_idea1Only) #is the node neighbor infected with 2 and 1?
check2F = cif.ConditionalComposition(neighbor2,c_idea2Only,c_recover1) # is the node neighbor infected with 2 only? if False, the node remains Susceptible
check1 = cif.ConditionalComposition(neighbor1,check2T,check2F) #is the node neighbor infected with 1?

model.add_rule("B","1",c_1Both)
model.add_rule("B","2",c_2Both)
model.add_rule("S","1",check1)
model.add_rule("S","2",check1)
model.add_rule("S","B",check1)
model.add_rule("1","S",c_recover1)
model.add_rule("2","S",c_recover2)
"""