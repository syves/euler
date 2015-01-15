=begin
2520 is the smallest number that can be divided by each of the
 numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
 all of the numbers from 1 to 20?
=end

def factorize(num, factors)# 20
  if (num == 1)
    factors
  else
    factor = (2..num).find {|x|num % x == 0 }
    factors << factor
    factorize(num/factor, factors)
  end
end

def euler5(num)
  lists = (1..num).map {|n| factorize(n, [])}

  (2..num).map {|x| x ** lists.map {|list|list.count(x)}.max}
  .reject{|x| x == 0 }.inject(1, :*)
end

p euler5(20)

