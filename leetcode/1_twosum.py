'''
DISCLAMAIR:
The is my personal solution to Leetcode problem.

Leetcode Problem 1
Description: The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
__author__ = 'srikantadatta'

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        input_list = []
        for i in range(len(num)):
            input_list.append((i,num[i]))
        input_list = sorted (input_list, key = lambda input_list:input_list[1])
        print input_list

        #initialize two pointers
        beg = 0
        end = len(input_list)-1
        while beg<end:
            if input_list[beg][1] + input_list[end][1] == target:
                print "index1=%s,index2=%s" %(str(input_list[beg][0]),str(input_list[end][0]))
                break
            if input_list[beg][1] + input_list[end][1] < target:
                beg = beg + 1
            if input_list[beg][1] + input_list[end][1] > target:
                end = end - 1

        return "index1=-1,index2=-1"
