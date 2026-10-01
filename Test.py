import os

import networkx as nx
import matplotlib.pyplot as plt

# Define the nodes and edges with labels from the equations
nodes = ['0', '0b', '1', 'm', 'b']
edges = [
    ('0', '1', 'α(V1 - V0)'),
    ('0b', 'b', 'αb(μb)(Vb - V0b)'),
    ('1', 'm', 'βμπm maxπm (Vm - V1)'),
    ('1', 'b', 'βμβ maxπb (Vb - V1)'),
    ('m', '0b', 'maxπm4b(Vb - εm4b - Vm) + β(1 - πm4b)μ1cΠ1m(U - ε + V* - Vm)'),
    ('b', '0', 'γb(μb, Πb) + βμ1cΠ1b(U - εb + V* - Vb)')
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
for edge in edges:
    G.add_edge(edge[0], edge[1], label=edge[2])

# Define node positions in a circular layout
pos = nx.circular_layout(G)

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='lightblue')

# Draw the edges
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=25)

# Draw the labels for nodes
nx.draw_networkx_labels(G, pos, font_size=12)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()


#print(os.getcwd())