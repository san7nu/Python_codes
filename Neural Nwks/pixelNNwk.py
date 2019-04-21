## Idea is we will read all pixel files and identify each pixel active or not, map this data to even or odd then observe how wts alter
## Lets do wt update on each training sample also we will see cost for each step

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(i):
  return 1 / (1 + np.exp(-i))


# Reading pixel files and storing active pixels
x = []
for i in range(0,10):
    file = str(i)+'.png'
    im = Image.open(file)
    pix = list(im.getdata())
    a = [int(i == (0,0,0)) for i in pix]
    x.append(a)

trackCost = []
np.random.seed(1)
W = 2*np.random.rand(1,15)-1 #random wts

# Altering W using backprop
for epoch in range(0,100):
    for i in range(0,len(x)-2): # Loop till 7, we will use 8,9 to test 
        sig = sigmoid(W.dot(x[i]))
        red = (2*(sig-(i%2))*sig*(1-sig))
        dw = red*x[i]
        W = W - dw
        cost_now = ( sigmoid(W.dot(np.array(x[i]))) - (i%2) )**2
        trackCost.append(cost_now)

plt.plot(trackCost)
plt.show()

print("========== TESTING ========")
print(sigmoid(W.dot(x[8])))
print(sigmoid(W.dot(x[9])))