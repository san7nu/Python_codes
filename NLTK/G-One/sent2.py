from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

client = language.LanguageServiceClient()

f = open("Samples/1.txt", "r")
text = f.read()

'''
Sortng sentence on sentiment & apply exclusn & take top sentence
'''
document = types.Document(
    content=text,
    language='en',
    type=enums.Document.Type.PLAIN_TEXT)

sentiment = client.analyze_sentiment(document=document)

useful_list = []
for s in sentiment.sentences:
    if s.sentiment.score < 0:
        useful_list.append(s.text.content)
    print('{} ---- {}'.format(s.sentiment.score, s.text.content))

print("=======================================================")
s = "".join(useful_list)

with open('ICD9codes_Orig.json') as f:
    data = json.load(f)

out = set()
for d in data:
    for j in d:
        if len(j) == 4:
            for word in j['descr'].lower().split(" "):
                if word == "and" or word == "to" or len(word) < 4:
                    continue
                if(s.lower().find(" "+word+" ") != -1):
                    out.add(word)
print(out)
