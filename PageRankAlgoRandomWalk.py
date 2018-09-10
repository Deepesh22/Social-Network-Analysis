import networkx as nx 
import random
import numpy as np

def add_edges(G,p):
	for i in G.nodes():
		for j in G.nodes():
			if(i!=j):
				r=random.random()
				if(r<=p):
					G.add_edge(i,j)
	return G

def get_nodes_sorted(points):
	points_array=np.array(points)
	return np.argsort(-points_array)

def random_walk(G):
	nodes=list(G.nodes())
	points=[0 for i in range(G.number_of_nodes())]
	r= random.choice(nodes)
	points[r]+=1
	out=list(G.out_edges(r))
	c=0
	while(c!=100000 ):
		if(len(out)==0):
			current_node=random.choice(nodes)
		else:
			neigh=random.choice(out)
			current_node=neigh[1]
		points[current_node]+=1
		out=list(G.out_edges(current_node))
		c+=1
	return points

def main():
	#Create a distributed graph with n nodes
	G= nx.DiGraph()
	G.add_nodes_from([i for i in range(10)])
	G=add_edges(G,0.3)
	# perform random walk
	points=random_walk(G)
	#get nodes ranking as per the points accumulated
	sorted_nodes=get_nodes_sorted(points)
	print sorted_nodes
	#compare the ranks thus obtain with the ranks obtained from the inbuilt page rank method
	pr=nx.pagerank(G)
	pr_sorted = sorted(pr.items(),key = lambda x:x[1],reverse=True)
	for i in pr_sorted:
		print i[0],
	print points

main()
