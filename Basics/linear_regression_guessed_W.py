# Linear reg(for regression) with guessed W

x = np.array([[1,0.600],[2,0.900],[1,0.475],[2,0.1100]])
y = np.array([0.55,0.75,0.50,0.100])
W = np.random.randn(1,2) #* 0.0001
#W = np.array([[1,2],[3,4],[5,6],[7,8]])
#W = np.array([[1,2],[0,2],[3,1],[1,0]])

x_test = np.array([1,0.700])

print(W)

scores = W.dot(x_test)
print("Predicted is:",scores)