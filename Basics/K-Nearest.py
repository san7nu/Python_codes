#### Simplest K-NN

from keras.datasets import cifar10
import matplotlib
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

z = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck',]

print(x_train.shape)

print("RESULT --- ACTUAL")

i = x_test[1]
c = np.abs(x_train - i)
d = np.sum(c, axis=(1,2,3))
minTop_index = d.argsort()[:100]
print(minTop_index)
most_index = np.bincount(minTop_index)
print(np.argmax(most_index))

# for i in min_index[0:10]:
#     print(d[i])

# plt.subplot(2, 1, 1)
# plt.imshow(i)
# plt.subplot(2, 1, 2)
# plt.imshow(x_train[min_index])