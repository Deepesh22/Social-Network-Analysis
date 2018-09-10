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

def initialize_points(G):
	points=[100 for i in range(G.number_of_nodes())]
	return points

def distribute_points(G,points):
	prev_points=points
	new_points=[0 for i in range(G.number_of_nodes())]
	for i in G.nodes():
		out=G.out_edges(i)
		if len(out)==0:
			new_points[i]+=prev_points[i]
		else:
			share=(float)(prev_points[i]/len(out))
			for each in out:
				new_points[each[1]]+=share
	return G,new_points

def handle_sink(G,points):
	for i in range(len(points)):
		points[i]=(float)(points[i])*0.8
	n=G.number_of_nodes()
	extra=((float)(n)*100*0.2)/n
	for i in range(len(points)):
		points[i]+=extra
	return points

def keep_distributing_points(G,points):
	prev_points=points
	print "Enter # to stop"
	while(1):
		G,new_points=distribute_points(G,prev_points)
		print new_points
		new_points=handle_sink(G,prev_points)
		char=raw_input()
		if char=="#":
			break
		prev_points=new_points
	return G,new_points

def get_nodes_sorted(points):
	points_array=np.array(points)
	return np.argsort(-points_array)

def main():
	#Create a distributed graph with n nodes
	G= nx.DiGraph()
	G.add_nodes_from([i for i in range(10)])
	G=add_edges(G,0.3)
	#Assign 100 or equal points to each node
	points=initialize_points(G)
	print points
	#keep distributin point untill convergence
	G,points=keep_distributing_points(G,points)
	#get nodes ranking as per the points accumulated
	sorted_nodes=get_nodes_sorted(points)
	print sorted_nodes
	#compare the ranks thus obtain with the ranks obtained from the inbuilt page rank method
	pr=nx.pagerank(G)
	pr_sorted = sorted(pr.items(),key = lambda x:x[1],reverse=True)
	for i in pr_sorted:
		print i[0],

main()
