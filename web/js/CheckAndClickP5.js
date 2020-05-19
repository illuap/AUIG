
let x1 = 0;
let y1 = 0;
let x2 = 0;
let y2 = 0;
let rec;
let dot;
let _img;
let isDrag = false;
function setup() {
  let myCanvas = createCanvas(600, 400);
  myCanvas.parent('screenSection');
  _img = loadImage('/images-screens/template1.png', drawCat);
  
}
function draw() {
  image(_img, 0, 0);
  if(rec){
    rec.show();
  }
  if(dot){
    dot.show();
  }
} 
function mousePressed(){
  
  x1 = mouseX;
  y1 = mouseY;
}
function mouseDragged() {
  x2 = mouseX - x1;
  y2 = mouseY - y1;
  rec = new imageSection(x1,y1,x2,y2);
  isDrag = true;
}
function mouseClicked(){
  if(!isDrag){
    dot = new clickDot(mouseX,mouseY);
  }else{
    isDrag = false;
  }
  
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