import tensorflow as tf
import pandas as pd
import nltk as nl
import numpy as np
import sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import tflearn
from nltk.corpus import stopwords
from flask import Flask, jsonify, request


df = pd.read_csv('Samples\icd10_ABC_31.txt')

print("================================ Tokenizing ==================================")
df['tokens'] = [nl.word_tokenize(s) for s in df.desc]
words = []
for i in df.tokens:
    words.extend(i)

print("================================ Removing stopwords ==================================")
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]


print("================================== Stemming ==================================")
stemmer = nl.stem.snowball.SnowballStemmer('english')
#stemmer = nl.stem.lancaster.LancasterStemmer()
words = [stemmer.stem(word) for word in words]
words = sorted(set(words))
#words = set(words)

training = []
for index, item in df.iterrows():
    onehot = []
    token_words = [stemmer.stem(word) for word in item['tokens']]
    for w in words:
        onehot.append(1) if w in token_words else onehot.append(0)
    training.append([onehot, item['code']])

# print(words)
# print(training)
print("================================== preprocessing ==================================")
training_new = np.array(training)


label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(training_new[:, 1])
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

train_x = list(training_new[:, 0])
train_y = onehot_encoded
# print(len(train_x[0]))
# print(train_x)
# print(train_y)

print("================================ TF ========================================")

tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 100)
net = tflearn.fully_connected(net, 100)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
#model = tflearn.DNN(net, tensorboard_dir='tflearn_logs', tensorboard_verbose=3)
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)

model.fit(train_x, train_y, n_epoch=6, batch_size=5, show_metric=True)
model.save('model.tflearn1')

print("======================== Testing ==================================")

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    fromAPI = {'desc': [request.json["sent"]]}
    test = pd.DataFrame(fromAPI, columns=['desc'])
    test['tokens'] = [nl.word_tokenize(w) for w in test.desc]
    print("======================== Testing2 ==================================")
    print(test)
    testing = []
    for index, item in test.iterrows():
        onehot = []
        token_words = [stemmer.stem(word) for word in item['tokens']]
        for w in words:
            onehot.append(1) if w in token_words else onehot.append(0)
        testing.append(onehot)
    print("======================== Testing3 ==================================")
    print(sum(testing[0]))
    print(len(testing[0]))
    testing = list(np.array(testing))
    print(np.any(testing))
    predicted = model.predict(X=testing)

    result = pd.DataFrame(predicted)

    result.columns = sorted(list(set(df.code)))
    print(result.transpose()[0].sort_values(ascending=False).head(10))
    print(result.idxmax(axis=1))
    out = result.idxmax(axis=1)
    print(out[0])
    print(type(out))
    return jsonify({'out': out[0]})


if __name__ == '__main__':
    app.run(port=5005, debug=True, use_reloader=False)
