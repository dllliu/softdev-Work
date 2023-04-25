// Team Aggregate Dinosaurs :: Anjini Katari, Daniel Liu
// SoftDev pd7
// K31 JS Paint, Paint, Paint...
// 2023-04-25
// --------------------------------------------------

var c = document.getElementById("playground"); //GET CANVAS
var dotButton = document.getElementById("buttonCircle"); //GET DOT BUTTON
var stopButton = document.getElementById("buttonStop"); //GET STOP BUTTON

var ctx = c.getContext("2d");

ctx.fillStyle = "green";
var requestID; //init global var for use with animation frames

var clear = (e) => {
    ctx.clearRect(0,0,c.width,c.height);
};

var radius = 100;
var radius_inc = 1;
var growing = true;

var drawCircle = () => {
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(c.width/2,c.height/2,radius,0,2 * Math.PI);
    ctx.stroke()
    ctx.fill()
 }

var drawDot = (e) => {
    requestID = window.requestAnimationFrame(drawDot);
    clear();
    drawCircle();
    if (growing) {
        if (radius > c.width / 2) { //if too big
            growing = false;
        }
        radius += radius_inc;
    } 
    else {
        radius -= radius_inc;
        if (radius == 0) {  //other side when growing is set to false
            growing = true
        }
    }
};

var once = true;
var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click",drawDot,once);

stopButton.addEventListener("click",stopIt,once);