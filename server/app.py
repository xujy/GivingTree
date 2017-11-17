import json

from flask import Flask, request
from flask_cors import CORS

from language_understanding import LanguageUnderstanding
from charity_navigator import CharityNavigator

app = Flask(__name__)
CORS(app)

lanUn = LanguageUnderstanding()
charity = CharityNavigator()

@app.route('/', methods=["POST"])
def GET():
    url = request.form.get('url')
    unRes = lanUn.runpipe(url)
    charity.runpipe(unRes)
    return '200'

if __name__ == '__main__':
    app.run()
