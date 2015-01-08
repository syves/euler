#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two
#2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two
  # 3-digit numbers.
#
def isPal(num)
  num.to_s == num.to_s.reverse
end

def makePal
  largePal = [];
  (99..999).each do |i|
    (99..999).each do |j|
      if (isPal(i*j))
        largePal << i*j.to_i;
      end
    end
  end
  largePal.max
end

p makePal
