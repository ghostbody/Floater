$(document).ready(function() {
  $("#extendButton").click(function() {
    var imageName = pyObj.imageName;
    if(imageName == "" || imageName == "None") {
      alert("please input image")
    } else {
      putImage("right", imageName);
    }
  });

  $("body").on("click", ".images", function(e) {
    $('#myModal').modal('show');
    var target = $(e.target);
    $("#big-image").attr("src", target.attr("src"));
  });

  $("#message").val("");

  $("#message").keyup(function() {
    if($("#message").val() == "") {
      $("#extendButton").show();
      $("#messageButton").hide();
    } else {
      $("#extendButton").hide();
      $("#messageButton").show();
    }
  });

});
