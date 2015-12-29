
$(document).ready(function() {
  $("#loginButton").click(function() {
    // golabal var username
    username = $("#myname").val();

    if(username == "") {
      alert("please input username");
      return false;
    }

    $('#shclCcw').shCircleLoader({color:"white", clockwise:false});
    $('#shclCcw').css("margin", "0 auto");
    $($('.namebox')[0]).hide();
    $($(".hint")[0]).show();

    searching();

  });
});
