import json
import requests

class CharityNavigator():


    def __init__(self):
        self.url = 'https://api.data.charitynavigator.org/v2/Organizations'
        self.app_id = '54cad626'
        self.app_key = 'd6c8b4cadf59fa82aec7f801cfb5f6c2'
        self.pageSize = 5
        self.rated = True
        self.sort = 'RATING'
        self.minRating = 4


    def getcharity(self, categoryID, search="", scope='INTERNATIONAL', state=''):
        payload = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'pageSize': self.pageSize,
            'search': search,
            'rated': self.rated,
            'sort': self.sort,
            'categoryID': categoryID,
            'scopeOfWork' : scope,
            'state': ''
        }

        if scope == 'REGIONAL':
            payload['state'] = state

        r = requests.get(self.url, params=payload)
        return r.json()


    def parse(self, rawdata):
        result = {'result' : []}
        for charity in rawdata:
            data = {}
            data['charityName'] = charity['charityName']
            data['tagLine'] = charity['tagLine']
            data['cause'] = charity['cause']['causeName']
            result['result'].append(data)
        return result

    def decompose_category(self, category):
        if category == 'Animals':
            return 1
        elif category == 'ArtsCultureHumanities':
            return 2
        elif category == 'Education':
            return 3
        elif category == 'Environment':
            return 4
        elif category == 'Health':
            return 5
        elif category == 'HumanServices':
            return 6
        elif category == 'International':
            return 7
        elif category == 'HumanCivilRights':
            return 8
        elif category == 'Religion':
            return 9
        elif category == 'CommunityDevelopment':
            return 10
        elif category == 'ResearchPublicPolicy':
            return 11
        else:
            return 0


    def runpipe(self, watsonresult, category):
        search = " ".join([x['title'] for x in watsonresult['keywords']])
        categoryID = self.decompose_category(category)

        if not categoryID:
            raise ValueError('Invalid category name')

        resp = self.getcharity(categoryID, search)
        formatresult = self.parse(resp)
        return formatresult
