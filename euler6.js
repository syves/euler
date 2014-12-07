//The sum of the squares of the first ten natural numbers is,

//12 + 22 + ... + 102 = 385
//The square of the sum of the first ten natural numbers is,

//(1 + 2 + ... + 10)2 = 552 = 3025
//Hence the difference between the sum of the squares of the
//first ten natural numbers and the square of the sum is
//3025 − 385 = 2640.

//Find the difference between the sum of the squares of the
//first one hundred natural numbers and the square of the sum.)
//
//find the sum of the first 10 natural numbers? 1*1 + 2*2,
//
var difOfSquares = function(num){
  var sumSquares = 0, squareSum = 0;
  for (var i = 1; i<= num; i++){
   sumSquares += i*i;
   squareSum += i;
  }
  return squareSum * squareSum - sumSquares
}
console.log(difOfSquares(100))

