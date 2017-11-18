from collections import defaultdict
import json
import operator

from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

class LanguageUnderstanding():


    def __init__(self):
        self.api = {
            'url': 'https://gateway.watsonplatform.net/natural-language-understanding/api',
            'username': 'cac72f87-4a20-45c6-9b45-0305632c0bfc',
            'password': 'K0ILmZ3JqLiN'
        }
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(username= self.api['username'],password= self.api['password'],version='2017-02-27')


    def nlu(self,urlstr):
        response = self.natural_language_understanding.analyze(
        url=urlstr,
        features=[
            Features.Concepts(limit=5),
            Features.Keywords(limit=5,emotion=True,sentiment=True),
            Features.Entities(limit=5,emotion=True,sentiment=True),
            Features.Categories(),
            Features.MetaData()
        ])
        #print json.dumps(response, indent=2)
        return json.dumps(response, indent=2)


    def parse(self, data):
        result = defaultdict(list)
        for key,value in data.items():
            if key == 'keywords':
                for item in value:
                    data = {}

                    try:
                        keyword = item['text']
                        data['title'] = keyword
                    except:
                        data['title'] = ''

                    try:
                        emotions = item['emotion']
                        data['emotion'] = max(emotions.iteritems(), key=operator.itemgetter(1))[0]
                    except:
                        emotions = ''


                    try:
                        data['sentiment'] = item['sentiment']['label']
                    except:
                        data['sentiment'] = ''

                    result['keywords'].append(data)

            if key == 'concepts':
                for item in value:
                    result['concepts'].append(item['text'])

            if key == 'categories':
                for item in value:
                    result['categories'].append(item['label'].strip('/'))

            if key == 'metadata':
                result['title'] = value['title']
        return json.dumps(result)


    def runpipe(self, urlstr):
        resp = self.nlu(urlstr)
        return self.parse(json.loads(resp))
