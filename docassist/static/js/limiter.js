var counter = 1;
var limit = 5;
function addSymptoms(divName) {
  if (counter == limit) {
    alert("No more than " + counter + " symptoms are acceptable.");
  }
  else {
    counter++;
    var newDiv = document.createElement('div');
    var html = "<div class=\"clearfix\"><label for=\"symptom" + counter + "\"><span>Symptom " +
                      counter + "</span></label><div class=\"input\"><input tabindex=\"1\" size=\"18\"" +
                      " id=\"symptom" + counter + "\" name=\"symptom" + counter + "\" type=\"text\" value=\"\">" +
                      "</div></div>";
    newDiv.innerHTML = html;
    document.getElementById(divName).appendChild(newDiv);
  }
}