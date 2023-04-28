// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
    //alert -> brings up a pop up with whatever is taken as a parameter in the function
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}
