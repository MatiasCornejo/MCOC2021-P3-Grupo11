import networkx as nx 
import matplotlib.pyplot as plt
from networkx.algorithms import dijkstra_path
from networkx.algorithms import shortest_simple_paths

r= lambda f: 10 + f/120
v=r
z=r

s= lambda f: 14 + (3*f)/240
u=s
w=s
y=s

t= lambda f: 10 + f/240
x=t

#matriz OD

OD = {
      ("A","C") : 1100,
      ("A","D") : 1110,
      ("A","E") : 1020,
      ("B","C") : 1140,
      ("B","D") : 1160,
      ("C","E") : 1170,
      ("C","G") : 1180,
      ("D","C") : 350,
      ("D","E") : 1190,
      ("D","G") : 1200,
      }
#copia Matriz OD
OD_target = OD.copy()
list_OD =[["A","C"],["A","D"],["A","E"],["B","C"],["B","D"],["C","E"],["C","G"],["D","C"],["D","E"],["D","G"]]


G = nx.DiGraph()   #Graph asume bidireccionalidad en todos los arcos


G.add_node("A", pos=[-3,3])
G.add_node("B", pos=[-3,0])
G.add_node("C", pos=[0,0])
G.add_node("D", pos=[0,-3])
G.add_node("E", pos=[3,3])
G.add_node("G", pos=[3,0])



G.add_edge("A","B", fcosto=r,flujo=0,costo=0)
G.add_edge("A","C", fcosto=s,flujo=0,costo=0)
G.add_edge("B","C", fcosto=t,flujo=0,costo=0)
G.add_edge("D","C", fcosto=v,flujo=0,costo=0)
G.add_edge("B","D", fcosto=u,flujo=0,costo=0)
G.add_edge("D","G", fcosto=y,flujo=0,costo=0)
G.add_edge("C","G", fcosto=x,flujo=0,costo=0)
G.add_edge("C","E", fcosto=w,flujo=0,costo=0)
G.add_edge("G","E", fcosto=z,flujo=0,costo=0)

G.add_edge("A","B", fcosto=r,flujo=0,costoo="r")
G.add_edge("A","C", fcosto=s,flujo=0,costoo="s")
G.add_edge("B","C", fcosto=t,flujo=0,costoo="t")
G.add_edge("D","C", fcosto=v,flujo=0,costoo="v")
G.add_edge("B","D", fcosto=u,flujo=0,costoo="u")
G.add_edge("D","G", fcosto=y,flujo=0,costoo="y")
G.add_edge("C","G", fcosto=x,flujo=0,costoo="x")
G.add_edge("C","E", fcosto=w,flujo=0,costoo="w")
G.add_edge("G","E", fcosto=z,flujo=0,costoo="z")









def costo(ni,nf,attr):
    funcosto_arco = attr["fcosto"]
    flujo_arco = attr["flujo"]
    return funcosto_arco(flujo_arco)





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
                
            
            #print(f"{origen} - {destino } : demanda {demanda_actual} {path}")
            OD[key] -=1
        
            se_asigno_demanda = True
            
    if not se_asigno_demanda:
        break
                
#para ver costo

for ni,nf in G.edges:
    arco = G.edges[ni,nf]
    funcosto_arco = arco["fcosto"]
    flujo_arco = arco["flujo"]
    arco["costo"] = funcosto_arco(flujo_arco)

    

for z in list_OD:
    d=z[0]
    dd=z[1]

    ppath = shortest_simple_paths(G,d,dd,weight=costo)
    for x in ppath:
        suma=0
        l=len(x)
        #print(x)
        a=0
        b=1
        
        while l>1:
            arco = G.edges[x[a],x[b]]
            funcosto_arco = arco["fcosto"]
            flujo_arco = arco["flujo"]
            arco["costo"] = funcosto_arco(flujo_arco)
            a+=1
            b+=1
            l-=1
            suma+=arco["costo"]
            
            if l<=1:
                print("par OD :",d,dd,"costo =",suma)
                suma=0    
    print("-----------------------------------------------")   

plt.figure(1)
ax1 = plt.subplot(111)
pos = nx.get_node_attributes(G,"pos")
nx.draw(G,pos,with_labels=True,font_weight="bold")
labels = nx.get_edge_attributes(G,"flujo")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.suptitle(f"flujo")



plt.figure(2)
ax1 = plt.subplot(111)
pos = nx.get_node_attributes(G,"pos")
nx.draw(G,pos,with_labels=True,font_weight="bold")
labels = nx.get_edge_attributes(G,"costo")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.suptitle(f"costo")



#plt.figure(2)
#ax1 = plt.subplot(111)
plt.show()