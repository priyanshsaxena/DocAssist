import numpy as np
import pandas as pd
import nehatest as T

def update_disease_rep(size):
	array = np.zeros((size,size))
	for i in range(0,size):
		a = np.zeros((1,size))
		a[0,i] = bool(1)
		array[i,:] = a

	np.savetxt("disease_rep.csv", array, delimiter=",")	
	file = open("disease_rep.csv",'w')
	file.write(" ".join("DISEASE"))
	file.write("\n")
	for i in range(0,size):
		a = np.zeros((1,size))
		a[0,i] = bool(1)
		file.write(" ".join(map(str,map(int,a[0]))))
		file.write("\n")
	file.close()

def add_disease(a):
	data = pd.read_csv("new_rep.csv")
	symptoms = pd.read_csv("symptoms.csv")
	disease_rep = pd.read_csv("disease_rep.csv")
	data = data.values
	symptoms = symptoms.values
	disease_rep = disease_rep.values
	
	size = disease_rep.shape[0]
	size = size + 1

	update_disease_rep(size)
	new_rep_list = data.tolist() 
	new_rep_list.append(a)
	# print(new_rep_list)
	file = open("new_rep.csv","a")
	file.write(a[0])
	for item in a[1:]:
		file.write(",")
		file.write(str(item))
	file.write("\n")
	file.close()
	T.train()
	

def convert(a):
	x = []
	a = a.split(',')
	x.append(a[0])
	array = np.zeros((1,404))
	size = len(a)
	symptoms = pd.read_csv("symptoms.csv")
	symptoms = symptoms.values
	size2 = symptoms.shape[0]
	for i in range (1,size):
		for j in range(0,size2):
			if (str(symptoms[j,0]) == str(a[i])):
				array[0,j] = 1
	l = array.tolist()
	for i in l[0]:
		x.append(i)
	add_disease(x)

if __name__ == '__main__':	
	convert("breastpain,uncoordination,fever,pleuritic pain,snuffle,throat sore,malaise,debilitation,symptom aggravating factors,chill")