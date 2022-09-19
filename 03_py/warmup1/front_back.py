# https://codingbat.com/prob/p153599

"""
Given a string, return a new string where the first and last chars have been
exchanged.
"""
def front_back(str):
  if len(str) == 0 or len(str) == 1:
    return str
  return str[-1] + str[1:-1] + str[0]

# test cases: do not edit
print(front_back('code')) # 'eodc'
print(front_back('a')) # 'a'
print(front_back('ab')) # 'ba'

