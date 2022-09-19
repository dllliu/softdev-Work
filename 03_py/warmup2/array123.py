# https://codingbat.com/prob/p193604

"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears
in the array somewhere.
"""
def array123(nums):
  for i in range(len(nums)-2):
    if (nums[i] ==1 and nums[i+1] ==2 and nums[i+2] ==3):
      return True
  return False

# test cases: do not edit
print(array123([1, 1, 2, 3, 1])) # True
print(array123([1, 1, 2, 4, 1])) # False
print(array123([1, 1, 2, 1, 2, 3])) # True

