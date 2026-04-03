'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

 

Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100

 







stack keeps indices of temperatures that are waiting for a warmer day.

'''
def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # will store indices

    # get he index and the temperature 
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer



'''
Walkthrough Example

Input:

[73,74,75,71,69,72,76,73]

Process:

Day 0: 73 -> push index 0
Day 1: 74 -> warmer than 73 -> answer[0] = 1
Day 2: 75 -> warmer than 74 -> answer[1] = 1
Day 3: 71 -> push
Day 4: 69 -> push
Day 5: 72 -> warmer than 69, 71 -> answer[4]=1, answer[3]=2
Day 6: 76 -> warmer than 72, 75 -> answer[5]=1, answer[2]=4
Day 7: 73 -> push

Final Output:

[1,1,4,2,1,1,0,0]

'''
