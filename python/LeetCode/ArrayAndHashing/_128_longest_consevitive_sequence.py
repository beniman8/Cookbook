
# 128. Longest Consecutive Sequence - Explanation

# Problem Link
# Description

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4

# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7

class Solution:
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


# longest = the bigger value between:
#           (current longest) and (new sequence length)


def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start if it's the beginning of a sequence
        if num - 1 not in num_set:
            length = 1
            current = num

            while current + 1 in num_set:
                current += 1
                length += 1
            

            longest = max(longest, length)
            
            print(longest)

    return longest

longestConsecutive([0,3,2])


# For each number:

# If num - 1 is NOT in set → start counting

# Keep checking num + 1, num + 2, etc.

# Track the max length