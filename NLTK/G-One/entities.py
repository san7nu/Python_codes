from google.cloud import language

f = open("sample1.txt", "r")
client = language.LanguageServiceClient()

document = language.types.Document(
    content=f.read(),
    language='en',
    type='PLAIN_TEXT',
)

response = client.analyze_entities(
    document=document,
    encoding_type='UTF32',
)

for entity in response.entities:
    print('=' * 20)
    print('         name: {0}'.format(entity.name))
    #print('         type: {0}'.format(entity.entity_type))
    print('     metadata: {0}'.format(entity.metadata))
    print('     salience: {0}'.format(entity.salience))
