# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:26:39 2021

@author: Matias
"""
import numpy as np
from math import sqrt
import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gps
import networkx as nx
from networkx.algorithms import astar_path, all_simple_paths, all_shortest_paths, dijkstra_path


def fun_costo(n1, n2, attr_arco):
    print(n1,n2)
    usar_arco_numero = 0

    if "name" in attr_arco[usar_arco_numero]:
        name = str(attr_arco[usar_arco_numero]["name"])
    else:
        name = ""

    length = attr_arco[usar_arco_numero]["length"]

    stree_type = attr_arco[usar_arco_numero]["highway"]
    N_pistas=attr_arco[usar_arco_numero]
    p=1 #modelar funcion de p , parece que hay un lanes que no existe
    
    #print(p)
    l=6
    f=0 #implemntar funcion de flujo (excel)
    q=f/5400
    zona_origen = 213
    zona_destino = 146
     
    if name.find("Autopista Central")>=0:
        length*=1000
    if name.find("Diagonal Oriente")>=0:
        length*=1000    
    if stree_type == "motorway":
        vel = 25
        u = 5
    elif stree_type == "primary":
        vel = 15
        u = 3
    elif stree_type == "secondary":
        vel = 15
        u = 3

    else:
        vel=8
        u = 2
    
    a1=0
    a2=0
    
    
    #for line in open("mod.csv"):
     #   sl=line.split(',')
      #  o = int(sl[0])
       # d = int(sl[1]) 
        
    
        #if o==zona_origen :
         #   print(o)
          #  a1+=1
           # break
        
        
    #print("es")
    #print(a1)
    
    
 #funcion para hacer funcionar wardrop
   
'''


while True:
    se_asigno_demanda = False
    for key in OD:
        
        
        origen = key[0]
        destino = key[1]
        demanda_actual = OD[key]
        demanda_objetivo = OD_target[key]
        
        
        if demanda_actual > 0:
            
            path = dijkstra_path(G,origen,destino,weight=costo)
            
            Nparadas = len(path)
            
            for i_parada in range(Nparadas-1):
                o = path[i_parada]
                d = path[i_parada+1]
                flujo_antes = G.edges[o,d]["flujo"]
                
                G.edges[o,d]["flujo"]+=1
                
            
            print(f"{origen} - {destino } : demanda {demanda_actual} {path}")
            OD[key] -=1
        
            se_asigno_demanda = True
            
    if not se_asigno_demanda:
        break
    
'''
            
        
            
    q=f/5400
    tiempo = length/vel
    c=sqrt(((10*q-u*p)**2)+(q/9))
    cc=(10*q)-(u*p)+c
    costo = tiempo+(5-u)*12+(900/(u*p))*cc
    print(costo)
    return costo

a=0
   
ox.config(use_cache=True, log_console=True)


G = nx.read_gpickle("MiGrafo.gpickle")
zonas_gdf = gps.read_file("eod.json")
gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
fig, ax = plt.subplots(1, 1)


street_centroids = gdf_edges.centroid
gdf_edges[gdf_edges.highway == "primary"].plot(ax=ax, color="yellow")

gdf_edges[gdf_edges.highway == "secondary"].plot(ax=ax, color="green")

gdf_edges[gdf_edges.highway == "motorway"].plot(ax=ax, color="blue")
gdf_edges[gdf_edges.highway == "construction"].plot(ax=ax, color="red")

zona_origen = 213
zona_destino = 146

#nodo_origen = 2744834665
#nodo_destino = 1225556707

#for ni,nf,indice in G.edges:
   # print(f"ni={ni} nf={nf} attr={G.edges[ni,nf,indice]}")

#lo que hare a continuacion es encontrar el nodo mas cercano posible a la zona de origen y destino 


t=zonas_gdf[zonas_gdf.ID == zona_origen].representative_point()
cx_zona_origen,cy_zona_origen =float(t.x),float(t.y)

distancia_minima = np.infty
for i, node in enumerate(G.nodes):
    cx_nodo = G.nodes[node]["x"]
    cy_nodo = G.nodes[node]["y"]
    dist_nodo_actual = np.sqrt((cx_nodo - cx_zona_origen)**2 + (cy_nodo - cy_zona_origen)**2)
    a+=1
    
    if dist_nodo_actual < distancia_minima:
        distancia_minima = dist_nodo_actual
        nodo_origen = node
        
t=zonas_gdf[zonas_gdf.ID == zona_destino].representative_point()
cx_zona_destino,cy_zona_destino =float(t.x),float(t.y)

distancia_minima = np.infty
for i, node in enumerate(G.nodes):
    cx_nodo = G.nodes[node]["x"]
    cy_nodo = G.nodes[node]["y"]
    dist_nodo_actual = np.sqrt((cx_nodo - cx_zona_destino)**2 + (cy_nodo - cy_zona_destino)**2)
    if dist_nodo_actual < distancia_minima:
        distancia_minima = dist_nodo_actual
        nodo_destino = node
   


    
zonas_gdf[zonas_gdf.ID == zona_origen].plot(ax=ax, color="#9D9D9D")
zonas_gdf[zonas_gdf.ID == zona_destino].plot(ax=ax, color="#9D9D9D")

# ciclo para ver los nodos del mapa

# for i, node in enumerate(G.nodes):
#    ax.annotate(node,xy=(G.nodes[node]["x"],G.nodes[node]["y"]))

ax.annotate(nodo_origen, xy=(
    G.nodes[nodo_origen]["x"], G.nodes[nodo_origen]["y"]))
ax.annotate(nodo_destino, xy=(
    G.nodes[nodo_destino]["x"], G.nodes[nodo_destino]["y"]))


take_path = dijkstra_path(G, nodo_origen, nodo_destino, weight=fun_costo)

Nparadas = len(take_path)

ss=0




while True:
    se_asigno_demanda = False
    for key in OD:
        
        
        origen = key[0]
        destino = key[1]
        demanda_actual = OD[key]
        demanda_objetivo = OD_target[key]
        
        
        if demanda_actual > 0:
            
            path = dijkstra_path(G,origen,destino,weight=costo)
            
            Nparadas = len(path)
            
            for i_parada in range(Nparadas-1):
                o = path[i_parada]
                d = path[i_parada+1]
                flujo_antes = G.edges[o,d]["flujo"]
                
                G.edges[o,d]["flujo"]+=1
                
            
            print(f"{origen} - {destino } : demanda {demanda_actual} {path}")
            OD[key] -=1
        
            se_asigno_demanda = True
            
    if not se_asigno_demanda:
        break
for i_parada in range(Nparadas-1):
    n1 = take_path[i_parada]
    n2 = take_path[i_parada+1]
    
    #n3=fun_costo(n1,n2)
    tomar_arco = 0
    
    
  

    arco = G.edges[n1, n2, tomar_arco]
    
    if "name" in arco:
        nombre = arco["name"]
        #print(arco)
    else:
        nombre = ""
    
    #print(f"uniendo{n1} con{n2} sigue por {nombre}")
    xx = [G.nodes[n1]["x"], G.nodes[n2]["x"]]
    yy = [G.nodes[n1]["y"], G.nodes[n2]["y"]]
  
    ax.plot(xx, yy, color="#9D9D9D", linewidth=3)
plt.show()
