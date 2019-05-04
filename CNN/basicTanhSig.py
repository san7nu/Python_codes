import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def sig(x):
    return 1 / (1 + np.exp(-1*x) )
def d_sig(x):
    return sig(x) * (1 - sig(x))

def tanh(x):
    return np.tanh(x)
def d_tanh(x):
    return 1 - (np.tanh(x))**2

def findcost(w1,w2,track_out=False):
    cost = 0
    out = []
    for i in range(0,len(X)):
        l1 = signal.convolve2d(X[i],w1,'valid')
        l1a = tanh(l1).reshape(1,len(X))
        l2 = np.dot(l1a,w2)
        l2a = sig(l2)
        if track_out == True:
            out.append(l2a[0])
        tmp = (l2a - Y[i])**2
        cost += (l2a - Y[i])**2
    return cost[0],out

x1 = np.array([[0,0,0],[0,0,0],[0,0,0]])
x2 = np.array([[1,1,1],[0,0,0],[0,0,0]])
x3 = np.array([[0,0,0],[1,1,1],[1,1,1]])
x4 = np.array([ [1,1,1],[1,1,1],[1,1,1]])
X = [x1,x2,x3,x4]
Y = np.array([0.53,0.77,0.88,1.1]).reshape(len(X),1)

np.random.seed(1)
w1 = np.random.random((2,2))
w2 = np.random.random((4,1))

tracecost = []
learning_rate = 0.1
epoch = 500

for n in range(0,epoch):
    c, _ = findcost(w1,w2,False)
    tracecost.append(c)
    for i in range(0,len(X)):
        #Fwd prop
        l1 = signal.convolve2d(X[i],w1,'valid')
        l1a = tanh(l1).reshape(1,len(X))
        l2 = np.dot(l1a,w2)
        l2a = sig(l2)
        
        #Back prop
            #dw2 = dc_l2a * dl2a_l2 * dl2_w2
            #dw1 = dc_l2a * dl2a_l2 * dl2_l1a * dl1a_l1 * dl1_dw1
            # OR thk it as propagation of grad
            #dc(cost layer) = derv of cost 
            #dw2(l2 layer) =  dc * derv sig(l2) * layer1_out
            #dw1(l1 layer) = dc * derv sig(l2) * w2 * derv tanh(l1) * layer1_out(which is X)
            #In final layer we need to convolve to pass grads
        dc_l2a = 2*(l2a - Y[i])
        dl2a_l2 = d_sig(l2a)
        dl2_w2 = l1a
        
        dl2_l1a = w2
        dl1a_l1 = d_tanh(l1a)
        dl1_dw1 = X[i]
        
        dw2 = dc_l2a * dl2a_l2 * (dl2_w2.reshape(len(X),1))
        tmp2 = np.dot((dc_l2a * dl2a_l2),dl2_l1a.T)
        tmp1 = (tmp2  * dl1a_l1).reshape(w1.shape)
        dw1 = signal.convolve2d(dl1_dw1,tmp1,'valid')
        w1 -= learning_rate*dw1
        w2 -= learning_rate*dw2

c, out = findcost(w1,w2,True)
tracecost.append(c)

plt.plot(tracecost)
plt.show()
print(c)
print(out)
print(Y.T)
# print(w1,w2)