# Given two strings s and t, return true if t is an of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "anagram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


       # res = defaultdict(int)
        # res2=[]
        # for num in nums:
        #     res[num] +=1

        # print(res)
        # sorted_by_value = dict(sorted(res.items(),key=lambda item:item[0]))
        # print(sorted_by_value)

        # for key,value in sorted_by_value.items():
        #     res2.append(value)

        # return sorted(res2)[0:k]


        #-----------------------------------
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1+ count.get(n,0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



def topKFrequent(nums, k):
    # Step 1: Count frequency
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Sort by frequency (highest first)
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Extract the first k elements
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])

    return result