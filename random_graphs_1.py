import networkx as nx
import matplotlib.pyplot as plt

import numpy as np

# Simple code to create a random graph of any type.
G = nx.Graph()


r1 = [np.random.randint(1,10) for r in range(0,10)]
print(r1)

r2 = [np.random.randint(1,10) for r in range(0,10)]
print(r2)

zip_r = list(zip(r1,r2))

print(zip_r)
print(len(zip_r))


G.add_edges_from(zip_r)
graph_verticies = G.number_of_nodes()

nx.draw(G, with_labels=True)


plt.title(f'Random Graph on {graph_verticies} Verticies')
plt.savefig('random_graph.png', bbox_inches='tight')




