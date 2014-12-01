var euler1 = function(start, stop) {
  var sum = 0;
    for ( var n = start; n < stop; n++) {
      if (n % 3 === 0 || n % 5 === 0){
        sum += n;
      }
    }
    return sum
};

console.log(euler1(1, 1000))



