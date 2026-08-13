class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        frequency = sorted(dic.items(),key = lambda items:items[1], reverse = True)
        return [num for num , count in frequency[:k]]
        