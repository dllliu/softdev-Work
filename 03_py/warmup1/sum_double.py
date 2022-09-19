# https://codingbat.com/prob/p141905

"""
Given two int values, return their sum. Unless the two values are the same, then
return double their sum.
"""
def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum


# test cases: do not edit
print(sum_double(1, 2)) # 3
print(sum_double(3, 2)) # 5
print(sum_double(2, 2)) # 8

