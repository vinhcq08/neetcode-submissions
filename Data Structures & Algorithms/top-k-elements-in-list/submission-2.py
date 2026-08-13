class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        frequency = sorted(dic.values(), reverse = True)
        for e in frequency[:k]:
            for number , count in dic.items():
                if count == e and number not in result:
                    result.append(number)
                else:
                    pass
        return result
        