import json

from flask import Flask, request
from flask_cors import CORS

from watsonproxy import WatsonProxy


app = Flask(__name__)
CORS(app)

watson = WatsonProxy()

@app.route('/', methods=["POST"])
def GET():
    url = request.form.get('url')
    watson.runpipe(url)
    return '200'


if __name__ == '__main__':
    app.run()
