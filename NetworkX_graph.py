# Patient AI 


#Importing requirements libraries to convert data into Graph
import json
import networkx as nx
import matplotlib.pyplot as plt

# Load JSON files
with open(r"c:\Users\USER\Downloads\patients_550.json", "r") as f:
    patients = json.load(f)

with open(r"c:\Users\USER\Downloads\diseases_35.json", "r") as f: 
    diseases = json.load(f)

with open(r"c:\Users\USER\Downloads\edges_corrected_100.json", "r") as f:
    edges = json.load(f)

# Create a NetworkX graph
G = nx.Graph()

# Add patients as nodes
for patient in patients:
    G.add_node(patient["_key"], label="Patient", name=patient.get("name", "Unknown"))

# Add diseases as nodes
for disease in diseases:
    G.add_node(disease["_key"], label="Disease", name=disease["name"])

# Add edges (relations between patients and diseases)
for edge in edges:
    G.add_edge(edge["_from"].split("/")[-1], edge["_to"].split("/")[-1], relation=edge["relation"])

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)  # Positioning
node_colors = ["lightblue" if G.nodes[n]["label"] == "Patient" else "lightcoral" for n in G.nodes]

nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color="gray", node_size=2000, font_size=8)
edge_labels = {(u, v): G[u][v]['relation'] for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

plt.title("Patient-Disease Relationship Graph")
plt.show()
