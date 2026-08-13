#Brute force idea
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        frequency = sorted(list(dic.values()))[::-1]
        for e in range(k):
            for a , b in dic.items():
                if b == frequency[e]:
                    if a in result:
                        pass
                    else:
                        result.append(a)
                else:
                    pass
        return result

            