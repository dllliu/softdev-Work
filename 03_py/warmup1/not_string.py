# https://codingbat.com/prob/p189441

"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
"""
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

# test cases: do not edit
print(not_string('candy')) # 'not candy'
print(not_string('x')) # 'not x'
print(not_string('not bad')) # 'not bad'

