import json
import requests

class Category:
    Animals = 1
    ArtsCultureHumanities = 2
    CommunityDevelopment = 3
    Education = 4
    Environment = 5
    Health = 6
    HumanCivilRights = 7
    HumanServices = 8
    International = 9
    ResearchPublicPolicy = 10
    Religion = 11

class CharityAPI():
    def __init__(self):
        self.url = 'https://api.data.charitynavigator.org/v2/Organizations'
        self.app_id = '54cad626'
        self.app_key = 'd6c8b4cadf59fa82aec7f801cfb5f6c2'
        self.pageSize = 5
        self.rated = True
        self.sort = 'RATING'
        self.scope = 'INTERNATIONAL'
    def getcharity(self, watsonresult):
        payload = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'pageSize': self.pageSize,
            'search': 'oil sands business and industrial energy natural gas Petroleum, Canada, Natural gas',
            'rated': self.rated,
            'sort': self.sort,
            'categoryID': Category.Animals
            #'scopeOfWork' : self.scope
        }
        r = requests.get(self.url, params=payload)
        return r.json()

    def parse(self, rawdata):
        print type(rawdata)
        for item in rawdata:
            #print item
            print '\n'

    def runpipe(self, watsonresult):
        resp = self.getcharity(watsonresult)
        formatresult = self.parse(resp)


charity = CharityAPI()
