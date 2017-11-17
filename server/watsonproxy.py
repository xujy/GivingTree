import json
from collections import defaultdict
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

json_data=open("sample.json").read()
data = json.loads(json_data)
response = defaultdict(list)
for key,value in data.items():

    '''if key == entities:
        print""

    if key == concepts:
        print""


    if key == keywords:
        print""

    if key == categories:
        print""'''

    if key == "metadata":
        response["title"] = value["title"]

print response


class WatsonProxy():
    def __init__(self):
        self.resultdict = {}
        self.api = {
            "url": "https://gateway.watsonplatform.net/natural-language-understanding/api",
            "username": "cac72f87-4a20-45c6-9b45-0305632c0bfc",
            "password": "K0ILmZ3JqLiN"
        }
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(username= self.api['username'],password= self.api['password'],version="2017-02-27")


    def nlu(self,urlstr):
        response = self.natural_language_understanding.analyze(
        url=urlstr,
        features=[
            Features.Concepts(limit=3),
            Features.Keywords(limit=3,emotion=True,sentiment=True),
            Features.Entities(limit=3,emotion=True,sentiment=True),
            Features.Categories(),
            Features.MetaData(),
        ])
        return json.dumps(response, indent=2)


    def parse(self, data):

        return


    def runpipe(self, urlstr):
        resp = self.nlu(urlstr)
        print(resp)
        #return parse(resp)

#watson = WatsonProxy()
#watson.runpipe("https://www.nytimes.com/2017/10/19/reader-center/ohio-athens-climate.html")
