#Neetcode solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #remove duplicates
        numSet = set(nums)
        longest = 0
        for x in numSet:
            if (x-1) not in numSet:
                length = 0
                while (x+length) in numSet:
                    length +=1 
                longest = max(length,longest)
        return longest
