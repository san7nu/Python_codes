## We will train with one full batch in single epoch => wts also get updated in single go

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

n = 10
n_train = 8
n_test = 2

def sigmoid(i):
  return 1 / (1 + np.exp(-i))

def findcost(w,x):
    cost = 0 
    for i in range(0,len(x)): 
        cost = cost + ( sigmoid(w.dot(np.array(x[i]))) - (i%2) )**2
    return cost/len(x)


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
W = 2*np.random.rand(1,15)-1 #random wts

# Altering W using backprop
for epoch in range(0,1000): 
    sig = sigmoid(np.dot(x,W.T))
    red = 2*(sig-y)*(sig*(1-sig))
    dw = np.dot(red.T,x)
    W = W - dw
    cost_now = findcost(W,x)
    trackCost.append(cost_now)

plt.plot(trackCost)
plt.show()

print("========== TESTING ========")
print(sigmoid(W.dot(list_x[8])))
print(sigmoid(W.dot(list_x[9])))