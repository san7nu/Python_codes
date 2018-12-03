#### KNN from sklearn

from keras.datasets import cifar10
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from pprint import pprint

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

z = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck',]

print(x_train.shape)
x_train_flat = x_train.reshape((50000,3072))
x_test_flat = x_test.reshape((10000,3072))

clf = KNeighborsClassifier(5, weights='uniform')
clf.fit(x_flat,y_train)
out = clf.predict(x_test_flat[:10])

print(out)

for i in out:
    print(z[i])