## 3 layers and contrast with different learning rate

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

n = 10
n_train = 8
n_test = 2

def sigmoid(i):
  return 1 / (1 + np.exp(-i))


# Reading pixel files and storing active pixels
list_x = []
for i in range(0,10):
    file = str(i)+'.png'
    im = Image.open(file)
    pix = list(im.getdata())
    a = [int(i == (0,0,0)) for i in pix]
    list_x.append(a)

x = np.array(list_x[0:n_train])

y = np.array([(i%2) for i in range(0,n_train)]).reshape(n_train,1)

trackCost = []
np.random.seed(1)
W0 = 2*np.random.rand(15,10)-1 #random wts
W1 = 2*np.random.rand(10,1)-1 #random wts

def NN(W0,W1,alpha):
    for epoch in range(0,1000):
        # Forward prop
        l0 = x
        l1 =  sigmoid(l0.dot(W0))
        l2 =  sigmoid(l1.dot(W1))

        # Back prop
        l2_delta = (l2-y)*l2*(1-l2)
        l1_delta = (l2_delta.dot(W1.T))*l1*(1-l1)

        W1 -= (l1.T.dot(l2_delta)) * alpha
        W0 -= (l0.T.dot(l1_delta)) * alpha
        
        cost_now = np.sum((l2 - y)**2)
        trackCost.append(cost_now)

    plt.plot(trackCost)
    plt.show()

    print("========== TESTING ======== with learning rate", alpha)
    print("Final cost is:",cost_now)
    l0 = np.array(list_x[n_train:n])
    l1 =  sigmoid(l0.dot(W0))
    l2 =  sigmoid(l1.dot(W1))
    print(l2)

NN(W0,W1,0.1)
NN(W0,W1,1)
NN(W0,W1,10)