# https://codingbat.com/prob/p145834

"""
Given a string, return the count of the number of times that a substring length
2 appears in the string and also as the last 2 chars of the string, so "hixxxhi"
yields 1 (we won't count the end substring).
"""
def last2(str):
  count = 0
  end = str[len(str)-2:]
  for char in range(len(str)):
    if (str[char:char+2] == end):
      count += 1
  if(count == 0):
    return 0
  return count -1

# test cases: do not edit
print(last2('hixxhi')) # 1
print(last2('xaxxaxaxx')) # 1
print(last2('axxxaaxx')) # 2

