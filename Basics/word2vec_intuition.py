# Intuition of word2vec

# I like deep learining
# I like NLP
# I enjoy flying

import numpy as np
import matplotlib.pyplot as plt
words = ["I","like","enjoy","deep","learning","NLP","flying","."]
X = np.array([[0,2,1,0,0,0,0,0],
              [2,0,0,1,0,1,0,0],
              [1,0,0,0,0,0,1,0],
              [0,1,0,0,1,0,0,0],
              [0,0,0,1,0,0,0,1],
              [0,1,0,0,0,0,0,1],
              [0,0,1,0,0,0,0,1],
              [0,1,0,0,1,1,1,0]
              ])

U,s,Vh = np.linalg.svd(X,full_matrices=False)

fig = plt.figure(figsize=(8,8))
a = plt.ylim([-0.5,0.5])

for i in range(len(words)):
    plt.text(U[i,0]+1,U[i,1]/3,words[i])