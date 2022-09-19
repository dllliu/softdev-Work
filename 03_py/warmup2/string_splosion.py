# https://codingbat.com/prob/p118366

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
  ans = ""
  for x in range(len(str)):
    ans += str[:x+1]
  return ans

# test cases: do not edit
print(string_splosion('Code')) # 'CCoCodCode'
print(string_splosion('abc')) # 'aababc'
print(string_splosion('ab')) # 'aab'

