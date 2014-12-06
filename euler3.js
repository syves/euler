//The prime factors of 13195 are 5, 7, 13 and 29.

//What is the largest prime factor of the number 600851475143 ?
  //tests for prime numbe
  var isPrime = function(num){
    for (var n= 2; n < num; n++){
      if (num % n === 0) {
        return false
      }
    }
    return true
}
//number // num(which is smallest prime factor) == largest prime
var getLargestPrime = function(number) {
  var sqrt = Math.sqrt(number), smallFactors = [];
  for (var small_num = 2; small_num <= sqrt; small_num++){
    if (number % small_num === 0){
      if (isPrime(number / small_num)) {
        return number/small_num;
      }
      smallFactors.push(small_num)
    }
  }
  for (var idx = smallFactors.length - 1; idx >= 0; idx--){
    if (isPrime(smallFactors[idx])) {
      return smallFactors[idx];
    }
  }
}

console.log(getLargestPrime(600851475143))
