class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        verify = {}
        for current_index,i in enumerate(nums):
            complementary = target - i
            if complementary in verify:
                return [verify[complementary], current_index]
            verify[i] = current_index