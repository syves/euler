//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

//Find the sum of all the primes below two million.
//
var isPrime = function(number, smallerPrimes){
  for (var idx = 0; idx < smallerPrimes.length; idx++){
    if (number % smallerPrimes[idx] == 0){
      return false;
    }
  }
  return true;
}

var sumPrimes_ = function(stop){
  var sum = 0, primes = [];
  for (var m = 2; m <= stop; m++){
    if (isPrime(m, primes)){
      primes.push(m);
      sum += m;
    }
  }
  return sum;
}
//console.log(sumPrimes(2000000))

//30 min. initial solution dec.8th





























function sumPrimes(stop) {

  var state = [true, true];  // 0 and 1 are not prime
  for (var n = state.length; n < stop; n++) {
    state[n] = false;
  }

  for (var n = 2; n < stop; n++) {
    if (!state[n]) {
      for (var m = n + n; m < stop; m += n) {
        state[m] = true;
      }
    }
  }
  return state.reduce(function(sum, marked, n) {
    return marked ? sum : sum + n;
  },0);
}
console.log(sumPrimes(2000000))


