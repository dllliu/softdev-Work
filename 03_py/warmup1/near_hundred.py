# https://codingbat.com/prob/p124676

"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
computes the absolute value of a number.
"""
def near_hundred(n):
  if abs(100-n) <= 10:
    return True
  if abs(200-n) <= 10:
    return True
  else:
    return False

# test cases: do not edit
print(near_hundred(93)) # True
print(near_hundred(90)) # True
print(near_hundred(89)) # False

