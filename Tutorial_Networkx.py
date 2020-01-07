import networkx as nx
nx.to_networkx_graph()
nx.draw_networkx_edge_labels()
nx.draw_networkx_labels()
G = nx.Graph()
nx.draw()

print("G.degree:"+str(G.degree))
G.add_node(1) #添加一个节点
print("G.degree:"+str(G.degree))
G.add_nodes_from([2,3])#add node list
print("G.degree:"+str(G.degree))
H = nx.path_graph(20)#线性连接点的路径图
print("H:"+str(H))
G.add_nodes_from(H)
print("G.degree:"+str(G.degree))
print("G.edges:"+str(G.edges))
G.add_node(H)
print("G.degree:"+str(G.degree))
print("G.edges:"+str(G.edges))
G.add_edge(1,2)#单独增加一条边
print("G.edges:"+str(G.edges))
G.add_edges_from([(1,2),(1,3)])
print("G.edges:"+str(G.edges))
print("G.degree:"+str(G.degree))
print("G.adg:"+str(G.adj))
print("G.name:"+str(G.name))

G.add_edges_from(H.edges)
print("H.edges:"+str(H.edges))
print("H.degree:"+str(H.degree))
G.clear()
G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam")
G.add_nodes_from("spam")
G.add_edge(3,'m')
list(G.edges)
print("G.edges"+str(G.edges))
print(list(G.edges))

G2 = nx.DiGraph(G)
print("G2.degree:"+list(G2.degree))
print("G2.edges"+list(G2.edges))
print("G2.nodes"+list(G2.adg))
print()
edgelist= [(0,1),(1,2),(2,3)]
H = nx.Graph(edgelist)
