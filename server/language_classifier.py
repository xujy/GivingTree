import json
from watson_developer_cloud import NaturalLanguageClassifierV1

class LanguageUnderstanding():


    def __init__(self):
        self.natural_language_classifier = NaturalLanguageClassifierV1(username='c78668c9-16a1-4cea-a453-25c89bbce1d6',password='k8tNQegE6FKd')


    def train(self):
        with open('../charity_data_train.csv', 'rb') as training_data:
            classifier = self.natural_language_classifier.create(
                training_data=training_data,
                name='Charity Category',
                language='en'
            )
        print(json.dumps(classifier, indent=2))


    def status(self):
        classifiers = self.natural_language_classifier.list()
        status = self.natural_language_classifier.status('c533b1x244-nlc-3169')
        print (json.dumps(status, indent=2))


    def remove(self,id):
        classes = self.natural_language_classifier.remove(id)
        print(json.dumps(classes, indent=2))

    def classify(self):
        classes = self.natural_language_classifier.classify('c533b1x244-nlc-3169', 'petroleum canada natural gas energy oilsands keystone xl')
        print(json.dumps(classes, indent=2))

lu = LanguageUnderstanding()
lu.classify()
