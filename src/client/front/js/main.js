username = "Unknown"
function searching() {
  pyObj.searchThread();
  t = setInterval("checking()",1000);
}
function checking() {
  aval = pyObj.isLogin;
  if (!aval) {
    $("#login_container").hide(1000);
    $("#chartroom_container").show(1000);
    $("#localName").text(pyObj.username);
    $("#remoteName").text(pyObj.remotename);
    pyObj.setThreads();
    clearInterval(t);
    t = setInterval("getMessage()",1000);
  } else {
    ;
  }
}

function putImage(method, ImagePath) {
  putMessage(method, '<img class="images" src="'+ ImagePath +'"height="100" width="100">');
}

function putMessage(method, content) {
  if(method == "left") {
    trueContent = '<div class="message_left"><div class="from"><span class="username">'
    + pyObj.remotename + ' </span>says:</div><div class="content"><span>'+ content +'</span></div></div>'
  } else {
    trueContent = '<div class="message_right"><div class="from"><span class="username">'
    + pyObj.username + ' </span>says:</div><div class="content"><span>'+ content +'</span></div></div>'
  }
  $("#wrap .panel-body").append(trueContent);
}

function putTitle(remoteUsername) {
  $("#username").text(remoteUsername);
}


function getMessage() {
  message = pyObj.receiveMsg;

  if(message != "") {
    var messageObj = JSON.parse(message);
    if(messageObj.type == "Text") {
      putMessage("left", messageObj.message);
    } else if(messageObj.type == "Image") {
      putImage("left", messageObj.path);
    }
  }

}

function sendMessage(message_send) {
  putMessage("right", message_send);
  pyObj.send(message_send);
}

$(document).ready(function() {
  $("#send").click(function() {
    message_send = $("#message").val();
    sendMessage(message_send)
    $("#message").val("");
    $("#extendButton").show();
  });
});
