# Linear classification with guessed W

x = np.array([[1,600],[2,900],[1,475],[2,1100]])
y = np.array([55,75,50,100])
W = np.random.randint(5, size=(4,2)) #* 0.0001
#W = np.array([[1,2],[3,4],[5,6],[7,8]])
#W = np.array([[1,2],[0,2],[3,1],[1,0]])

x_test = np.array([1,700]).reshape([2,1])

print(W)

scores = W.dot(x_test)
print(scores)
predicted_pos = np.argmax(scores,axis=0)
print(scores,predicted_pos)
print(y[predicted_pos])