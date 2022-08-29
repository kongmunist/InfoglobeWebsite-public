// This loads in a text file as a string
function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  return result;
}

// Get the last time the Infoglobe accessed this website
function writeLastAccessed(){
    timeStr = loadFile("static/lastLogged.txt");
    lastTime = new Date(parseInt(timeStr + "000"));
    timeShowcase = document.getElementById("lastAccessed");

//    timestr =
//    datestr = lastTime.toLocaleDateString([], {dateStyle:"long"});
    timeShowcase.innerHTML = "Infoglobe Last Visit Time: "
                + lastTime.toLocaleTimeString([], {timeStyle:"short"})
                + ", "
                + lastTime.toLocaleDateString([], {dateStyle:"long"});
}

document.addEventListener("DOMContentLoaded", function(event) {
    writeLastAccessed();
})
