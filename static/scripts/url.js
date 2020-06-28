//Initiate jQuery on load.
$(function() {
    $("#url").on("click", function(e) {
      e.preventDefault();
      var imgval = document.getElementById("img-url").value
      var diagnoseRequest = { 'text': imgval, 'type': 'url' }

      if (imgval !== "") {
        $.ajax({
          url: '/diagnose',
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          dataType: 'json',
          data: JSON.stringify(diagnoseRequest),
          success: function(data) {
            document.getElementById("diagnosis-result").textContent = "";
            for (var i = 0; i < data.length; i++) {
                document.getElementById("diagnosis-result").textContent += "(" + data[i] + ")\n";
            }
          }
        });
      };
    });
  })