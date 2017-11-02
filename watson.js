var apis = {
  natlang: { "url": "https://gateway.watsonplatform.net/natural-language-understanding/api",
    "username": "cac72f87-4a20-45c6-9b45-0305632c0bfc",
    "password": "K0ILmZ3JqLiN" }
}

apis.toneAnalyzer.auth.cred = btoa(apis.toneAnalyzer.auth.username + ":" + apis.toneAnalyzer.auth.password);

function callWatson(options, successCallBack, errorCallBack) {
  fetch(options.uri, {
    method: options.method,
    headers: {
      "Authorization": "Basic " + options.cred,
      "Content-Type" : options.reqType,
      "Accept": options.respType
    },
    // TODO complete parameters of request

  }).then(function (response) {
    if (response.status === 200 || response.status === 206) {
      response.json().then(successCallBack);
    } else {
        errorCallBack("ERROR");
    }
  });
}

function analyzeLang(reqURL) {
  var options;
  options.method = "GET";
  options.reqType = "application/json";
  options.respType = "application/json";

  //TODO complete options fields.

  options.cred = apis.toneAnalyzer.auth.cred;

  callWatson(options, function(resp) {
    alert(resp);
  }), alert("callWatson failed");
}
