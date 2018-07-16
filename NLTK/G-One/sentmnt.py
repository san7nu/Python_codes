from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


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

low_score = 0
useful_list = []
for s in sentiment.sentences:
    if s.sentiment.score < low_score:
        low_score = s.sentiment.score
        useful_list.append(s.text.content)
    print('{} ---- {}'.format(s.sentiment.score, s.text.content))

print("=======================================================")
'''
Apply exclusn: sentence with questn mark
'''
i = 0
'''for i, s1 in enumerate(useful_list):
    if s1.find("?"):
        break'''

print(useful_list[len(useful_list) - i - 1])

'''
Analyze for imp entities
'''

final_document = types.Document(
    content=useful_list[len(useful_list) - i - 1],
    language='en',
    type=enums.Document.Type.PLAIN_TEXT)

response = client.analyze_entities(
    document=final_document,
    encoding_type='UTF32',
)


print("=======================================================")
final_entities = []
for entity in response.entities:
    print('name: {}'.format(entity.name))
    final_entities.append(entity.name)
print("=======================================================")

'''entities_doc = types.Document(
    content=' '.join(final_entities),
    language='en',
    type=enums.Document.Type.PLAIN_TEXT)

entity_sentiment = client.analyze_sentiment(document=entities_doc)

print(entity_sentiment)'''

'''low_score = 0
useful_entity = []
for s in entity_sentiment.sentences:
    if s.sentiment.score < low_score:
        low_score = s.sentiment.score
        useful_list.append(s.text.content)
    print('{} ---- {}'.format(s.sentiment.score, s.text.content))

print("=======================================================")
print(useful_list[len(useful_list) - 1])'''
