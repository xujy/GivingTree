/*chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
});
*/


var getCharities = function(url) {
  var xhr = new XMLHttpRequest();
  var formData = new FormData();
  formData.append('url', url)
  xhr.open('POST','https://givingtree-api.herokuapp.com', true);

  xhr.onload = function(e) {
    alert(xhr.responseText)
  }
  xhr.onerror = function(e) {
    alert(xhr.status)
  }
  xhr.send(formData)
}
