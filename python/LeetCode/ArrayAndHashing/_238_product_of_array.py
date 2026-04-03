'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]



'''


def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
    
    # Step 1: Left products
    left = 1
    for i in range(n):
        output[i] = left
        left *= nums[i]
    
    # Step 2: Right products
    right = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right
        right *= nums[i]
    
    return output


'''MY EXPLANATION


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # take the length of the array so we can use it to loop through the numbers on the list
        length_of_array = len(nums)

        # create an array of the same length as the list with all one cause anything times one is itself
        result = [1] * length_of_array
        
        This is the starting result we make 
        [1,1,1,1]

        
        #Calculate the left product of the array from the number[i]
        
        #start at one
        left = 1
        
        #loop through the numbers on the left side of nums[i]    [1,2,nums[i],3,4] so 1 and 2 
        for i in range(length_of_array):
            result[i] = left
            print(result)
            left *= nums[i]
            
            take the value on the right side and multiply it by the value on the left side

        print(left)
        
        This is what it is doing in that loop
        [1, 1, 1, 1]
        [1, 1, 1, 1]
        [1, 1, 2, 1]
        [1, 1, 2, 6]

        # now the right products 

        right = 1 

        #looping the right has to be done the opposite way  <-- so we need to loop backward range(start, stop, step)
        #start at the end of our array so length of the array minus 1 .. the arrays start counting at 0 us at 1
        start = length_of_array -1
        stop =-1 # stop when you reach -1
        step=-1 #reverse the array by starting at -1
        for i in range(start, stop, step):
            result[i] *= right
            print(result)
            right *=nums[i]
            
        This is what it is doing in this loop
        [1, 1, 2, 6]
        [1, 1, 8, 6]
        [1, 12, 8, 6]
        [24, 12, 8, 6]
        
        return result






'''

def productExceptSelf( nums):
        # take the length of the array so we can use it to loop through the numbers on the list
        length_of_array = len(nums)

        # create an array of the same length as the list with all one cause anything times one is itself
        result = [1] * length_of_array

        
        #Calculate the left product of the array from the number[i]
        
        #start at one
        left = 1
        
        #loop through the numbers on the left side of nums[i]    [1,2,nums[i],3,4] so 1 and 2 
        for i in range(length_of_array):
            result[i] = left
            left *= nums[i]

        # now the right products 

        right = 1 

        #looping the right has to be done the opposite way  <-- so we need to loop backward range(start, stop, step)
        #start at the end of our array so length of the array minus 1 .. the arrays start counting at 0 us at 1
        start = length_of_array -1
        stop =-1 # stop when you reach -1
        step=-1 #reverse the array by starting at -1
        for i in range(start, stop, step):
            
            result[i] *= right
            right *=nums[i]        
        return result

productExceptSelf([1,2,4,6])