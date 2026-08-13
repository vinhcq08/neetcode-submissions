class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        verify = dict()
        for cur_index,value in enumerate(numbers):
            comple = target - value
            if comple in verify:
                return sorted([cur_index+1,verify[comple]+1])
            verify[value] = cur_index