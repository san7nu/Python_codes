# Linear classification with W in step-by-step refinement(see all directions and choose vch is less loss causing)

sample_count = 4
x = np.array([[1,600],[2,900],[1,475],[2,1100]])
y = np.array([55,75,50,100])
#W = np.random.randint(5, size=(4,2)) #* 0.0001
#W = np.array([[1,2],[3,4],[5,6],[7,8]])
W = np.array([[1,2],[0,2],[3,1],[1,0]])

x_test = np.array([1,700]).reshape([2,1])
step = 0.001
bestloss = float('inf')
print(y.shape)

for i in range(30):
    for n in range(sample_count):
        #print("======================= {}".format(n))
        new_W = W + np.random.randint(100, size=(4,2)) * step
        loss_now = np.sum(y - new_W.dot(x[n]))   
        #print("----->",loss_now,new_W)
        if loss_now < bestloss:
            W = new_W
            bestloss = loss_now

scores = W.dot(x_test)
print(scores)
predicted_pos = np.argmax(scores,axis=0)
print(bestloss, y[predicted_pos])