from __future__ import print_function
import json
import os

# from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    username='u1',
    password='p1')

classifiers = natural_language_classifier.list_classifiers()
print(json.dumps(classifiers, indent=2))

# create a classifier
with open(os.path.join(os.path.dirname(__file__), './samples/ICD-10-GT-AA.csv'), 'rb') as training_data:
    metadata = json.dumps({'name': 'my-classifier', 'language': 'en'})
    classifier = natural_language_classifier.create_classifier(
        metadata=metadata,
        training_data=training_data
    )
    classifier_id = classifier['classifier_id']
    print(json.dumps(classifier, indent=2))

status = natural_language_classifier.get_classifier(classifier_id)
print(json.dumps(status, indent=2))

if status['status'] == 'Available':
    classes = natural_language_classifier.classify(classifier_id,
                                                   'How hot will it be '
                                                   'tomorrow?')
    print(json.dumps(classes, indent=2))

if status['status'] == 'Available':
    collection = ['{"text":"How hot will it be today?"}', '{"text":"Is it hot outside?"}']
    classes = natural_language_classifier.classify_collection(
        classifier_id, collection)
    print(json.dumps(classes, indent=2))

delete = natural_language_classifier.delete_classifier(classifier_id)
print(json.dumps(delete, indent=2))
