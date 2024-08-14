var timeDisplay = document.getElementById("time");


function refreshTime() {
  var dateString = new Date().toLocaleString("uk-UA", {timeZone: "Europe/Kyiv"});
  var formattedString = dateString.replace(", ", " - ");
  timeDisplay.innerHTML = formattedString;
}

setInterval(refreshTime, 1000);