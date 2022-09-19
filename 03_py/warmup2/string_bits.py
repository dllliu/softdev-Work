# https://codingbat.com/prob/p113152

"""
Given a string, return a new string made of every other char starting with the
first, so "Hello" yields "Hlo".
"""
def string_bits(str):
  ans = ""
  for x in range(len(str)):
    if (x % 2 == 0):
      ans += str[x:x+1]
  return ans

# test cases: do not edit
print(string_bits('Hello')) # 'Hlo'
print(string_bits('Hi')) # 'H'
print(string_bits('Heeololeo')) # 'Hello'

