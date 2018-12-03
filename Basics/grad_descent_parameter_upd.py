# Simple parameter update for gradient descent with MSE cost func

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,3,3,2,5]

# x = [1, 1, 2, 3, 4, 3, 4, 6, 4]
# y = [2, 1, 0.5, 1, 3, 3, 2, 5, 4]

# x = [1,2,3,4]
# y = [8,11,14,17]
n = len(x)
for_loss_plot = []
num_of_tms_training = 20
learning_rate = 0.001 

B0, B1 = 1,0.3
dB0, dB1 = 0,0

for k in range(num_of_tms_training):
    loss = 0
    for i in range(n):
        dB1 += 2*x[i]*((B1*x[i] + B0) - y[i])
        dB0 += 2*x[i]*((B1*x[i] + B0) - y[i])
        loss += ((B1*x[i] + B0) - y[i])**2
        print(dB0,dB1,"---",loss)
    B1 -= (dB1 / float(n)) * learning_rate
    B0 -= (dB1 / float(n)) * learning_rate
    loss = loss/n
    for_loss_plot.append(loss)
    print("================================================>",B1,B0, loss)
    
plt.plot(range(num_of_tms_training),for_loss_plot)