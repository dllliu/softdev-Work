# https://codingbat.com/prob/p182414

"""
Given 2 strings, a and b, return the number of the positions where they contain
the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx",
"aa", and "az" substrings appear in the same place in both strings.
"""
def string_match(a, b):
  len_a = len(a)
  len_b = len(b)
  shorter = a
  longer = b
  if(len_a > len_b):
    shorter = b
    longer = a
  count = 0
  for char in range(len(shorter)-1):
    if (shorter[char] == longer[char] and shorter[char+1] == longer[char+1]):
      count += 1
  return count

# test cases: do not edit
print(string_match('xxcaazz', 'xxbaaz')) # 3
print(string_match('abc', 'abc')) # 2
print(string_match('abc', 'axc')) # 0

