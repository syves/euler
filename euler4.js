/*A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/

var isPal = function(str) {
  return str === str.split("").reverse().join("");
};

var largestPalindrome = function(numDigits) {
  var min = Math.pow(10, numDigits - 1);
  var max = Math.pow(10, numDigits);
  var results = [];
  for (var i = min; i < max; i += 1) {
    for (var j = i; j < max; j += 1) {
      var num = i * j;
      if (isPal(String(num))) {
        results.push(num);
      }
    }
  }
  return Math.max.apply(Math, results);
};

console.log(largestPalindrome(3));
