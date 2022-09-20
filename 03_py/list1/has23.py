# https://codingbat.com/prob/p177892

"""
Given an int array length 2, return True if it contains a 2 or a 3.
"""
def has23(nums):
  for x in nums:
    if(x == 2) or (x==3):
      return True
  return False

# test cases: do not edit
print(has23([2, 5])) # True
print(has23([4, 3])) # True
print(has23([4, 5])) # False

