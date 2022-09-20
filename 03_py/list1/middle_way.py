# https://codingbat.com/prob/p171011

"""
Given 2 int arrays, a and b, each length 3, return a new array length 2
containing their middle elements.
"""
def middle_way(a, b):
  mid_a = a[1]
  mid_b = b[1]
  ans = [mid_a,mid_b]
  return ans

# test cases: do not edit
print(middle_way([1, 2, 3], [4, 5, 6])) # [2, 5]
print(middle_way([7, 7, 7], [3, 8, 0])) # [7, 8]
print(middle_way([5, 2, 9], [1, 4, 5])) # [2, 4]

