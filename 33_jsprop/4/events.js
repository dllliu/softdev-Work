// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //A: One event will occur -> all other events following are ignored
  //e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?
//A: The order in which the event listeners are attached doesn't matter 
//   only parameters in the eventlistener function specifying bubbling/
//   capturing matter.

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)
//A: the boolean affects the order in which the events are triggered
//   since the clicky function calls on the function to occur. 

for (var x=0; x < trs.length; x++) {
  // trs[x].addEventListener('click', clicky, true);
  trs[x].addEventListener('click', clicky, false);
}

for (x=0; x < tds.length; x++) {
  // tds[x].addEventListener('click', clicky, true);
  tds[x].addEventListener('click', clicky, false);
}


table.addEventListener('click', clicky, true);
//table.addEventListener('click', clicky, false);
