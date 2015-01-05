#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143

def is_prime_number(num)
  (2...num).all? {|n| num % n != 0}# has factors
end

p is_prime_number(5)# true
p is_prime_number(4)#false

def get_factors(number)
  prime_factors = []
  number_sq = Math.sqrt(number).floor
  factors = (2..number_sq).each do |x|
    if (number % x == 0) && (is_prime_number(x) == true)
      prime_factors << x
    end
  end
  prime_factors.max
end

p get_factors(600851475143)# 2 hrs with a hangover and lots of
#refactoring
#
#Don't forget about :
#
#Prime.prime?(num) => true/false
#and
#
#Prime.each(num) do |prime|
#p prime #=> 2,3,5,7...97
#end

