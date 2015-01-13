=begin
2520 is the smallest number that can be divided by each of the
 numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
 all of the numbers from 1 to 20?
=end

#how do you get a number, X*x = number
#num % x == 0
#product of natural numbers have any meanining here?
# 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800
# what is the trick?
#
#create a number
#
def isdivis(n)
  divisable = []
  (1...20).each do |x|
    divisable.push(n % x == 0)
  end
  #print divisable
  if (divisable.all?)
    true
  else
    false
  end
end

p isdivis(2520)#true
p isdivis(2620)#false

def make_num(bigNum)
  n = 1;
  while(n < 3628800)
    if (isdivis(n))
      return n
    else
      n += 1
    end
  end
end

#p make_num(3628800)
#p make_num(3628800)
#p make_num((1...20).inject(:*))
p make_num(121645100408832000)

