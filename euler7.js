//By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
//we can see that the 6th prime is 13.

//What is the 10 001st prime number?

var isPrime = function(num) {
  for (var m = 2; m < num; m++) {
    if (num % m === 0) {
      return false;
    }
  }
  return true;
}
console.log(isPrime(5))
console.log(isPrime(7927))

var largePrime = function(number){
  var count = 0;
  for (var n = 2; count < number; n++){
    //prime and count is less than number keep looking
    if (isPrime(n)){
      count += 1;
    }
  }
  console.log(count)
  return n-1;
}

console.log(largePrime(10001))
