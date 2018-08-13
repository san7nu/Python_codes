from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
lm = WordNetLemmatizer()

ex = "food poisioning"
ex_words = word_tokenize(ex)
print(ex_words)

for i in ex_words:
    print(ps.stem(i))
print(pos_tag(ex_words))


print(lm.lemmatize("food poisioning", pos='n'))
print(ps.stem("food poisioning"))

print(dir(lm))
