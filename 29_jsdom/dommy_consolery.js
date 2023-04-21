// Team Aggregate Dinosaurs :: Anjini Katari, Daniel Liu
// SoftDev pd7
// K29 --DOM and stuff
// 2023-04-20
// --------------------------------------------------
//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
}; 


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024, //this seems like a dictionary assigned to a variable, but why does only name have quotations? 
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          } //we can put functions inside a dictionary? is this even a dictionary?
        }; 


var addItem = function(text) {
  var list = document.getElementById("thelist"); //this is an HTML ID Tag. in index.html it is for the <ol> or ordered list
  var newitem = document.createElement("li"); 
  newitem.innerHTML = text; //we are adding a entry of the text inside the ordered list with the JS function
  list.appendChild(newitem);
};

var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove(); //we are removing an entry inside the ordered list by index
};


var red = function() {
  //for every element inside the ordered list, we are adding "red"
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){ //if index is even, add red. otherwise blue
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//Fib
function fib(n){
  if (n == 0 || n == 1){
      return n
  }else{
      return (fib(n-1) + fib(n-2))
  }
}

//Fact
function fact(n){
  if (n <= 1){
      return 1
  }else{
      return (n * fact(n-1))
  }
}

// GCD
function gcd(a,b){
  if (b == 0){
    return a
  }else{
    return gcd(b,a % b)
  }
}

var addFib = function(text) {
  var list = document.getElementById("div1"); //this is an HTML ID Tag. in index.html it is for the <ol> or ordered list
  var newitem = document.createElement("li"); 
  newitem.innerHTML = "The third term in the Fibonacci Sequence is " + fib(3); //we are adding a entry of the text inside the ordered list with the JS function
  list.appendChild(newitem);
};

var addFact = function(text) {
  var list = document.getElementById("div2"); //this is an HTML ID Tag. in index.html it is for the <ol> or ordered list
  var newitem = document.createElement("li"); 
  newitem.innerHTML = "3! is " + fib(3); //we are adding a entry of the text inside the ordered list with the JS function
  list.appendChild(newitem);
};

var addGcd = function(text) {
  var list = document.getElementById("div3"); //this is an HTML ID Tag. in index.html it is for the <ol> or ordered list
  var newitem = document.createElement("li"); 
  newitem.innerHTML = "GCD of 12 and 18 is " + gcd(12,18); //we are adding a entry of the text inside the ordered list with the JS function
  list.appendChild(newitem);
};

//making a variable referring to a button
var dasfib = document.getElementById("b_fib");
//call the function that contains addFib()
dasfib.addEventListener('click', () => {addFib()
});


var dasfact = document.getElementById("b_fact");
dasfact.addEventListener('click', () => {addFact()
});

var dasgcd = document.getElementById("b_gcd");
dasgcd.addEventListener('click', () => {addGcd()
});