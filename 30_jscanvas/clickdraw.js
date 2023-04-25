// Team ED: Emerson, Daniel
// SoftDev pd7
// K30 -- canvas based JS drawing
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
            mode = "circle";
            bToggler.innerHTML = "Circle Mode"
        }
        else{
            mode = "rect";
            bToggler.innerHTML = "Rectangle Mode"
        }
        
 }
 var drawRect = function(e) {
    console.log("drawing rectangle...")
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log(mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.rect(mouseX,mouseY,100,75);
    ctx.stroke()
    ctx.fill()
 }

 var drawCircle = function(e) {
    console.log("drawing circle...")
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log(mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(mouseX,mouseY,50,50,0,2 * Math.PI);
    ctx.stroke()
    ctx.fill()
 }

 //var draw = function(e){
var draw = (e) => {
    if (mode == "rect"){
        drawRect(e);
    }else{
        drawCircle(e);
    }
}

var wipeCanvas = (e) => {
    console.log("clearing...")
    ctx.clearRect(0, 0, c.width, c.height);
}


c.addEventListener("click", draw);

var bToggler = document.getElementById("toggle");
bToggler.addEventListener("click",toggleMode);

var clearB = document.getElementById("wipe");
clearB.addEventListener("click",wipeCanvas);
