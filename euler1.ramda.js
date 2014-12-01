var R = require('ramda');

var divisibleBy = R.curry(function(denom, numer) {
  return numer % denom === 0
});

var euler1 = R.pipe(R.range,
                    R.filter(R.or(divisibleBy(3), divisibleBy(5))),
                    R.sum);

console.log(euler1(1, 1000))
