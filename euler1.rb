#If we list all the natural numbers below 10 that are multiples of
#3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.
#
#find all the multiple of 3 below 1000
#
def mult_of_3(num)
  mult = (1...num).select do |x|
   ( x % 3 == 0) || ( x % 5 == 0)
  end
  mult.inject(:+)
end

p mult_of_3(1000) #26min, with refactoring.
