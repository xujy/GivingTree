import json

from flask import Flask, request
from flask_cors import CORS

from watsonproxy import WatsonProxy
from charity import CharityAPI


app = Flask(__name__)
CORS(app)

watson = WatsonProxy()
charity = CharityAPI()

@app.route('/', methods=["POST"])
def GET():
    url = request.form.get('url')
    watsonresult = watson.runpipe(url)
    charity.runpipe(watsonresult)
    return '200'



if __name__ == '__main__':
    app.run()
