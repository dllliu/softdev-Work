var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "green";
var requestID; 

var clear = (e) => {
    ctx.clearRect(0,0,c.width,c.height);
};

var radius = 0;
var growing = true;

var drawCircle = function(e) {
    console.log("drawing circle...")
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(0,0,50,50,0,2 * Math.PI);
    ctx.stroke()
    ctx.fill()
 }

var drawDot = (e) => {
   //console.log(requestID);
   clear;
   drawCircle;
   window.requestAnimationFrame(e);
};

var stopIt = () => {

};

dotButton.addEventListener("click",drawDot);
stopButton.addEventListener("click",stopIt);