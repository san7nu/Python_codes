# Linear reg with W learnt from gradient(mathetically gauranteed direction that will decrease the loss)
import numpy as np

x = np.array([[1,0.600],[2,0.900],[1,0.475],[2,0.1100]])
y = np.array([0.55,0.75,0.50,0.100])

n = len(x)
print(x[0].shape)
for_loss_plot = []
num_of_tms_training = 50
learning_rate = 0.001 

W = np.random.randn(1,2)
dW = np.zeros((1,2))
print(W)
loss = 0

for k in range(num_of_tms_training):
    prev_loss = loss
    prev_W = W + np.zeros(W.shape)
    loss = 0
    for i in range(n):
        dW += 2*x[i]*((W.dot(x[i])[0]) - y[i])
        loss += ((W.dot(x[i])[0]) - y[i])**2
        print(dW,"---",loss)
    W -= (dW / float(n)) * learning_rate
    loss = loss/n
    print(prev_W, "================================================>",W, loss)
    if prev_loss < loss and k > 0:
        W = prev_W
        loss = prev_loss
        break


        
print("\n\n##############################################################",W, loss)

x_test = np.array([1,0.700])


scores = W.dot(x_test)
print("predicted is:", scores[0])