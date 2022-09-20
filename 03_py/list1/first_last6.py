# https://codingbat.com/prob/p181624

"""
Given an array of ints, return True if 6 appears as either the first or last
element in the array. The array will be length 1 or more.
"""
def first_last6(nums):
  first = nums[0]
  last = nums[len(nums)-1]
  return (first == 6 or last == 6)

# test cases: do not edit
print(first_last6([1, 2, 6])) # True
print(first_last6([6, 1, 2, 3])) # True
print(first_last6([13, 6, 1, 2, 3])) # False

