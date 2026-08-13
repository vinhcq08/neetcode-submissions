class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        duplicate_check = set()
        for target_index,target in enumerate(nums):
            verify = dict()
            for cur_index, value in enumerate(nums):
                if cur_index == target_index:
                    continue
                comp =  -(target + value)
                if comp in verify:
                    triplet = tuple(sorted([target,value,comp]))
                    if triplet not in duplicate_check:
                        duplicate_check.add(triplet)
                        result.append(list(triplet))
                verify[value] = cur_index
        return result