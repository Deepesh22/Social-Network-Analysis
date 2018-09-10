import networkx as nx
import itertools as it
def brute_community(G):
	nodes=G.nodes()
	n=G.number_of_nodes()
	fc=[]
	sc=[]
	#determining nodes falling in community 1 and 2, for loop till n/2 only while determining fc is bcoz of fact that sc will have nodes which will not be in fc.
	for i in range(1,n/2+1): #combinations for 1st community
		comb=[list(x) for x in it.combinations(nodes,i)]
		fc.extend(comb)
	#print fc
	for i in (fc): #appending nodes not in 1st community to 2nd community
		sc.append(list(set(nodes)-set(i)))
	#print sc
	
	#among all division of nodes in both coomunity which is best
	num_intra_edges1=[] #no. of intra edges in 1st community
	num_intra_edges2=[] #no of intra edge in 2nd community 
	num_inter_edges=[] #no. of inter edges acroos both communtiy
	ratio=[] #ratio of number of intra/number of inter
	for i in fc:
		num_intra_edges1.append(G.subgraph(i).number_of_edges())
	for i in sc:
		num_intra_edges2.append(G.subgraph(i).number_of_edges())
	for i in range(len(fc)):
		num_inter_edges.append(G.number_of_edges()-num_intra_edges2[i]-num_intra_edges1[i])
	for i in range(len(fc)):
		ratio.append((float)(num_intra_edges1[i]+num_intra_edges2[i])/num_inter_edges[i])
	max_value=max(ratio)
	max_index=ratio.index(max_value)
	print fc[max_index],sc[max_index]

G=nx.barbell_graph(5,0)
brute_community(G)
