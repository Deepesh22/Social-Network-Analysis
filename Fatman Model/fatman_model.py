import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time
#from matplotlib.backends.backend_pdf import PdfPages
#pp = PdfPages('evolution.pdf')


def create_graph():
	G=nx.Graph()
	for i in range(1,101):
		G.add_node(i)
	return G

def bmi(G): #to assign bmi
	for each in G.nodes():
		G.node[each]["name"]=random.randint(15,40) #assigning random bmi bw 15 and 40 to each node of G and storing bmi in attribute "name"
		G.node[each]["type"]="person" #creating attribute defining "type" of node

def get_labels(G): 	#to get a dictionary with labels for nodes as bmi
	dict1={}
	for each in G.node():
		dict1[each]=G.node[each]["name"] #storing bmi in key each of dict1
	return dict1

def get_size(G): #storing bmi of each node in a list to use its value as size for node
	size=[]
	for each in G.node():
		if G.node[each]["type"]=="person":
			size.append(G.node[each]["name"]*15) #*15 to inc size and visualize better
		else:
			size.append(1200)
	return size

def add_foci(G): #adding foci
	foci_nodes=["gym","eatout","movie","karate","yoga"]
	for i in range(5):
		n=G.number_of_nodes()
		G.add_node(n+1)
		G.node[n+1]["name"]=foci_nodes[i]
		G.node[n+1]["type"]="foci" 

def get_color(G): #setting color to nodes or persons and foci
	c=[]
	for each in G.node():
		if G.node[each]["type"]=="person":
			if G.node[each]["name"]==15:
				c.append("green")
			elif G.node[each]["name"]==40:
				c.append("yellow")
			else:
				c.append("blue")

		else:
			c.append("red")
	return c 

def get_foci_nodes():
	f=[]
	for each in G.node():
		if G.node[each]["type"]=="foci":
			f.append(each)
	return f

def get_person_nodes():
	p=[]
	for each in G.node():
		if G.node[each]["type"]=="person":
			p.append(each)
	return p

def add_foci_edges(): #connecting persons to foci(one person is connected to only one foci initially)
	foci_nodes=get_foci_nodes()
	person_nodes=get_person_nodes()
	for each in person_nodes:
		r=random.choice(foci_nodes)
		G.add_edge(each,r)

def homophily(G): #implementing homophily
	person_nodes=get_person_nodes()
	for u in person_nodes:
		for v in person_nodes:
			if u!=v:
				d=abs(G.node[u]["name"]-G.node[u]["name"])
				p=float(1)/(d+1000)
				r=random.random()
				if r<p:
					G.add_edge(u,v)

def cmn(u,v):
	nu=set(G.neighbors(u))
	nv=set(G.neighbors(v))
	return len(nv & nu)

def closure(G):
	a=[]
	for u in G.node():
		for v in G.node():
			if(u!=v and (G.node[u]["type"]=="person" or G.node[u]["type"]=="person")):
				k=cmn(u,v)
				p=1-math.pow((1-0.001),k)
				tmp=[]
				tmp.append(u)
				tmp.append(v)
				tmp.append(p)
				a.append(tmp)
	for each in a:
		 u=each[0]
		 v=each[1]
		 p=each[2]
		 r=random.random()
		 if(r<p):
		 	G.add_edge (u,v)

def social_inf(G):
	fnodes=get_foci_nodes()
	for each in fnodes:
		if G.node[each]["name"]=="gym" or G.node[each]["name"]=="gym" or G.node[each]["name"]=="yoga":
			for each1 in G.neighbors(each):
				if G.node[each1]["name"]!=15:
					G.node[each1]["name"]-=1
		if G.node[each]["name"]=="eatout" or G.node[each]["name"]=="movie":
			for each1 in G.neighbors(each):
				if G.node[each1]["name"]!=40:
					G.node[each1]["name"]+=1

def show(G,t):
	labeldict=get_labels(G)
	nodesize=get_size(G)
	color=get_color(G)
	pos=nx.spring_layout(G)
	nx.draw(G,pos,labels=labeldict,node_size=nodesize,node_color=color)
	plt.show()
	plt.savefig("evolution"+str(t)+".jpg")
	#plt.savefig(pp, format='pdf')
	#plt.clf()
	#plt.cla()
	nx.write_gml(G,"evolution"+str(t)+".gml")



G=create_graph()
bmi(G)
add_foci(G)
add_foci_edges()
time.sleep(1)
t=0
show(G,t)
for i in range(15):
	homophily(G)
	closure(G)
	social_inf(G)
	show(G,i+1)
#pp.close()