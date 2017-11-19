var loadResult = function(jsonresult) {
  for(var i = 0; i < jsonresult['result'].length; i++) {
    var tmpl = document.getElementById('result-template').content.cloneNode(true);
    tmpl.querySelector('.name').innerText = jsonresult['result'][i]['charityName']
    tmpl.querySelector('.tagline').innerText = jsonresult['result'][i]['tagLine']
    tmpl.querySelector('a').href = jsonresult['result'][i]['charityNavigatorURL']
    var obj = document.getElementsByClassName('results')[0]
    obj.appendChild(tmpl);
  }
}

function getCurrentTab(callback) {
  chrome.tabs.query({'active': true, 'lastFocusedWindow': true},
  function (tabs) {
      callback(tabs[0].url)
  })
}

function getCharities(url) {
  var xhr = new XMLHttpRequest();
  var formData = new FormData();
  formData.append('url', url)
  xhr.open('POST','https://givingtree-api.herokuapp.com', true);
  xhr.onload = function(e) {
    var result = JSON.parse(xhr.responseText)
    loadResult(result);
  }
  xhr.onerror = function(e) {
    alert(xhr.status)
  }
  xhr.send(formData)
}

getCurrentTab(getCharities)
