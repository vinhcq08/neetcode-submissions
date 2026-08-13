class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        counter = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                counter += 1
        for e in nums:
            if counter == 0:
                result.append(int(prod/e))
            if counter == 1:
                if e != 0:
                    result.append(0)
                else:
                    result.append(int(prod))
            if counter > 1:
                result.append(0)
        return result

            
                 
        