username = "Unknown"
function searching() {
  $("#login_container").delay(1000).hide(1000);
  $("#chartroom_container").delay(1000).show(1000);
}

function putMessage(username, method, content) {
  if(method == "left") {
    trueContent = '<div class="message_left"><div class="from"><span class="username">'
    + username + ' </span>says:</div><div class="content"><span>'+ content +'</span></div></div>'
  } else {
    trueContent = '<div class="message_right"><div class="from"><span class="username">'
    + username + ' </span>says:</div><div class="content"><span>'+ content +'</span></div></div>'
  }
  $("#wrap .panel-body").append(trueContent);
}

function putTitle(remoteUsername) {
  $("#username").text(remoteUsername);
}

//
// function getMessage() {
//   message = pyObj.receiveMsg;
//
//   if(message != "") {
//     put(message);
//   }
//
// }

function sendMessage(message_send) {
  putMessage(username, "right", message_send);
  // pyObj.send(message_send);
}

$(document).ready(function() {
  $("#send").click(function() {
    message_send = $("#message").val();
    sendMessage(message_send)
    $("#message").val("");
  });
});
