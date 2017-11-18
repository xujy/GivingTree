chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
});

function getCharities = function() {
  var xhr = new XMLHttpRequest(url);
  xhr.open("POST", url, true);

  xhr.onload = function(e) {
    alert(xhr.responseText)
  }
  xhr.onerror = function(e) {
    alert(xhr.status)
  }
}
