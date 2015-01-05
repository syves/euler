#Each new term in the Fibonacci sequence is generated by adding the
#previous two terms. By starting with 1 and 2, the first 10 terms
#will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
#
def get_all_fibs(num)
  a = 1; b = 2; c = 0;
  fibs = [a, b];
  while ((c = a + b) < num)
    fibs << c;
    a = b;
    b = c;
  end
  fibs.select {|x| x.even?}.inject(:+)
end

p get_all_fibs(4000000) 31mins
