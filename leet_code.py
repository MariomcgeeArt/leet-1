#Given an array of integers, return indices of the two numbers such that they add up to a specific target,

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].





# Restate the Problem:
# The Problem ask to return the indexes of the two numbers in a list or array thats sum exuals a target value
# so i must find two numbers in a list that when added their total is equal to my target number and return their index placment back of where they are in the array or list.


#starter code
#(Personal thoughts)--- even tho this is listed as an easy problem i am looking at this and am already wondering why they decided to use a class to start ...I would hav e put it in a function and thats it.


class Solution(object):
    def twoSum(self, nums, target):
        """
         :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
# this is the brute force solution in which we search through the array and compare the numbers to ++1 to the previous to see if it matches the target. not sure the 
        for a in range(0, len(nums)):
            for b in range(1,len(nums)):
                if nums[a] + nums[b] == target and b != a:
                    return [a,b]



                    

