function sendData(data) {
    var XHR = new XMLHttpRequest();
    var FD  = new FormData();

    // We push our data into our FormData object
    for(name in data) {
      FD.append(name, data[name]);
    }

    // We define what will happen if the data are successfully sent
/*    XHR.addEventListener('load', function(event) {
      alert('Yeah! Data sent and response loaded.');
    });

    // We define what will happen in case of error
    XHR.addEventListener('error', function(event) {
      alert('Oups! Something goes wrong.');
    });
*/
    // We setup our request
    XHR.open('POST', 'http://localhost:5000');

    // We just send our FormData object, HTTP headers are set automatically
    XHR.send(FD);
}

var toggleBtn = document.getElementById("toggleLED");

toggleBtn.onmousedown = function() {
	sendData({state:"on"});
};

toggleBtn.onmouseup = function() {
	sendData({state:"off"});
};