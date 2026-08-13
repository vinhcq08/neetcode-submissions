#Optimized by ChatGPT
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []
        for i in nums:
            dic[i] = dic.get(i,0) + 1
            #get current number i if it exists, else get 0
        frequency = sorted(dic.items(),key = lambda items:items[1], reverse = True)
        #key = lambda items: items[1] call for second element in each tuple pair
        return [num for num , count in frequency[:k]]
        