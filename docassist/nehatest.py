import numpy as np
import pandas as pd
from keras.models import Sequential,load_model
from keras.layers import Dense, Dropout, Activation
from keras.utils import np_utils
import matplotlib.pyplot as plt


def parse_string(a):
	a = a.split(",")
	size = len(a)
	array = np.zeros((1,404))
	symptoms = pd.read_csv("/var/www/html/symptoms.csv")
	symptoms = symptoms.values
	size2 = symptoms.shape[0]
	for i in range (0,size):
		for j in range(0,size2):
			if (str(symptoms[j,0]) == str(a[i])):
				# print str(symptoms[j,0])," -> " ,str(a[i])
				array[0,j] = 1
	tests(array)			


def tests(x_test):
	# pass
	np.random.seed(1234)
	textdata = pd.read_csv("/var/www/html/new_rep.csv")
	disease_rep = pd.read_csv("/var/www/html/disease_rep.csv", header = 0)
	model = load_model("/var/www/html/model.h5")
	textdata = textdata.values
	x_test = np.reshape(x_test,(1,1,404))
	predictions = model.predict(x_test)
	size = disease_rep.shape[0]
	#print (size)
	array = np.zeros((size,2))
	for i in range (0,size):
		array[i,0] = i
		array[i,1] = predictions[0,0,i]
	
	# print (array)
	array = array[np.argsort(array[:,1])]
	# print(array)
	ret = []
	for i in range(0,5):
		index = int(array[size-i-1,0])
		ret.append([textdata[index,0],float(array[size-i-1,1])])
	file = open("/var/www/html/out.csv","w")
	for i in ret:
		file.write(i[0]+","+str(i[1]))
		file.write("\n")
	file.close()


def train():
	np.random.seed(1234)
	textdata = pd.read_csv("/var/www/html/new_rep.csv")
	data = pd.read_csv("/var/www/html/new_rep.csv")
	disease = pd.read_csv("/var/www/html/disease_rep.csv", header = 0)
	dis_array = pd.read_csv("/var/www/html/diseases.csv")
	data = data.values
	disease = disease.values
	textdata = textdata.values
	dis_array = dis_array.values

	rows = disease.shape[0]
	num_diseases = disease.shape[0]
	# print(disease.shape)
	x_train = data[0:rows,1:]
	y_train = np.zeros((rows,rows))
	for i in range (0,rows):
		y_train[i,:] = disease[i][0].split(' ')

	x_train = np.reshape(x_train,(rows,1,404))
	y_train = np.reshape(y_train,(rows,1,num_diseases))
	model = Sequential()
	model.add(Dense(600, input_shape=(1,404)))
	model.add(Activation('linear'))
	model.add(Dense(600))
	model.add(Activation('linear'))
	model.add(Dense(100))
	model.add(Activation('linear'))
	model.add(Dense(num_diseases))
	model.add(Activation('softmax'))

	model.compile(loss='categorical_crossentropy',optimizer='rmsprop')
	model.summary()
	hist = model.fit(x_train, y_train,nb_epoch=20, batch_size=1, verbose=1)

	model.save('/var/www/html/model.h5')


if __name__ == '__main__':
	a = 2
	# train()
	# parse_string("uncoordination,fever,pleuritic pain,snuffle,throat sore,malaise")
	# test()