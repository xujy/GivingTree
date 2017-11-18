import json

from flask import Flask, request
from flask_cors import CORS

from language_understanding import LanguageUnderstanding
from language_classifier import LanguageClassifier
from charity_navigator import CharityNavigator

app = Flask(__name__)
CORS(app)

language_classifier = LanguageClassifier()
language_understanding = LanguageUnderstanding()
charity_navigator = CharityNavigator()

@app.route('/', methods=["POST"])
def GET():

    url = request.form.get('url')
    res = language_understanding.runpipe(url)
    category = language_classifier.classify(json.loads(res))
    return json.dumps(charity_navigator.runpipe(json.loads(res), category))

if __name__ == '__main__':
    app.run(debug=True)
