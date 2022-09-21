# https://codingbat.com/prob/p119308

"""
Given an array of ints, return True if the array contains a 2 next to a 2
somewhere.
"""
def has22(nums):
    for idx, num in enumerate(nums):
        if num == 2:
            if (idx != 0 and nums[idx - 1] == 2) or (idx != len(nums) - 1 and nums[idx + 1] == 2):
                return True

    return False


# test cases: do not edit
print(has22([1, 2, 2])) # True
print(has22([1, 2, 1, 2])) # False
print(has22([2, 1, 2])) # False

