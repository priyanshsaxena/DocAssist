import numpy as np
import pandas as pd



data = pd.read_csv("data.csv",header = 0)
symptoms = pd.read_csv("symptoms.csv")

data = data.values
symptoms = symptoms.values

disease_symptoms = np.zeros((148,404))


size = data.shape[0]
size2 = symptoms.shape[0]

# initial_disease = data[0,0]
# print(data[0,0])
# count = 0
# for i in range (0,size):
# 	disease = data[i,0]
# 	if (initial_disease != disease):
# 		initial_disease = disease
# 		# print(initial_disease)
# 		count = count + 1
# 	for j in range(0,size2):
# 		# print(data[i,1]),i
# 		data[i,1] = data[i,1].strip()
# 		symptoms[j,0] = symptoms[j,0].strip()
# 		# print (symptoms[j,0])
# 		if (str(symptoms[j,0]) == str(data[i,1])):
# 			disease_symptoms[count,j] = 1

np.savetxt("new_rep.csv", disease_symptoms, delimiter=",")	

# for i in range(1,149):
# 	print(i)

# array = np.zeros((148,148))
# for i in range(0,148):
# 	a = np.zeros((1,148))
# 	a[0,i] = bool(1)
# 	# print (a[0])
# 	array[i,:] = a

# np.savetxt("disease_rep.csv", array, delimiter=",")	
# file = open("disease_rep.csv",'w')
# for i in range(0,148):
# 	a = np.zeros((1,148))
# 	a[0,i] = bool(1)
# 	file.write(" ".join(map(str,map(int,a[0]))))
# 	file.write("\n")
# file.close()	

# # for i in range(0,148):
# # 	print (array[i])	

