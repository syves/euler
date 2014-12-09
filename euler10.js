//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

//Find the sum of all the primes below two million.
//
var isPrime = function(number){
  for (var n = 2; n < number; n++){
    if (number % n === 0){
      return false;
    }
  }
  return true;
}

var sumPrimes = function(stop){
  var sum = 0;
  for (var m = 2; m <= stop; m++){
    if (isPrime(m)){
      sum += m;
      }
    }
    return sum
  }
console.log(sumPrimes(2000))

//30 min. initial solution dec.8th
