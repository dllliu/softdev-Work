# https://codingbat.com/prob/p167025

"""
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come
immediately after a 13 also do not count.
"""
def sum13(nums):
    add = True
    sum = 0
    
    for num in nums:
        if num == 13:
            add = False
        elif add:
            sum += num
        else:
            add = True

    return sum

# test cases: do not edit
print(sum13([1, 2, 2, 1])) # 6
print(sum13([1, 1])) # 2
print(sum13([1, 2, 2, 1, 13])) # 6

