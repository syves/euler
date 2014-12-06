//2520 is the smallest number that can be divided by each
//of the numbers from 1 to 10 without any remainder.

//What is the smallest positive number that is evenly
//divisible by all of the numbers from 1 to 20?

//check if divisable
var isDivisable = function(start, stop, smallest){
  for (var i = start; i < stop; i++){
    if (smallest % i != 0){
      return false
    }
  }
  return true;
};

var getSmallest = function(start, stop, smallest){
// from 1 until first number divisable by 1..10
  for (var smallest= 1; ; smallest++){
    if (isDivisable(start, stop, smallest)){
      return smallest;
    }
  }
}
console.log(getSmallest(1,20,1))

