//The prime factors of 13195 are 5, 7, 13 and 29.

//What is the largest prime factor of the number 600851475143 ?
  //
  var isPrime = function(num){
    for (var n= 2; n < num; n++){
      if (num % n === 0) {
        return false
      } else {
        return true
    }
}

isPrime(5)

5 % 2 > 0 && 5 % 3 > 0 && 5 % 4 > 0

isPrime(6)

6 % 2 > 0 && 6 % 3 > 0 && 6 % 4 > 0 && 6 % 5 > 0


var getLargestPrime = function(number) {
  var num = 1
  while (num < number) {
    var largestPrime = 0;
    if (num % 2 != 0) {
      largestPrime = num;
      num += 1;
    }
  }
  console.log(largestPrime)
  return largestPrime
}

//console.log(getLargestPrime(13195))
