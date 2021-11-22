
import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gps
import networkx as nx

ox.config(use_cache=True, log_console=True)

N = -33.3637
S = -33.56
E = -70.5240
O = -70.80

G = ox.graph_from_bbox(N,S,E,O,
                       network_type="drive",
                       clean_periphery=True,
                       custom_filter= '["highway"~"construction|primary|secondar|ymotorway|"]'
                       )
                       #|construction primary|secondar|ymotorway|
                       
  

nx.write_gpickle(G,"MiGrafo.gpickle")

print("jiji")