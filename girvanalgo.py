import networkx as nx

def edge_to_remove(G):# compute betweeness and sort accordingly and get edge with highest betweeness value
	dict1=nx.edge_betweenness_centrality(G) 
	list_of_tuples=dict1.items()
	list_of_tuples.sort(key=lambda x:x[1], reverse=True)
	return list_of_tuples[0][0] #(a,b)

def girvan(G):
	c=list(nx.connected_component_subgraphs(G))
	l=len(c)
	print "The number of connected component are ",l
	while(l==1):
		G.remove_edge(*edge_to_remove(G)) #returned value is in form (a,b) but we need to pass a,b in remove edge func. therefor get elements only of tuple we use *
		c=list(nx.connected_component_subgraphs(G))
		l=len(c)
		print "The number of connected component are ",l
	return c

G=nx.karate_club_graph()
#G=nx.barbell_graph(5,0)
c= girvan(G)
for i in c:
	print i.nodes(),"*****",i.number_of_nodes(),"*****\n"
