import networkx as nx 
import matplotlib.pyplot as plt 


def chk_existence(G,d):
	f=0
	for each in H.nodes():
		if H.degree(each)<=d:
			f=1
			break
	return f

def find_node(H,it):
	setn=[]
	for each in H.nodes():
		if H.degree(each)<=it:
			setn.append(each)
	return setn

#implementing k shell decomposition to find cores of network
#given a graph we say a subgraph is n-core if every node in subgraph has degree>=n
G=nx.Graph()
edges=[(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)]
G.add_edges_from(edges)
H=G.copy()
i=1
tmp=[]
b=[]
while(1):
	flag=chk_existence(G,i)
	if flag==0:
		i+=1
		b.append(tmp)
		tmp=[]
	if flag==1:
		node_set=find_node(H,i)
		for each in node_set:
			H.remove_node(each)
			tmp.append(each)
	if H.number_of_nodes==0:
		b.append(tmp)
		break

print b

nx.draw(G,with_labels=True)
plt.show() 
