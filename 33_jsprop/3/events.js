// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // A: stop future calls of clicky -> it'll only work once
  // e.stopPropagation();
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)

table.addEventListener('click', clicky, true);
// table.addEventListener('click', clicky, false);
//False is bubbling and True is capturing (?)


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// when true, the order is table, name, row 
// when false, the order is name, the row, table
