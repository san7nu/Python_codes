from keras.datasets import cifar10
import matplotlib
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

z = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck',]

print(x_train.shape)
# plt.subplot(2, 1, 1)
# plt.imshow(x_test[1])
# plt.subplot(2, 1, 2)
# plt.imshow(x_train[1])

print("RESULT --- ACTUAL")

for n,i in enumerate(x_test[0:6]):
    c = np.abs(x_train - i)
    d = np.sum(c, axis=(1,2,3))
    min_index = np.argmin(d)
    print(z[y_train[min_index][0]],"---", z[y_test[n][0]])

# plt.subplot(2, 1, 1)
# plt.imshow(i)
# plt.subplot(2, 1, 2)
# plt.imshow(x_train[min_index])