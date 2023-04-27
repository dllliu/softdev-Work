// Team ED Exquisite Dingos: Emerson, Daniel
// SoftDev pd7
// K32 JS Animation
// 2023-04-26
// --------------------------------------------------
//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)


var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");

var requestID;

var radius = 100;
var radius_inc = 1;
var growing = true;

var drawCircle = () => {
  ctx.beginPath();
  ctx.fillStyle = "green";
  ctx.arc(c.width/2,c.height/2,radius,0,2 * Math.PI);
  ctx.stroke()
  ctx.fill()
}

var clear = function(e){
  //e.preventDefault();
  ctx.clearRect(0,0,500,500);
};

var drawDot = (e) => {
  window.cancelAnimationFrame(requestID);
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

var stopIt = function() {
    window.cancelAnimationFrame(requestID);
}

var dvdLogoSetup = function(){
  window.cancelAnimationFrame(requestID);

  var rectWidth = 100;
  var rectHeight = 50;

  var rectX = Math.floor(Math.random() * (c.width - rectWidth));
  var rectY = Math.floor(Math.random() * (c.height - rectHeight));
  //console.log(rectX);
  //console.log(rectY);

  var xVel = 2;
  var yVel = 2;

  var logo = new Image();
  logo.src = "logo_dvd.jpg";

  var dvdLogo = function(){
    ctx.clearRect(0, 0, c.width, c.height);
    ctx.fillRect(rectX, rectY, rectWidth, rectHeight);
    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);

    if(rectX >= (c.width - rectWidth) || rectX <= 0){
      xVel *= -1 ;
    }

    if(rectY >=(c.height - rectHeight) || rectY <= 0){
      yVel *= -1 ;
    }

    rectX += xVel;
    rectY += yVel;

    requestID = window.requestAnimationFrame(dvdLogo);
  };
  dvdLogo();
};

var stopIt = function() {
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);