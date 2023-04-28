// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');
// td = table data cell 
var trs = document.getElementsByTagName('tr');
// tr = table roow cell
var table = document.getElementsByTagName('table')[0];
// first element in the table 

var clicky = function(e) {
  alert( this.innerHTML );

};

for (var x=0; x < tds.length; x++) {
  //event listener to ever element 
  tds[x].addEventListener('click', clicky);
  console.log("first");
}

for (x=0; x < trs.length; x++) {
  //event listener for each row
  trs[x].addEventListener('click', clicky);
  console.log("second");
}

table.addEventListener('click', clicky);
// eventlistener for 1 element


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// 