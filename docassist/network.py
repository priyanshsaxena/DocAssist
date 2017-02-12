import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import np_utils
import matplotlib.pyplot as plt

np.random.seed(1234)
textdata = pd.read_csv("new_rep.csv")
data = pd.read_csv("new_rep.csv")
disease = pd.read_csv("disease_rep.csv", header = 0)
dis_array = pd.read_csv("diseases.csv")
data = data.values
disease = disease.values
textdata = textdata.values
dis_array = dis_array.values

rows = disease.shape[0]

print(disease.shape)
# rows  = 148

x_train = data[0:rows,1:]
y_train = np.zeros((rows,rows))
for i in range (0,rows):
	y_train[i,:] = disease[i][0].split(' ')


rows1 = 147
# x_test = data[rows1: ,2:]
y_test = np.zeros((rows-rows1,rows))
for i in range (rows1,rows):
	y_test[i-rows1,:] = disease[i][0].split(' ')

x_test = np.zeros((1,404))
x_test[0,:] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


x_train = np.reshape(x_train,(rows,1,404))
x_test = np.reshape(x_test,(148 - rows1,1,404))
y_train = np.reshape(y_train,(rows,1,148))
y_test = np.reshape(y_test,(148 - rows1,1,148))

model = Sequential()
model.add(Dense(404, input_shape=(1,404)))
model.add(Activation('relu'))
model.add(Dense(200))
model.add(Dense(100))
model.add(Dense(148))
model.add(Activation('softmax'))

model.compile(loss='mse',optimizer='adam')
model.summary()
hist = model.fit(x_train, y_train,nb_epoch=14, batch_size=1, verbose=1)

predictions = model.predict(x_test)
array = np.zeros((148,2))
for i in range (0,148):
	array[i,0] = i
	array[i,1] = predictions[0,0,i]
array = array[np.argsort(array[:,1])]


y = hist.history
plt.plot(y['loss'])
plt.hold(1)

for i in range(0,5):
	index = int(array[147-i,0])
	print(textdata[index,0])

model.save('model.h5')

