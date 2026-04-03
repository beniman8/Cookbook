'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]



'''
def largestRectangleArea(heights):
    stack = []
    max_area = 0

    heights.append(0)  # sentinel to flush stack

    for i, h in enumerate(heights):

        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = height * width
            max_area = max(max_area, area)

        stack.append(i)

    return max_area