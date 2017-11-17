var apis = {
  natlang: {
    "service_uri": "https://gateway.watsonplatform.net/natural-language-understanding/api",
    "username": "cac72f87-4a20-45c6-9b45-0305632c0bfc",
    "password": "K0ILmZ3JqLiN",
  }
}
apis.natlang.cred = btoa(apis.natlang.username + ":" + apis.natlang.password);

function callWatson(options, successCallBack, errorCallBack) {
  fetch(options.uri, {
    method: options.method,
    headers: {
      "Authorization": "Basic " + options.cred,
      "content-type" : options.reqType,
      "Accept": options.respType,
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": true,
      "Access-Control-Allow-Methods": "GET, OPTIONS",
      "Access-Control-Allow-Headers": "access-control-allow-headers,access-control-allow-methods,access-control-allow-origin,access-control-expose-headers,authorization,content-type",
      "Access-Control-Expose-Headers": "Authorization"
    },
    body: options.body
  }).then(function (response) {
    if (response.status === 200 || response.status === 206) {
        alert(response.json());
    } else {
        alert("ERROR");
    }
  });
}

function analyzeLang(reqURL) {
  var options = {};
  options.method = "GET";
  options.reqType = "application/json";
  options.respType = "application/json";
  options.uri = reqURL;
  options.cred = apis.natlang.cred
  options.metho = "GET";
  callWatson(options, function(resp) {
    alert(resp);
  }), alert("callWatson failed");
}
