// Team ED: Emerson, Daniel
// SoftDev pd7
// K30 
// 2023-04-24
// --------------------------------------------------
//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)


 //retrieve node in DOM via ID
 var c = document.getElementById("slate");

 //instantiate a CanvasRenderingContext2D object
 var ctx = c.getContext("2d");

 //init global state var 
 var mode = "rect";

 //var toggleMode = function(e) {
    var toggleMode = (e) => {
        console.log("toggling...");
        if(mode=="rect"){
            mode = "circles";
        }
        else{
            mode = "rect";
        }
        
 }
 var drawRect = function(e) {
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log(mouseX, mouseY);

 }

 drawRect()

 var drawCircle = function(e) {
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log(mouseX, mouseY);
    arc(mouseX,mouseY,20,0,360);
 }

 //var draw = function(e){
var draw = (e) => {
}

var wipeCanvas = (e) => {
}


c.addEventListener("click", draw);
var bToggler = document.getElementById("rect");
bToggler. ;
var clearB = :
clearB. ;
