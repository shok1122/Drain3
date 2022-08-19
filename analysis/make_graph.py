import json
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

json_file = open("/tmp/drain.json", "r")
automaton = json.load(json_file)
json_file.close()

G = nx.DiGraph()

ratio_max = 0
ratio_min = 1

for k1 in automaton:
    G.add_node(k1)
    for k2 in automaton[k1]:
        if not G.has_node(k2):
            G.add_node(k2)
        ratio = automaton[k1][k2]["ratio"]
        if ratio > ratio_max:
            ratio_max = ratio
        if ratio < ratio_min:
            ratio_min = ratio
        G.add_edge(k1, k2, weight=ratio)

#pos = graphviz_layout(G, prog="dot")
pos = nx.spring_layout(G, k=0.8)

#nx.draw(G, with_labels=True, pos=pos)
#plt.savefig("/tmp/drain.png", format="PNG")

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="Monospace")
nx.draw_networkx_edges(G, pos, alpha=1.0, edge_color="darkgrey", width=[d['weight'] for (u,v,d) in G.edges(data=True)])

plt.savefig("/tmp/drain.png", format="PNG")

print(ratio_max)
print(ratio_min)

