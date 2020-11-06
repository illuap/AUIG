
let x1 = 0;
let y1 = 0;
let x2 = 0;
let y2 = 0;
let rec;
let dot;
let _img;
let _img2 = null;
let isDrag = false;

let isSSTaken = document.getElementById('isSSTaken').value;



function setup(x=600,y=400) {
  let myCanvas = createCanvas(x, y);
  myCanvas.parent('screenSection');
  myCanvas.mousePressed(mousePressed1);
  myCanvas.mouseClicked(mouseClicked1);
  loadDefault();
}
function draw() {
  isSSTaken = document.getElementById('isSSTaken').value;
  if( isSSTaken == "0"){ // TODO optimize this loading? but hey it works...
    image(_img, 0, 0);
  }
  else{
    if(_img2 == null)
      loadSS()
    image(_img2, 0, 0);
  }


  if(rec){
    rec.show();
  }
  if(dot){
    dot.show();
  }
} 
function mousePressed1(){
  
  x1 = mouseX;
  y1 = mouseY;
}
function mouseDragged() {
  //TODO inconsistent issue when dragging things outside.

  if(mouseX >= 0 && mouseY >= 0){
    x2 = mouseX - x1;
    y2 = mouseY - y1;
    rec = new imageSection(x1,y1,x2,y2);
  }
  isDrag = true;

}
function mouseClicked1(){
  if(!isDrag){
    dot = new clickDot(mouseX,mouseY);
  }else{
    isDrag = false;
  }
}

function loadDefault(){
  _img = loadImage('/images-screens/TEST.png', drawCat);
}
function loadSS(){
  _img2 = loadImage('/images-screens/TEST.png',drawCat);
}

function drawCat(img) {
  image(img, 0, 0);
}


class imageSection{
  constructor(_x1 = 0, _y1 = 0, _x2 = 0, _y2 = 0) {
    this.x1 = _x1;
    this.y1 = _y1;
    this.x2 = _x2;
    this.y2 = _y2;
  }

  show() {
    stroke(255,0,0);
    strokeWeight(1);
    fill(80, 80);
    rect(this.x1, this.y1,this.x2,this.y2);
  }

}
class clickDot{
  constructor(_x = 0, _y = 0) {
    this.x = _x;
    this.y = _y;
  }

  show() {
    stroke(0);
    fill(0,255,0);
    ellipse(this.x, this.y,10);
  }
}