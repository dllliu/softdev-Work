# https://codingbat.com/prob/p192589

"""
Given an array of ints, return the sum of the first 2 elements in the array. If
the array length is less than 2, just sum up the elements that exist, returning
0 if the array is length 0.
"""
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) < 2:
    return nums[0]
  else:
    sum = 0
    for x in range(2):
      sum += nums[x]
    return sum

# test cases: do not edit
print(sum2([1, 2, 3])) # 3
print(sum2([1, 1])) # 2
print(sum2([1, 1, 1, 1])) # 2

