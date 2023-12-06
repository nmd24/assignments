function mathMethods(value) {
  console.log("Original Value:", value);

  console.log("After round():", Math.round(value));
  console.log("After ceil():", Math.ceil(value));
  console.log("After floor():", Math.floor(value));
  console.log("After random():", Math.random());
  console.log("After max():", Math.max(5, 10, 15));
  console.log("After min():", Math.min(5, 10, 15));
  console.log("After pow():", Math.pow(value, 2));
  console.log("After sqrt():", Math.sqrt(value));
  console.log("After abs():", Math.abs(value));
  console.log("After exp():", Math.exp(value));
  console.log("After log():", Math.log(value));
  console.log("After log10():", Math.log10(value));
  console.log("After sin():", Math.sin(value));
  console.log("After cos():", Math.cos(value));
  console.log("After tan():", Math.tan(value));
  console.log("After asin():", Math.asin(value));
  console.log("After acos():", Math.acos(value));
  console.log("After atan():", Math.atan(value));
  console.log("After atan2():", Math.atan2(10, value)); 
  console.log("After hypot():", Math.hypot(3, 4)); 
  console.log("After trunc():", Math.trunc(value));
  console.log("After sign():", Math.sign(value));
}

// Example Usage for Math Methods
mathMethods(4.56);
mathMethods(-9);
mathMethods(0);
mathMethods(Math.E);